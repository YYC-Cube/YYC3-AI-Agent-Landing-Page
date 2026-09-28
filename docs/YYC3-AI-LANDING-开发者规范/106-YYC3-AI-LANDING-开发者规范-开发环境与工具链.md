---
file: 106-YYC3-AI-LANDING-开发者规范-开发环境与工具链.md
description: YYC3-AI-Landing-Page 开发环境与工具链规范
author: YYC³ Team
version: v1.0.0
created: 2026-09-28
updated: 2026-09-28
status: published
tags: [开发环境, 工具链, pnpm, Node]
category: standard
---

# 🛠️ 开发环境与工具链规范

> 状态：✅ 与项目实况对齐（2026-09-28）| 校准来源：package.json / pnpm-workspace.yaml

## 一、运行时要求

| 工具 | 最低版本 | 锁定机制 | 说明 |
| ---- | -------- | -------- | ---- |
| Node.js | **>= 20.9.0** | `engines.node` | Next.js 16 要求；CI 使用 Node 22 LTS |
| pnpm | **>= 10.0.0** | `engines.pnpm` + `packageManager` | 本项目锁定 `pnpm@11.10.0`（corepack 可自动启用） |

```bash
# 启用 corepack 自动匹配 packageManager 指定的 pnpm 版本
corepack enable
pnpm -v   # 应输出 11.10.0
```

## 二、依赖管理策略

### 2.1 安装与锁定

```bash
pnpm install                    # 日常安装
pnpm install --frozen-lockfile  # CI/协作者必须（与 pnpm-lock.yaml 严格一致）
```

- **锁定文件必须提交**：`pnpm-lock.yaml` 是部署一致性的基石
- **禁止使用 `latest` 浮动版本**：所有依赖必须显式声明版本范围（`^` 主版本锁定）
- **幽灵依赖零容忍**：仅保留被 import 的依赖（本项目 2026-09-28 清理 40+ 未用依赖）

### 2.2 供应链防护（pnpm 11）

构建脚本白名单位于 [pnpm-workspace.yaml](../../pnpm-workspace.yaml)：

```yaml
allowBuilds:
  '@tsparticles/engine': true   # 允许执行安装脚本
  unrs-resolver: true
```

- 未列入白名单的依赖**不允许**执行 postinstall 脚本（默认拒绝）
- 新增带构建脚本的依赖时，必须审查其脚本内容后手动加入 `allowBuilds`
- CI 使用 `--frozen-lockfile` 防止锁文件漂移

### 2.3 依赖升级流程

```bash
pnpm view <pkg> version     # 查询最新版本
# 编辑 package.json → pnpm install --no-frozen-lockfile
pnpm lint && pnpm typecheck && pnpm build   # 三门禁全绿后提交
```

- **重大版本升级**（如 tsparticles v3→v4）：必须审查 breaking changes 与 API 类型定义
- 依赖安全更新由 **Dependabot** 自动发起 PR，经 CI 门禁后人合入

## 三、本地开发

```bash
pnpm dev   # 开发服务器，端口 3030（YYC³ 团队端口规范）
```

| 脚本 | 命令 | 用途 |
| ---- | ---- | ---- |
| `dev` | `next dev -p 3030` | 开发服务器（端口规范 3030 起） |
| `build` | `next build` | 生产构建 + 静态导出至 `out/` |
| `lint` | `eslint .` | ESLint flat config 检查 |
| `lint:fix` | `eslint . --fix` | 自动修复 |
| `typecheck` | `tsc --noEmit` | 类型检查 |
| `preview` | `npx serve out` | 预览静态导出产物 |

## 四、编辑器与工具约定

- **TypeScript**：严格模式全套（strict / noUncheckedIndexedAccess / noUnusedLocals），禁止关闭
- **ESLint**：flat config（[eslint.config.mjs](../../eslint.config.mjs)），继承 `next/core-web-vitals` + `next/typescript`
- **Git 忽略**：`.env*`、`.next/`、`out/`、`node_modules/` 一律不入库
- **敏感信息**：仅通过环境变量注入，任何密钥不得硬编码

## 五、检查清单（新成员入职）

- [ ] Node >= 20.9.0 已安装
- [ ] corepack/pnpm >= 10 已启用
- [ ] `pnpm install --frozen-lockfile` 成功
- [ ] `pnpm dev` 在 3030 端口正常启动
- [ ] `pnpm lint && pnpm typecheck` 全绿
- [ ] 已阅读 107 代码规范与 108 CI/CD 规范

---

> 「***YanYuCloudCube***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
