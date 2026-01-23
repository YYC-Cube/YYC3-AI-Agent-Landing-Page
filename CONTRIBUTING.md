# 贡献指南

感谢您对 YYC³ AI Landing Page 项目的关注！我们欢迎所有形式的贡献。

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [提交规范](#提交规范)
- [问题反馈](#问题反馈)

---

## 🤝 行为准则

参与本项目即表示您同意遵守以下行为准则：

- 尊重所有贡献者
- 接受建设性批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同理心

---

## 🚀 如何贡献

### 报告 Bug

如果您发现了 Bug，请：

1. 检查 [Issues](https://github.com/YYC-Cube/yyc3-ai-landing-page/issues) 确认该 Bug 是否已被报告
2. 如果未被报告，创建一个新的 Issue
3. 在 Issue 中提供：
   - 清晰的标题和描述
   - 复现步骤
   - 预期行为
   - 实际行为
   - 截图（如适用）
   - 环境信息（操作系统、浏览器、Node.js 版本等）

### 提交功能请求

如果您有新功能的想法：

1. 检查 [Issues](https://github.com/YYC-Cube/yyc3-ai-landing-page/issues) 确认该功能是否已被请求
2. 如果未被请求，创建一个新的 Issue
3. 在 Issue 中提供：
   - 功能描述
   - 使用场景
   - 预期收益
   - 可能的实现方案（如有）

### 提交代码

如果您想直接贡献代码：

1. Fork 本仓库
2. 创建功能分支
3. 进行开发
4. 提交代码
5. 推送到您的 Fork
6. 创建 Pull Request

---

## 🔄 开发流程

### 1. 设置开发环境

```bash
# Fork 并克隆仓库
git clone https://github.com/your-username/yyc3-ai-landing-page.git
cd yyc3-ai-landing-page

# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev
```

### 2. 创建分支

```bash
# 功能分支
git checkout -b feature/your-feature-name

# 修复分支
git checkout -b fix/your-bug-fix
```

### 3. 开发

- 遵循项目的代码规范
- 添加必要的测试
- 更新相关文档
- 确保所有测试通过

### 4. 提交代码

```bash
# 添加更改
git add .

# 提交更改（遵循提交规范）
git commit -m "feat: add new feature"

# 推送到远程
git push origin feature/your-feature-name
```

### 5. 创建 Pull Request

1. 访问 GitHub 上的您的 Fork
2. 点击 "New Pull Request"
3. 选择您的功能分支
4. 填写 PR 模板
5. 等待代码审查

---

## 📝 代码规范

### TypeScript

- 使用 TypeScript 严格模式
- 为所有函数、组件、变量添加类型注解
- 避免使用 `any` 类型
- 使用接口定义数据结构

### 命名规范

- **组件**：PascalCase（如：`UserProfile.tsx`）
- **文件**：kebab-case（如：`user-service.ts`）
- **函数**：camelCase（如：`getUserData`）
- **常量**：UPPER_SNAKE_CASE（如：`API_BASE_URL`）
- **接口**：PascalCase，以 `I` 开头（如：`IUser`）

### 组件规范

- 使用函数式组件
- 使用 TypeScript 接口定义 Props
- 添加适当的注释
- 保持组件单一职责

### 样式规范

- 优先使用 Tailwind CSS
- 避免内联样式
- 使用语义化的类名
- 保持样式一致性

---

## 🎯 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

### 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### 类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整（不影响功能）
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建或辅助工具变动
- `ci`: CI/CD 相关
- `build`: 构建系统或依赖变动

### 示例

```bash
feat(i18n): 添加日语语言支持

- 更新 i18n 配置文件
- 添加日语翻译字典
- 更新语言切换器组件

Closes #123
```

```bash
fix(auth): 修复登录时的认证错误

修复了用户登录时因 token 过期导致的认证失败问题。

Fixes #456
```

---

## 🐛 问题反馈

### 报告 Bug

在报告 Bug 时，请提供：

- 清晰的标题和描述
- 复现步骤
- 预期行为
- 实际行为
- 截图（如适用）
- 环境信息：
  - 操作系统
  - 浏览器及版本
  - Node.js 版本
  - 包管理器及版本

### 功能请求

在提交功能请求时，请提供：

- 功能描述
- 使用场景
- 预期收益
- 可能的实现方案（如有）

---

## 📧 联系我们

- **技术支持**：<admin@0379.email>
- **GitHub Issues**：[https://github.com/YYC-Cube/yyc3-ai-landing-page/issues](https://github.com/YYC-Cube/yyc3-ai-landing-page/issues)

---

## 📄 许可证

通过贡献代码，您同意您的贡献将根据项目的 [MIT 许可证](LICENSE) 进行许可。

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
