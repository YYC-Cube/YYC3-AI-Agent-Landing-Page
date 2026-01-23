# 🔖 YYC³ AI Agent Landing Page

![YYC³ AI Agent Landing Page](public/yyc3-article-cover-03.png)

> ***YanYuCloudCube***

> 言启象限 | 语枢未来

> ***Words Initiate Quadrants, Language Serves as Core for the Future***

> 万象归元于云枢 | 深栈智启新纪元

> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

![Next.js](https://img.shields.io/badge/Next.js-14.2.25-black?style=for-the-badge&logo=next.js)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.1.9-38B2AC?style=for-the-badge&logo=tailwind-css)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📋 项目概述

**YYC³(YanYuCloudCube) AI Agent Landing Page** 是一个现代化的 AI 代理服务落地页，采用 Next.js 16 构建，集成了国际化系统、3D 场景交互、动画效果和响应式设计。本项目旨在为 AI 代理服务提供专业、美观、高性能的展示平台，支持多语言切换，提供流畅的用户体验。

### 核心特性

- 🌍 **国际化支持** - 内置中英文双语系统，支持实时语言切换
- 🎨 **现代化 UI** - 基于 shadcn/ui 组件库，提供精美的视觉体验
- 🎬 **丰富动效** - 集成 Framer Motion、Spline 3D 场景、粒子动画等
- 📱 **响应式设计** - 完美适配桌面、平板、移动设备
- ⚡ **高性能** - 优化的加载速度和交互响应
- 🔒 **类型安全** - 完整的 TypeScript 类型定义

---

## 🚀 快速开始

### 环境要求

- Node.js >= 18.0.0
- pnpm >= 8.0.0（推荐）或 npm >= 9.0.0

### 安装依赖

```bash
# 使用 pnpm（推荐）
pnpm install

# 或使用 npm
npm install
```

### 启动开发服务器

```bash
# 使用 pnpm
pnpm dev

# 或使用 npm
npm run dev
```

访问 [http://localhost:3000](http://localhost:3000) 查看应用。

### 构建生产版本

```bash
# 使用 pnpm
pnpm build

# 或使用 npm
npm run build
```

### 启动生产服务器

```bash
# 使用 pnpm
pnpm start

# 或使用 npm
npm start
```

---

## 📚 技术栈

### 核心框架

| 技术 | 版本 | 用途 |
|------|------|------|
| Next.js | 16 | React 框架，支持 App Router |
| React | 19.2.0 | UI 库 |
| TypeScript | 5.1.6 | 类型安全 |
| Tailwind CSS | 4.1.9 | 原子化 CSS 框架 |

### UI 组件库

| 技术 | 版本 | 用途 |
|------|------|------|
| shadcn/ui | latest | 可复用组件系统 |
| Radix UI | latest | 无障碍 UI 原语 |
| Lucide Icons | 0.454.0 | 图标库 |

### 动画与交互

| 技术 | 版本 | 用途 |
|------|------|------|
| Framer Motion | 12.23.12 | 动画库 |
| @splinetool/react-spline | 4.1.0 | 3D 场景渲染 |
| @tsparticles/react | 3.0.0 | 粒子动画 |
| canvas-confetti | 1.9.3 | 庆祝动画 |

### 其他依赖

- **@vercel/analytics** - Vercel 分析
- **react-hook-form** - 表单管理
- **zod** - 数据验证
- **date-fns** - 日期处理
- **recharts** - 图表库

---

## 🎯 功能特性

### 1. 国际化系统 (i18n)

基于 React Context API 的轻量级国际化解决方案，支持：

- 客户端语言切换
- 状态持久化到 localStorage
- 类型安全的翻译字典
- 支持中文（默认）和英文

**使用示例：**

```tsx
import { useLocale } from '@/contexts/locale-context'

function Component() {
  const { t, locale, setLocale } = useLocale()
  return <h1>{t.hero.title}</h1>
}
```

### 2. 响应式布局

采用移动优先设计策略，支持以下断点：

- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px

### 3. 动画与交互

- **Spotlight 聚光灯效果** - 鼠标跟随的光晕效果
- **Sparkles 粒子动画** - 动态粒子背景
- **Spline 3D 场景** - 交互式 3D 元素
- **渐变背景动画** - 流畅的背景渐变
- **卡片悬浮交互** - 优雅的悬停效果

### 4. 核心页面

- **首页** - 产品展示和介绍
- **隐私政策** - 隐私政策说明
- **服务条款** - 服务条款说明

### 5. 组件系统

- **Navbar** - 响应式导航栏
- **Pricing** - 定价卡片展示
- **BentoGrid** - 服务展示网格
- **LanguageSwitcher** - 语言切换器
- **Spotlight** - 聚光灯效果
- **Sparkles** - 粒子动画
- **SplineScene** - 3D 场景

---

## 📁 项目结构

```
yyc3-ai-agent-landing-page/
├── app/                      # Next.js App Router
│   ├── layout.tsx            # 根布局
│   ├── page.tsx              # 首页
│   ├── globals.css           # 全局样式
│   ├── privacy/              # 隐私政策页
│   └── terms/                # 服务条款页
├── components/
│   ├── ui/                   # UI 组件
│   │   ├── navbar.tsx        # 导航栏
│   │   ├── pricing.tsx       # 定价组件
│   │   ├── bento-grid.tsx    # Bento 网格布局
│   │   ├── spotlight.tsx     # 聚光灯效果
│   │   ├── sparkles.tsx      # 粒子效果
│   │   ├── spline-scene.tsx  # 3D 场景
│   │   ├── language-switcher.tsx  # 语言切换器
│   │   └── ...               # 其他 shadcn 组件
│   └── theme-provider.tsx    # 主题提供者
├── contexts/
│   └── locale-context.tsx    # 语言上下文
├── lib/
│   ├── i18n.ts               # 国际化配置
│   └── utils.ts              # 工具函数
├── hooks/                    # 自定义 Hooks
│   └── use-media-query.ts    # 媒体查询 Hook
├── public/                   # 静态资源
│   ├── assets/               # 资源文件
│   └── yyc3-article-cover-03.png  # 封面图
├── docs/                     # 文档
│   ├── ARCHITECTURE.md       # 架构文档
│   ├── FEATURE_MATRIX.md     # 功能矩阵
│   └── ENTERPRISE_ROADMAP.md # 企业路线图
├── styles/                   # 样式文件
│   └── globals.css           # 全局样式
├── package.json              # 项目配置
├── tsconfig.json             # TypeScript 配置
├── next.config.mjs           # Next.js 配置
└── tailwind.config.ts        # Tailwind CSS 配置
```

---

## 🎨 样式与主题

项目使用 Tailwind CSS 进行样式管理，支持：

- 深色主题（默认）
- 自定义颜色系统
- 响应式工具类
- 动画和过渡效果

### 自定义主题配置

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        // 自定义颜色
      },
      animation: {
        // 自定义动画
      },
    },
  },
}
```

---

## 🔧 配置说明

### 环境变量

创建 `.env.local` 文件：

```env
# 分析
NEXT_PUBLIC_GA_ID=
VERCEL_ANALYTICS_ID=

