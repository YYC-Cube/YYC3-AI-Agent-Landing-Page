# 🔖 YYC³ AI Agent Landing Page

![YYC³ AI Agent Landing Page](public/yyc3-family.png)

> ***YanYuCloudCube***

> 言启象限 | 语枢未来

> ***Words Initiate Quadrants, Language Serves as Core for the Future***

> 万象归元于云枢 | 深栈智启新纪元

> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

## 🛡️ 徽章体系

### 状态徽章

| 徽章 | 说明 |
| ---- | ---- |
| [![CI](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/actions/workflows/ci.yml/badge.svg)](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/actions/workflows/ci.yml) | 持续集成：Lint + Typecheck + Build 质量门禁 |
| [![Deploy Pages](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/actions/workflows/deploy-pages.yml) | GitHub Pages 自动部署 |
| [![Website](https://img.shields.io/website?url=https%3A%2F%2Fai-landing.yyc3.top&label=%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83)](https://ai-landing.yyc3.top) | 生产环境在线状态 |
| ![License](https://img.shields.io/badge/License-MIT-green?style=flat) | MIT 开源许可证 |

### 技术栈徽章

![Next.js](https://img.shields.io/badge/Next.js-16.3-000000?style=flat&logo=next.js)
![React](https://img.shields.io/badge/React-19.3-61DAFB?style=flat&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=flat&logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.3-38B2AC?style=flat&logo=tailwind-css)
![Radix UI](https://img.shields.io/badge/Radix_UI-latest-161618?style=flat&logo=radix-ui)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-new--york-000000?style=flat&logo=shadcnui)

### 工程规范徽章

![pnpm](https://img.shields.io/badge/pnpm-%E2%89%A510-F69220?style=flat&logo=pnpm)
![Node.js](https://img.shields.io/badge/Node-%E2%89%A520.9-339933?style=flat&logo=nodedotjs)
![Conventional Commits](https://img.shields.io/badge/Conventional_Commits-1.0.0-FE5196?style=flat&logo=conventionalcommits)
![Code Style: ESLint](https://img.shields.io/badge/Code_Style-ESLint_flat-4B32C3?style=flat&logo=eslint)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🏷️ 标签 / 关键词

**GitHub Topics**（推荐配置到仓库 About → Topics）：

```text
nextjs  react  typescript  tailwindcss  shadcn-ui  radix-ui  framer-motion
spline  tsparticles  landing-page  ai-agent  github-pages  pnpm  i18n
static-site  app-router  dark-theme  responsive  ci-cd  yyc3
```

**语义关键词**：AI 代理落地页 · 国际化 · 3D 场景 · 粒子动效 · 静态导出 · 自动化部署 · 五高五标五化

---

## 📋 项目概述

**YYC³(YanYuCloudCube) AI Agent Landing Page** 是一个现代化的 AI 代理服务落地页，采用 **Next.js 16 (App Router)** 构建，集成了国际化系统、Spline 3D 场景交互、粒子动画和响应式设计。生产环境通过 **GitHub Pages** 自动部署：**[https://ai-landing.yyc3.top](https://ai-landing.yyc3.top)**

### 核心特性

- 🌍 **国际化支持** - 基于 React Context 的中英双语系统，localStorage 持久化
- 🎨 **现代化 UI** - 基于 shadcn/ui (new-york) + Radix UI 原语
- 🎬 **丰富动效** - Framer Motion、Spline 3D 场景、tsparticles 粒子动画、confetti 庆祝
- 📱 **响应式设计** - 完美适配桌面、平板、移动设备
- ⚡ **静态导出** - `output: 'export'` 全静态化，Pages/CDN 友好
- 🔒 **类型安全** - TypeScript strict + noUncheckedIndexedAccess
- 🤖 **CI 自动化** - push 即 lint + typecheck + build + 部署全链路闭环

---

## 🚀 快速开始

### 环境要求

- Node.js >= 20.9.0
- pnpm >= 10.0.0（通过 `packageManager` 字段自动锁定）

### 安装依赖

```bash
pnpm install
```

### 启动开发服务器

```bash
pnpm dev
# 访问 http://localhost:3030
```

### 质量门禁（本地验证）

```bash
pnpm lint        # ESLint (flat config, next/core-web-vitals + typescript)
pnpm typecheck   # tsc --noEmit
pnpm build       # 生产构建 + 静态导出至 out/
```

### 预览生产构建

```bash
pnpm build && pnpm preview   # 静态预览 out/ 目录
```

---

## 📚 技术栈（与 package.json 对齐）

### 核心框架

| 技术 | 版本 | 用途 |
| ------ | ------ | ------ |
| Next.js | ^16.3.6 | React 框架，App Router + 静态导出 |
| React / React DOM | ^19.3.0 | UI 库 |
| TypeScript | ^5.9.3 | 类型安全（strict 模式） |
| Tailwind CSS | ^4.3.3 | 原子化 CSS（v4 CSS-first，无 tailwind.config） |

### UI 组件库

| 技术 | 版本 | 用途 |
| ------ | ------ | ------ |
| shadcn/ui | new-york style | 可复用组件系统（components.json） |
| Radix UI | ^2.x（按需 5 个原语） | dropdown-menu / label / switch / slot / icons |
| Lucide Icons | ^1.48.0 | 图标库（品牌图标已内联 SVG 化） |

### 动画与交互

| 技术 | 版本 | 用途 |
| ------ | ------ | ------ |
| Framer Motion | ^13.4.4 | 动画编排（Spotlight/渐变背景/定价卡） |
| @splinetool/react-spline | ^4.1.0 | Spline 3D 场景（lazy 加载） |
| @tsparticles/react | ^3.0.0 | 粒子动画（slim 引擎） |
| canvas-confetti | ^1.9.4 | 定价切换庆祝动效 |

### 工程化

| 技术 | 版本 | 用途 |
| ------ | ------ | ------ |
| ESLint | ^9.39.5 + eslint-config-next ^16.3.6 | Flat config 代码规范 |
| @vercel/analytics | ^2.0.1 | 访问分析 |
| geist | ^1.7.2 | 字体系统 |
| tw-animate-css | ^1.4.0 | Tailwind v4 动画工具类 |

---

## 📁 项目结构

```
yyc3-ai-agent-landing-page/
├── app/                      # Next.js App Router（静态导出）
│   ├── layout.tsx            # 根布局（metadataBase: ai-landing.yyc3.top）
│   ├── page.tsx              # 首页
│   ├── globals.css           # 全局样式（Tailwind v4 CSS-first）
│   ├── privacy/page.tsx      # 隐私政策页
│   └── terms/page.tsx        # 服务条款页
├── components/
│   └── ui/                   # UI 组件（navbar/pricing/bento-grid/spotlight/sparkles/
│                             #   spline-scene/animated-gradient-background/
│                             #   language-switcher/social-icons + shadcn 基础组件）
├── contexts/
│   └── locale-context.tsx    # 语言上下文
├── hooks/
│   └── use-media-query.ts    # 媒体查询 Hook (useSyncExternalStore)
├── lib/
│   ├── i18n.ts               # 国际化字典与配置
│   └── utils.ts              # cn() 工具函数
├── public/                   # 静态资源
│   ├── CNAME                 # GitHub Pages 自定义域名
│   ├── favicon-*.png         # 站点图标
│   └── yyc3/                 # 全平台应用图标（iOS/Android/macOS/watchOS/Web）
├── docs/                     # YYC³ 标准化文档体系（001-108）
├── .github/workflows/
│   ├── ci.yml                # CI 质量门禁
│   └── deploy-pages.yml      # Pages 自动部署
├── next.config.mjs           # output: 'export' + images.unoptimized
├── eslint.config.mjs         # ESLint flat config
└── pnpm-workspace.yaml       # pnpm 11 设置（allowBuilds）
```

---

## 🎨 样式与主题

项目使用 **Tailwind CSS v4**（CSS-first 配置，**无 tailwind.config 文件**），主题通过 [app/globals.css](app/globals.css) 中的 CSS 变量定义：

- 深色主题（默认）+ oklch 颜色系统
- `@custom-variant dark` 类切换策略
- tw-animate-css 提供动画工具类
- 响应式断点：`sm: 640px` / `md: 768px` / `lg: 1024px` / `xl: 1280px`

---

## 🔧 配置说明

### 环境变量

创建 `.env.local` 文件（已加入 .gitignore）：

```env
# Vercel Analytics（可选）
NEXT_PUBLIC_GA_ID=
```

### TypeScript 配置

项目使用 TypeScript 严格模式：`strict` + `noUncheckedIndexedAccess` + `noUnusedLocals` + `noFallthroughCasesInSwitch`，详见 [tsconfig.json](tsconfig.json)。

### 关键构建配置

| 配置 | 值 | 原因 |
| ---- | ---- | ---- |
| `output` | `'export'` | GitHub Pages 静态托管 |
| `images.unoptimized` | `true` | 静态导出不支持图片优化服务 |
| `trailingSlash` | `true` | Pages 目录索引路由兼容 |
| 开发端口 | `3030` | YYC³ 团队开发服务器端口规范 |

---

## 🚢 部署

### GitHub Pages 自动部署（当前方案）

**生产地址**：[https://ai-landing.yyc3.top](https://ai-landing.yyc3.top)

- 推送 `main` 分支自动触发 [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml)
- 流水线：install → lint → typecheck → build（静态导出）→ deploy-pages
- 自定义域名：`public/CNAME` → `ai-landing.yyc3.top`
- 首次启用（一次性）：仓库 **Settings → Pages → Source 选择「GitHub Actions」**，并确保域名 DNS CNAME 记录指向 `<org>.github.io`

### CI 质量门禁

[.github/workflows/ci.yml](.github/workflows/ci.yml) 在 push/PR 时执行：

1. `pnpm install --frozen-lockfile`
2. `pnpm lint`（ESLint 0 error 门禁）
3. `pnpm typecheck`（tsc 0 error 门禁）
4. `pnpm build`（构建成功门禁）
5. 产物上传（保留 7 天）

---

## 🧪 测试

测试体系处于规划阶段（详见 [docs/YYC3-AI-LANDING-测试文档](docs/YYC3-AI-LANDING-测试文档/)）：

- **单元测试** - Vitest（规划中）
- **组件测试** - React Testing Library（规划中）
- **E2E 测试** - Playwright（规划中）

---

## 🔒 安全

- 无硬编码密钥或凭据，环境变量管理敏感信息
- `.env*` 全部加入 .gitignore
- CI 中使用 `--frozen-lockfile` + pnpm 11 `allowBuilds` 构建脚本白名单（供应链防护）
- 依赖安全由 Dependabot 自动更新（见历史 PR）
- 安全漏洞反馈：见 [SECURITY.md](SECURITY.md)

---

## 📝 文档体系

YYC³ 标准化文档体系（编号详见 [文档映射目录](docs/YYC3-AI-LANDING-文档映射目录.md)）：

| 分类 | 编号 | 说明 |
| ---- | ---- | ---- |
| [需求规划](docs/YYC3-AI-LANDING-需求规划/) | 001-007 | 章程/可行性/需求说明书 |
| [项目规划](docs/YYC3-AI-LANDING-项目规划/) | 011-016 | 进度/资源/风险/沟通 |
| [架构设计](docs/YYC3-AI-LANDING-架构设计/) | 021-031 | 系统/数据/安全/部署架构 |
| [详细设计](docs/YYC3-AI-LANDING-详细设计/) | 036-054 | 模块/UI-UX/i18n/SEO |
| [API 文档](docs/YYC3-AI-LANDING-API文档/) | 056-073 | RESTful 规范/业务域接口 |
| [类型定义](docs/YYC3-AI-LANDING-类型定义/) | 074-080 | TS 全局类型/组件 Props |
| [测试文档](docs/YYC3-AI-LANDING-测试文档/) | 081-089 | 单元/集成/E2E/性能规范 |
| [部署运维](docs/YYC3-AI-LANDING-部署运维/) | 090-099 | 部署方案/CI/CD/监控 |
| [用户手册](docs/YYC3-AI-LANDING-用户手册/) | 100-105 | 快速开始/FAQ/故障排除 |
| [开发者规范](docs/YYC3-AI-LANDING-开发者规范/) | 106-108 | 工具链/代码规范/CI-CD 标规 |

### 社区文档

- [CONTRIBUTING.md](CONTRIBUTING.md) - 贡献指南
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 行为准则
- [SECURITY.md](SECURITY.md) - 安全策略
- [CHANGELOG.md](CHANGELOG.md) - 变更日志

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
# 1. Fork 后创建功能分支
git checkout -b feature/AmazingFeature

# 2. 开发并通过本地质量门禁
pnpm lint && pnpm typecheck && pnpm build

# 3. 遵循 Conventional Commits 提交
git commit -m "feat(i18n): 添加日语语言支持"

# 4. 推送并开启 Pull Request
git push origin feature/AmazingFeature
```

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 📞 联系我们

- **技术支持**：<admin@0379.email>
- **问题反馈**：[GitHub Issues](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/issues)

---

## 🔗 相关链接

- [YYC³ AI Agent 官网](https://yyc3.com/ai-agent)
- [Next.js 文档](https://nextjs.org/docs)
- [React 文档](https://react.dev)
- [Tailwind CSS 文档](https://tailwindcss.com/docs)
- [shadcn/ui 文档](https://ui.shadcn.com)

---

## 📌 备注

1. **文档更新**：本文档与技术实况严格对齐（最近校准：2026-09-28），请关注最新版本。

2. **使用建议**：
   - 建议在项目初始化阶段就开始使用本指南
   - 定期进行代码审查，确保代码质量
   - 结合 CI 自动化工具使用，提高开发效率

3. **适用范围**：
   - 适用于 YYC³ 团队所有 AI 相关项目
   - 旧项目建议逐步迁移到本规范
   - 特殊项目可根据实际情况调整部分标准

4. **术语说明**：
   - **YYC³（YanYuCloudCube）言语云³**：团队与项目品牌，取「言启象限、语枢未来」之意——以语言为枢，启万物智能
   - **五高五标五化**：YYC³ 团队的核心理念，指导团队的技术和管理实践
   - **标准目录结构**：基于 Next.js 16 (App Router) 的推荐项目结构
   - **YYC³ 模板**：团队提供的标准化项目模板，包含所有必要的配置和依赖

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
