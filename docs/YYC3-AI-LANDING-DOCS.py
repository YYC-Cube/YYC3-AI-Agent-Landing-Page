import os
import json
import time
import anthropic
from dotenv import load_dotenv
from pathlib import Path

# 加载环境变量（.env文件配置ANTHROPIC_API_KEY=你的密钥）
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# 项目配置
PROJECT_ROOT = Path(__file__).parent  # docs目录
DOC_STRUCTURE = PROJECT_ROOT / "YYC3-AI-LANDING-文档映射目录.md"
VALIDATE_RULES = PROJECT_ROOT / "YYC3-AI-LANDING-文档校验规则.json"
PROJECT_CONTEXT = PROJECT_ROOT / "YYC3-AI-LANDING-项目上下文.md"
FORMAT_SPEC = PROJECT_ROOT / "YYC3-AI-LANDING-文档格式规范.md"
LOG_FILE = PROJECT_ROOT / "YYC3-AI-LANDING-DOCS-LOG.md"

# 任务清单（可从JSON文件加载，此处简化为字典）
TASK_LIST = {
    # 需求规划任务
    "R001": {
        "file_path": PROJECT_ROOT / "YYC3-AI-LANDING-需求规划/001-YYC3-AI-LANDING-需求规划-项目章程.md",
        "content_desc": "编写YYC3-AI-LANDING项目章程，包含项目名称/目标/范围/利益相关者/启动时间",
        "acceptance_criteria": "1. 包含所有必填章节；2. 格式符合规范；3. 内容匹配项目上下文",
        "loop_mode": "human_collab",  # 人机协作版
        "status": "pending"  # pending/running/passed/failed
    },
    # API文档任务（示例）
    "A001": {
        "file_path": PROJECT_ROOT / "YYC3-AI-LANDING-API文档/056-YYC3-AI-LANDING-API文档-通用规范-RESTful接口设计标准.md",
        "content_desc": "编写RESTful接口设计标准，包含接口命名/请求方式/参数规则/响应格式/错误码规则",
        "acceptance_criteria": "1. 包含所有必填章节；2. 接口命名符合RESTful规范；3. 示例代码可直接复制",
        "loop_mode": "afk",  # 挂机版
        "status": "pending"
    },
    # 可扩展更多任务...
}