# API（未来）
NEXT_PUBLIC_API_URL=
API_SECRET_KEY=
```

### TypeScript 配置

项目使用 TypeScript 严格模式，确保类型安全：

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    // 其他配置...
  }
}
```

---

## 📖 开发指南

### 代码风格

- 使用 TypeScript 严格模式
- 遵循 ESLint 规则
- 组件使用函数式写法
- 优先使用 Tailwind CSS

### 命名规范

- 组件：PascalCase（如：`UserProfile.tsx`）
- 文件：kebab-case（如：`user-service.ts`）
- 函数：camelCase（如：`getUserData`）
- 常量：UPPER_SNAKE_CASE（如：`API_BASE_URL`）

### Git 工作流

- 主分支：`main`
- 功能分支：`feature/功能名`
- 修复分支：`fix/问题描述`
- Commit 信息：使用 Conventional Commits 规范

**Commit 示例：**

```bash
feat(i18n): 添加日语语言支持

- 更新 i18n 配置文件
- 添加日语翻译字典
- 更新语言切换器组件

Closes #123
```

---

## 🧪 测试

项目支持以下测试框架：

- **Jest** - 单元测试
- **React Testing Library** - 组件测试
- **Playwright** - E2E 测试

### 运行测试

```bash
# 运行所有测试
pnpm test

# 运行测试并监听变化
pnpm test:watch

# 运行 E2E 测试
pnpm test:e2e
```

---

## 🚢 部署

### Vercel 部署（推荐）

1. 将代码推送到 GitHub
2. 在 Vercel 中导入项目
3. 配置环境变量
4. 部署完成

### 其他平台

项目支持部署到以下平台：

- **Vercel** - 推荐
- **Netlify**
- **AWS Amplify**
- **Docker**

### Docker 部署

```bash
# 构建镜像
docker build -t yyc3-ai-agent-landing-page .

# 运行容器
docker run -p 3000:3000 yyc3-ai-agent-landing-page
```

---

## 📊 性能优化

### 已实现的优化

- 代码分割和懒加载
- 图片优化（Next.js Image 组件）
- 字体优化
- CSS 优化
- 缓存策略

### 性能指标

- **LCP** (最大内容绘制) < 2.5s
- **FID** (首次输入延迟) < 100ms
- **CLS** (累积布局偏移) < 0.1

---

## 🔒 安全

- 无硬编码密钥或凭据
- 输入验证和清理
- 安全头配置
- CORS 配置
- 依赖安全扫描

---

## 📝 文档

- [架构文档](docs/ARCHITECTURE.md) - 详细的技术架构说明
- [功能矩阵](docs/FEATURE_MATRIX.md) - 功能对比和路线图
- [企业路线图](docs/ENTERPRISE_ROADMAP.md) - 企业级功能规划

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 贡献规范

- 遵循项目的代码风格
- 添加必要的测试
- 更新相关文档
- 确保所有测试通过

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 📞 联系我们

- **技术支持**：<admin@0379.email>
- **问题反馈**：[GitHub Issues](https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/issues)
- **文档更新**：<admin@0379.email>

---

## 🔗 相关链接

- [YYC³ AI Agent 官网](https://yyc3.com/ai-agent)
- [Next.js 文档](https://nextjs.org/docs)
- [React 文档](https://react.dev)
- [Tailwind CSS 文档](https://tailwindcss.com/docs)
- [shadcn/ui 文档](https://ui.shadcn.com)

---

## 🌟 致谢

感谢所有为这个项目做出贡献的开发者和设计师！

---

## 📌 备注

1. **文档更新**：本文档将定期更新以适应项目的发展，请关注最新版本。

2. **使用建议**：
   - 建议在项目初始化阶段就开始使用本指南
   - 定期进行代码审查，确保代码质量
   - 结合自动化工具使用，提高开发效率

3. **适用范围**：
   - 适用于 YYC³ 团队所有 AI 相关项目
   - 旧项目建议逐步迁移到本规范
   - 特殊项目可根据实际情况调整部分标准

4. **术语说明**：
   - **五高五标五化**：YYC³ 团队的核心理念，指导团队的技术和管理实践
   - **标准目录结构**：基于 Next.js 14+ (App Router) 的推荐项目结构
   - **YYC³ 模板**：团队提供的标准化项目模板，包含所有必要的配置和依赖

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
