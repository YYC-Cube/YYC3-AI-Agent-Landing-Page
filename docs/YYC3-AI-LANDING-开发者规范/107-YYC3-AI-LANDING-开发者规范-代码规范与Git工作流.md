---
file: 107-YYC3-AI-LANDING-开发者规范-代码规范与Git工作流.md
description: YYC3-AI-Landing-Page 代码规范与 Git 工作流标准
author: YYC³ Team
version: v1.0.0
created: 2026-09-28
updated: 2026-09-28
status: published
tags: [代码规范, Git, Conventional Commits, TypeScript]
category: standard
---

# 📐 代码规范与 Git 工作流

> 状态：✅ 与项目实况对齐（2026-09-28）| 校准来源：tsconfig.json / eslint.config.mjs / CONTRIBUTING.md

## 一、TypeScript 规范

### 1.1 编译器门禁（不可关闭）

以下选项在 [tsconfig.json](../../tsconfig.json) 中已启用，PR 中不得降级：

| 选项 | 值 | 含义 |
| ---- | -- | ---- |
| `strict` | `true` | 严格模式全套（含 strictNullChecks 等 7 项） |
| `noUncheckedIndexedAccess` | `true` | 索引访问自动附加 `undefined` |
| `noUnusedLocals` | `true` | 未用局部变量报错 |
| `noUnusedParameters` | `true` | 未用参数报错（前缀 `_` 豁免） |
| `noFallthroughCasesInSwitch` | `true` | switch 穿透报错 |
| `isolatedModules` | `true` | 类型导出必须 `import type` |

```bash
pnpm typecheck   # tsc --noEmit，0 errors 方可通过
```

### 1.2 类型编写细则

- **禁止显式 `any`**（ESLint `@typescript-eslint/no-explicit-any` 强制）；确实未知时用 `unknown` + 类型收窄
- **类型导入统一使用 `import type`**：`import type { LucideIcon } from "lucide-react"`
- **组件 Props 用 `interface`** 且以 Props 结尾：`interface NavbarProps { ... }`
- **第三方库类型**优先从包内导出获取（如 `@tsparticles/engine` 的 `ISourceOptions`），不得手写重复结构

## 二、命名规范

| 对象 | 规则 | 示例 |
| ---- | ---- | ---- |
| 组件文件/组件名 | PascalCase | `navbar.tsx` 导出 `Navbar` |
| Hooks 文件 | `use-*.ts` kebab-case | `hooks/use-media-query.ts` |
| 普通工具文件 | kebab-case | `lib/utils.ts` |
| 函数/变量 | camelCase | `getPortfolioData` |
| 常量 | UPPER_SNAKE_CASE | `API_BASE_URL` |
| 类型/接口 | PascalCase | `NavbarProps`、`Locale` |
| CSS 类（组件层） | kebab-case | `.glass-panel`（全局层） |

## 三、React / Next.js 组件规范

### 3.1 组件形态

- **函数式组件 + 箭头函数**，显式返回类型 `ReactElement` 或省略由推断
- **单一职责**：一个文件一个默认导出组件，附属子组件内聚同文件
- **Props 解构**在参数位完成，禁止组件体内 `props.xxx` 逐次访问

### 3.2 Server / Client 边界

- 默认 **Server Component**；仅在需要 hooks/事件/浏览器 API 时添加 `"use client"`
- `"use client"` 必须位于文件首行、所有 import 之前
- 客户端组件中的浏览器 API（`matchMedia`、`localStorage`）必须处理 SSR 安全：
  - 订阅型状态用 `useSyncExternalStore`（参考 [use-media-query.ts](../../hooks/use-media-query.ts)）
  - 持久化水合在 effect 中读取后 setState（需 `/* eslint-disable react-hooks/set-state-in-effect */` 豁免并注释原因，参考 [locale-context.tsx](../../contexts/locale-context.tsx)）

### 3.3 Effect 纪律（React 19 lint 规则）

- **禁止在 effect 中直接根据 props/state 推导 setState**（`react-hooks/set-state-in-effect`）
- 事件驱动的状态转换写在事件处理器内聚函数中，effect 仅用于订阅/清理
- 订阅必须返回清理函数

### 3.4 路径别名

统一使用 `@/*` 映射仓库根目录（tsconfig paths）：

```tsx
import { Button } from "@/components/ui/button";
```

## 四、样式规范（Tailwind v4 CSS-first）

- **本项目为 Tailwind v4，无 `tailwind.config.ts`**——主题令牌全部位于 [globals.css](../../app/globals.css) 的 `@theme` 块
- 优先使用工具类；重复组合 ≥ 3 处时提取语义类（globals.css 全局层）或组件
- 颜色/间距/圆角只用设计令牌（`primary`、`muted`、`border` 等语义变量），禁止裸十六进制
- 禁止内联 `style` 处理静态样式（动态计算值除外）
- 深色/浅色模式通过 CSS 变量切换，组件不写死颜色

## 五、Git 工作流

### 5.1 分支模型

```
main ──────────────────────────────► 生产分支（受保护，仅经 PR 或直接规范提交）
  └─ feature/<scope>-<desc>         功能开发
  └─ fix/<scope>-<desc>             缺陷修复
  └─ chore/<scope>-<desc>           构建/工具/依赖
```

- `main` 与 GitHub Pages 部署联动（[deploy-pages.yml](../../.github/workflows/deploy-pages.yml) 监听 push main）
- Dependabot 分支（`dependabot/npm_and_yarn/...`）经 CI 门禁后合入

### 5.2 Conventional Commits（强制）

完整规范见 [CONTRIBUTING.md](../../CONTRIBUTING.md)，速查：

```
<type>(<scope>): <简述>

feat: 新功能 | fix: 缺陷 | docs: 文档 | style: 格式
refactor: 重构 | perf: 性能 | test: 测试 | chore: 杂务
ci: CI/CD    | build: 依赖/构建
```

- 简述使用中文或英文均可，**句末不加标点**
- 破坏性变更必须携带 `!` 或 footer `BREAKING CHANGE:`
- 关联 Issue 使用 `Closes #123` / `Fixes #456`

### 5.3 提交前门禁（本地必须全绿）

```bash
pnpm lint && pnpm typecheck && pnpm build
```

| 检查 | 工具 | 通过标准 |
| ---- | ---- | -------- |
| Lint | `eslint .`（flat config） | 0 errors |
| 类型 | `tsc --noEmit` | 0 errors |
| 构建 | `next build`（静态导出 out/） | 成功产出 index.html / 404.html |

### 5.4 敏感信息红线

- `.env*` 一律不入库（.gitignore 已覆盖）
- 提交前自查：无硬编码密钥、Token、密码；占位符使用 `${ENV_VAR}` 格式

## 六、AI 协同开发附加约定

- 遵循 YYC³ 会话文档四件套（00 审核 / 01 规划 / 02 日志 / 03 总结），目录 `docs/{项目名}-{导师}-{YYYYMMDD}`
- 开发服务器固定端口 3030 起
- 重大重构（如依赖大版本升级）必须先在会话文档中记录决策依据（例：tsparticles 锁定 v3 的原因见 00-审核报告）

---

> 「***YanYuCloudCube***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