class DocRalphLoop:
    def __init__(self):
        # 加载基础规范
        self.context = self._read_file(PROJECT_CONTEXT)
        self.format_spec = self._read_file(FORMAT_SPEC)
        self.validate_rules = json.loads(self._read_file(VALIDATE_RULES))
        # 初始化日志
        self._init_log()

    def _read_file(self, file_path):
        """读取文件内容，处理编码问题"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            self._log(f"读取文件失败 {file_path}：{str(e)}")
            return ""

    def _write_file(self, file_path, content):
        """写入文档，自动创建目录"""
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self._log(f"成功写入文档：{file_path}")
            return True
        except Exception as e:
            self._log(f"写入文件失败 {file_path}：{str(e)}")
            return False

    def _init_log(self):
        """初始化日志文件"""
        if not LOG_FILE.exists():
            self._write_file(LOG_FILE, "# YYC3-AI-LANDING文档闭环日志\n")

    def _log(self, content):
        """记录日志（带时间戳）"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_content = f"\n## {timestamp}\n{content}"
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_content)

    def _call_ai(self, task):
        """调用Claude编写/更新文档"""
        prompt = f"""
        你是YYC3-AI-LANDING项目的文档工程师，需按以下要求完成文档编写：

        ### 项目上下文（必须严格匹配）
        {self.context}

        ### 格式规范（必须严格遵守）
        {self.format_spec}

        ### 任务要求
        文档路径：{task['file_path']}
        编写内容：{task['content_desc']}
        验收标准：{task['acceptance_criteria']}

        ### 输出要求
        1. 直接输出完整的Markdown文档内容，无需额外说明；
        2. 严格遵循格式规范，标题层级、列表、代码块符合要求；
        3. 内容需量化，避免模糊表述（如“优化性能”需改为“页面加载≤2s”）；
        4. 匹配项目上下文，符合YYC3-AI-LANDING的AI Landing页定位。
        """

        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=8000,
                temperature=0.1,  # 低随机性，保证标准化
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content.strip()
        except Exception as e:
            self._log(f"AI调用失败：{str(e)}")
            return ""

    def _validate_doc(self, task, doc_content):
        """文档自动化校验（格式+必填项+基础合规性）"""
        errors = []
        file_path = task["file_path"]

        # 1. 文件名校验
        file_name = file_path.name
        if not file_name.startswith(f"{file_name.split('-')[0]}-YYC3-AI-LANDING-"):
            errors.append(f"文件名不符合规范：{file_name}")

        # 2. 必填章节校验（简化示例，可扩展更细规则）
        if "项目章程" in file_name:
            required_sections = ["项目名称", "项目目标", "项目范围", "利益相关者"]
            for section in required_sections:
                if section not in doc_content:
                    errors.append(f"缺失必填章节：{section}")

        # 3. 格式校验（标题层级、代码块）
        if "# " not in doc_content:  # 无一级标题
            errors.append("缺失一级标题（# 文档名）")
        if "```" in doc_content and "```python" not in doc_content and "```bash" not in doc_content:
            errors.append("代码块未指定语言标识")

        # 4. 项目上下文匹配度（简单关键词校验）
        core_keywords = ["AI Landing页", "React", "TypeScript", "Spline 3D"]
        match_count = sum(1 for keyword in core_keywords if keyword in doc_content)
        if match_count < len(core_keywords) * 0.8:
            errors.append(f"项目上下文匹配度不足，仅匹配{match_count}个核心关键词")

        # 返回校验结果
        if errors:
            self._log(f"文档校验失败 {file_path}：{'; '.join(errors)}")
            return False, errors
        else:
            self._log(f"文档校验通过 {file_path}")
            return True, []

    def _human_review_prompt(self, task):
        """人机协作版：提示人工审核"""
        print(f"\n===== 需人工审核任务 {task['file_path'].name} =====")
        print(f"验收标准：{task['acceptance_criteria']}")
        print(f"文档路径：{task['file_path']}")
        while True:
            choice = input("审核结果（通过/不通过/修改）：")
            if choice == "通过":
                return True, []
            elif choice == "不通过":
                reason = input("不通过原因：")
                return False, [reason]
            elif choice == "修改":
                suggestion = input("修改建议：")
                return False, [suggestion]
            else:
                print("请输入 通过/不通过/修改")

    def run_loop(self):
        """启动Ralph Loop核心循环"""
        self._log("===== 启动YYC3-AI-LANDING文档闭环 =====")

        # 遍历所有任务
        for task_id, task in TASK_LIST.items():
            if task["status"] == "passed":
                continue  # 跳过已完成任务

            self._log(f"\n开始处理任务 {task_id}：{task['file_path'].name}")
            task["status"] = "running"
            retry_count = 0
            max_retry = 3  # 最大重试次数

            # 单任务迭代闭环
            while retry_count < max_retry:
                # 1. AI编写/更新文档
                doc_content = self._call_ai(task)
                if not doc_content:
                    retry_count += 1
                    self._log(f"任务 {task_id} AI返回为空，重试第{retry_count}次")
                    time.sleep(2)
                    continue

                # 2. 自动化校验
                validate_pass, errors = self._validate_doc(task, doc_content)

                # 3. 人机协作版：触发人工审核
                if task["loop_mode"] == "human_collab":
                    human_pass, human_errors = self._human_review_prompt(task)
                    if not human_pass:
                        validate_pass = False
                        errors = human_errors

                # 4. 校验通过：保存文档
                if validate_pass:
                    self._write_file(task["file_path"], doc_content)
                    task["status"] = "passed"
                    self._log(f"任务 {task_id} 完成")
                    break

                # 5. 校验失败：重试
                retry_count += 1
                self._log(f"任务 {task_id} 校验失败，重试第{retry_count}次，原因：{errors}")
                time.sleep(3)  # 重试间隔

            # 任务重试耗尽仍失败
            if retry_count >= max_retry:
                task["status"] = "failed"
                self._log(f"任务 {task_id} 重试{max_retry}次仍失败，标记为失败")

        # 闭环结束：更新文档映射目录
        self._update_doc_mapping()
        self._log("===== 文档闭环执行完成 =====")
        print("\n闭环执行完成，日志已保存至：", LOG_FILE)

    def _update_doc_mapping(self):
        """自动更新文档映射目录（YYC3-AI-LANDING-文档映射目录.md）"""
        mapping_content = "# YYC3-AI-LANDING文档映射目录\n\n"
        # 按目录分组生成映射
        dir_tasks = {}
        for task in TASK_LIST.values():
            dir_name = task["file_path"].parent.name
            if dir_name not in dir_tasks:
                dir_tasks[dir_name] = []
            dir_tasks[dir_name].append({
                "name": task["file_path"].name,
                "status": task["status"]
            })

        # 生成映射内容
        for dir_name, tasks in dir_tasks.items():
            mapping_content += f"## {dir_name}\n"
            for task in tasks:
                status_tag = "✅" if task["status"] == "passed" else "❌" if task["status"] == "failed" else "🔄"
                mapping_content += f"- {status_tag} {task['name']}\n"

        # 写入映射文件
        self._write_file(DOC_STRUCTURE, mapping_content)

if __name__ == "__main__":
    # 启动文档闭环
    doc_loop = DocRalphLoop()
    doc_loop.run_loop()
