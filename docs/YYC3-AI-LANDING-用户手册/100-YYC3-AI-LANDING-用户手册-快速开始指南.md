---
@file: 100-YYC3-AI-LANDING-用户手册-快速开始指南.md
@description: YYC3-AI-LANDING 项目的快速开始指南，包含安装、配置、启动的详细步骤
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [用户手册],[快速开始],[入门指南]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 100-YYC3-AI-LANDING-用户手册

## 概述

本文档详细描述YYC3-AI-LANDING-用户手册-快速开始指南相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范快速开始指南相关的业务标准与技术落地要求
- 为项目相关人员提供清晰的参考依据
- 保障相关模块开发、实施、运维的一致性与规范性

### 2. 设计原则

#### 2.1 五高原则
- **高可用性**：确保系统7x24小时稳定运行
- **高性能**：优化加载速度和交互响应
- **高安全性**：保护用户数据和隐私安全
- **高扩展性**：支持业务快速扩展
- **高可维护性**：便于后续维护和升级

#### 2.2 五标体系
- **标准化**：统一的技术和流程标准
- **规范化**：严格的开发和管理规范
- **自动化**：提高开发效率和质量
- **智能化**：利用AI技术提升能力
- **可视化**：直观的监控和管理界面

#### 2.3 五化架构
- **流程化**：标准化的开发流程
- **文档化**：完善的文档体系
- **工具化**：高效的开发工具链
- **数字化**：数据驱动的决策
- **生态化**：开放的生态系统

### 3. 快速开始指南

#### 3.1 环境要求

##### 3.1.1 系统要求

**开发环境**：
- Node.js: 18.x 或更高版本
- npm: 9.x 或更高版本（或 yarn 1.22+）
- Git: 2.x 或更高版本
- 操作系统: macOS, Linux, Windows (WSL2)

**推荐配置**：
- CPU: 4核心或更高
- 内存: 8GB或更高
- 硬盘: 20GB可用空间

##### 3.1.2 浏览器要求

**支持的浏览器**：
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

#### 3.2 安装步骤

##### 3.2.1 克隆项目

```bash
# 克隆仓库
git clone https://github.com/YYC3/yyc3-ai-landing-page.git

# 进入项目目录
cd yyc3-ai-landing-page

# 查看分支
git branch -a

# 切换到开发分支
git checkout develop
```

##### 3.2.2 安装依赖

```bash
# 使用npm安装
npm install

# 或使用yarn安装
yarn install

# 或使用pnpm安装（推荐）
pnpm install
```

**依赖安装说明**：
- 安装过程可能需要几分钟
- 首次安装会自动下载Playwright浏览器
- 如遇网络问题，可配置npm镜像源

**配置npm镜像源**：

```bash
# 使用淘宝镜像
npm config set registry https://registry.npmmirror.com

# 或使用华为镜像
npm config set registry https://mirrors.huaweicloud.com/repository/npm/
```

##### 3.2.3 环境变量配置

```bash
# 复制环境变量模板
cp .env.example .env.local

# 编辑环境变量
vim .env.local
```

**环境变量说明**：

```env
# 应用配置
NEXT_PUBLIC_APP_NAME=YYC³ AI Landing
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_DEFAULT_LOCALE=zh
NEXT_PUBLIC_SUPPORTED_LOCALES=zh,en

# API配置
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# 第三方服务
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_SENTRY_DSN=https://xxx@sentry.io/xxx

# Spline 3D场景
NEXT_PUBLIC_SPLINE_SCENE=https://prod.spline.design/xxx/scene.splinecode
```

#### 3.3 启动项目

##### 3.3.1 开发模式启动

```bash
# 启动开发服务器
npm run dev

# 或使用yarn
yarn dev

# 或使用pnpm
pnpm dev
```

**访问应用**：
- 本地访问: http://localhost:3000
- 默认端口: 3000
- 热重载: 自动

##### 3.3.2 生产模式构建

```bash
# 构建生产版本
npm run build

# 启动生产服务器
npm run start
```

**构建输出**：
- 输出目录: `.next/`
- 静态资源: `public/`
- 构建时间: 约2-5分钟

#### 3.4 开发工具配置

##### 3.4.1 VS Code配置

**推荐插件**：
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- TypeScript Vue Plugin (Volar)
- Auto Rename Tag
- Path Intellisense

**工作区设置**：

```json
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.tsdk": "node_modules/typescript/lib",
  "typescript.enablePromptUseWorkspaceTsdk": true
}
```

##### 3.4.2 Git配置

**提交前检查**：

```bash
# 安装husky
npm install -D husky

# 初始化husky
npx husky install

# 添加pre-commit钩子
npx husky add .husky/pre-commit "npm run lint && npm run type-check"
```

#### 3.5 常见问题

##### 3.5.1 依赖安装失败

**问题**：npm install失败

**解决方案**：

```bash
# 清除npm缓存
npm cache clean --force

# 删除node_modules
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

##### 3.5.2 端口被占用

**问题**：3000端口已被占用

**解决方案**：

```bash
# 查找占用端口的进程
lsof -i :3000

# 或使用netstat
netstat -ano | findstr :3000

# 杀死进程
kill -9 <PID>

# 或使用其他端口
PORT=3001 npm run dev
```

##### 3.5.3 TypeScript类型错误

**问题**：类型检查失败

**解决方案**：

```bash
# 重新生成类型
npm run type-check

# 清除.next缓存
rm -rf .next

# 重新构建
npm run build
```

#### 3.6 下一步

**推荐阅读**：
- [功能使用手册](./101-YYC3-AI-LANDING-用户手册-功能使用手册.md)
- [配置说明文档](./102-YYC3-AI-LANDING-用户手册-配置说明文档.md)
- [常见问题解答](./103-YYC3-AI-LANDING-用户手册-常见问题解答.md)

**学习资源**：
- Next.js官方文档: https://nextjs.org/docs
- Tailwind CSS文档: https://tailwindcss.com/docs
- shadcn/ui文档: https://ui.shadcn.com

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
