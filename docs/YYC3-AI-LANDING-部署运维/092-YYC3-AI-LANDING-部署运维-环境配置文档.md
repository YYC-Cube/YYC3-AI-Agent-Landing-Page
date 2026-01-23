---
@file: 092-YYC3-AI-LANDING-部署运维-环境配置文档.md
@description: YYC3-AI-LANDING 开发、测试、生产环境的配置文档，包含环境变量、配置文件、配置管理
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [部署运维],[环境配置],[配置管理]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 092-YYC3-AI-LANDING-部署运维

## 概述

本文档详细描述YYC3-AI-LANDING-部署运维-环境配置文档相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范环境配置文档相关的业务标准与技术落地要求
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

### 3. 环境配置文档

#### 3.1 环境划分

##### 3.1.1 环境类型

**环境定义**：

| 环境 | 用途 | 域名 | 分支 | 数据库 | 缓存 | 说明 |
|------|------|------|------|--------|------|------|
| Development | 本地开发 | localhost:3000 | local | memory | 开发者本地环境，支持热重载 |
| Staging | 预发布 | yyc3-ai-landing-staging.vercel.app | develop | staging | 生产环境前的最后测试 |
| Production | 生产环境 | yyc3-ai-landing.vercel.app | main | production | 正式对外提供服务 |

##### 3.1.2 环境差异

**开发环境特性**：
- 启用详细日志
- 禁用生产优化
- 启用Source Maps
- 启用错误堆栈
- 禁用缓存

**预发布环境特性**：
- 接近生产配置
- 启用性能监控
- 启用错误追踪
- 使用测试数据

**生产环境特性**：
- 完全优化构建
- 启用CDN缓存
- 启用Gzip压缩
- 禁用Source Maps
- 启用HTTPS强制

#### 3.2 环境变量配置

##### 3.2.1 环境变量分类

**公开环境变量（NEXT_PUBLIC_）**：

| 变量名 | 开发环境 | 预发布环境 | 生产环境 | 说明 |
|--------|----------|------------|----------|------|
| NEXT_PUBLIC_APP_NAME | YYC³ AI Landing (Dev) | YYC³ AI Landing (Staging) | YYC³ AI Landing | 应用名称 |
| NEXT_PUBLIC_APP_URL | http://localhost:3000 | https://yyc3-ai-landing-staging.vercel.app | https://yyc3-ai-landing.vercel.app | 应用URL |
| NEXT_PUBLIC_DEFAULT_LOCALE | zh | zh | zh | 默认语言 |
| NEXT_PUBLIC_SUPPORTED_LOCALES | zh,en | zh,en | zh,en | 支持语言列表 |
| NEXT_PUBLIC_GA_ID | - | G-XXXXXXXXXX | G-XXXXXXXXXX | Google Analytics ID |
| NEXT_PUBLIC_SENTRY_DSN | - | https://xxx@sentry.io/xxx | https://xxx@sentry.io/xxx | Sentry DSN |
| NEXT_PUBLIC_SPLINE_SCENE | https://prod.spline.design/xxx/scene.splinecode | https://prod.spline.design/xxx/scene.splinecode | https://prod.spline.design/xxx/scene.splinecode | Spline场景URL |

**私有环境变量**：

| 变量名 | 开发环境 | 预发布环境 | 生产环境 | 说明 |
|--------|----------|------------|----------|------|
| NODE_ENV | development | production | production | Node.js环境 |
| DATABASE_URL | mongodb://localhost:27017/yyc3-dev | mongodb://staging-db:27017/yyc3-staging | mongodb://prod-db:27017/yyc3-prod | 数据库连接 |
| REDIS_URL | redis://localhost:6379 | redis://staging-redis:6379 | redis://prod-redis:6379 | Redis连接 |
| API_SECRET_KEY | dev-secret-key | staging-secret-key | prod-secret-key | API密钥 |
| JWT_SECRET | dev-jwt-secret | staging-jwt-secret | prod-jwt-secret | JWT密钥 |
| ENCRYPTION_KEY | dev-encryption-key | staging-encryption-key | prod-encryption-key | 加密密钥 |

##### 3.2.2 环境变量文件

**.env.local（开发环境）**：

```bash
# 应用配置
NODE_ENV=development
NEXT_PUBLIC_APP_NAME=YYC³ AI Landing (Dev)
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_DEFAULT_LOCALE=zh
NEXT_PUBLIC_SUPPORTED_LOCALES=zh,en

# 3D场景
NEXT_PUBLIC_SPLINE_SCENE=https://prod.spline.design/UbM7F-HZcyTbZ4y3/scene.splinecode

# 数据库
DATABASE_URL=mongodb://localhost:27017/yyc3-dev
REDIS_URL=redis://localhost:6379

# 安全配置
API_SECRET_KEY=dev-secret-key-change-in-production
JWT_SECRET=dev-jwt-secret-change-in-production
ENCRYPTION_KEY=dev-encryption-key-change-in-production

# 开发工具
NEXT_PUBLIC_ENABLE_DEBUG=true
NEXT_PUBLIC_ENABLE_SOURCE_MAPS=true
```

**.env.production（生产环境）**：

```bash
# 应用配置
NODE_ENV=production
NEXT_PUBLIC_APP_NAME=YYC³ AI Landing
NEXT_PUBLIC_APP_URL=https://yyc3-ai-landing.vercel.app
NEXT_PUBLIC_DEFAULT_LOCALE=zh
NEXT_PUBLIC_SUPPORTED_LOCALES=zh,en

# 3D场景
NEXT_PUBLIC_SPLINE_SCENE=https://prod.spline.design/UbM7F-HZcyTbZ4y3/scene.splinecode

# 分析和监控
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_SENTRY_DSN=https://xxx@sentry.io/xxx

# 数据库
DATABASE_URL=mongodb://prod-db:27017/yyc3-prod
REDIS_URL=redis://prod-redis:6379

# 安全配置
API_SECRET_KEY=${{ secrets.API_SECRET_KEY }}
JWT_SECRET=${{ secrets.JWT_SECRET }}
ENCRYPTION_KEY=${{ secrets.ENCRYPTION_KEY }}

# 生产优化
NEXT_PUBLIC_ENABLE_DEBUG=false
NEXT_PUBLIC_ENABLE_SOURCE_MAPS=false
```

**.env.staging（预发布环境）**：

```bash
# 应用配置
NODE_ENV=production
NEXT_PUBLIC_APP_NAME=YYC³ AI Landing (Staging)
NEXT_PUBLIC_APP_URL=https://yyc3-ai-landing-staging.vercel.app
NEXT_PUBLIC_DEFAULT_LOCALE=zh
NEXT_PUBLIC_SUPPORTED_LOCALES=zh,en

# 3D场景
NEXT_PUBLIC_SPLINE_SCENE=https://prod.spline.design/UbM7F-HZcyTbZ4y3/scene.splinecode

# 分析和监控
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_SENTRY_DSN=https://xxx@sentry.io/xxx

# 数据库
DATABASE_URL=mongodb://staging-db:27017/yyc3-staging
REDIS_URL=redis://staging-redis:6379

# 安全配置
API_SECRET_KEY=${{ secrets.STAGING_API_SECRET_KEY }}
JWT_SECRET=${{ secrets.STAGING_JWT_SECRET }}
ENCRYPTION_KEY=${{ secrets.STAGING_ENCRYPTION_KEY }}

# 预发布配置
NEXT_PUBLIC_ENABLE_DEBUG=false
NEXT_PUBLIC_ENABLE_SOURCE_MAPS=false
```

#### 3.3 配置文件管理

##### 3.3.1 Next.js配置

**next.config.mjs**：

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // 环境检测
  env: {
    APP_ENV: process.env.NODE_ENV,
  },
  
  // 编译优化
  swcMinify: true,
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  
  // 图片优化
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'prod.spline.design',
        pathname: '/**',
      },
    ],
  },
  
  // 压缩
  compress: true,
  
  // 输出模式
  output: 'standalone',
  
  // 实验性功能
  experimental: {
    optimizeCss: true,
    optimizePackageImports: ['lucide-react', '@radix-ui/react-icons'],
  },
  
  // 生产环境优化
  productionBrowserSourceMaps: false,
  
  // 开发环境配置
  onDemandEntries: {
    maxInactiveAge: 25 * 1000,
    pagesBufferLength: 2,
  },
}

module.exports = nextConfig
```

##### 3.3.2 TypeScript配置

**tsconfig.json**：

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/hooks/*": ["./src/hooks/*"],
      "@/types/*": ["./src/types/*"],
      "@/utils/*": ["./src/utils/*"],
      "@/styles/*": ["./src/styles/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

##### 3.3.3 Tailwind CSS配置

**tailwind.config.ts**：

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
```

#### 3.4 开发环境配置

##### 3.4.1 本地开发设置

**安装依赖**：

```bash
# 安装Node.js依赖
npm install

# 或使用yarn
yarn install

# 或使用pnpm
pnpm install
```

**启动开发服务器**：

```bash
# 启动开发服务器
npm run dev

# 或使用yarn
yarn dev

# 或使用pnpm
pnpm dev
```

**开发服务器配置**：

```javascript
// package.json
{
  "scripts": {
    "dev": "next dev",
    "dev:turbo": "next dev --turbo",
    "dev:debug": "NODE_OPTIONS='--inspect' next dev"
  }
}
```

##### 3.4.2 开发工具配置

**ESLint配置**：

```javascript
// .eslintrc.js
module.exports = {
  extends: ['next/core-web-vitals', 'prettier'],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'warn',
    'no-unused-vars': 'error',
    'prefer-const': 'error',
    'no-var': 'error',
  },
  ignorePatterns: ['node_modules/', '.next/', 'out/'],
}
```

**Prettier配置**：

```javascript
// .prettierrc.js
module.exports = {
  semi: true,
  trailingComma: 'es5',
  singleQuote: true,
  printWidth: 100,
  tabWidth: 2,
  useTabs: false,
  arrowParens: 'always',
  endOfLine: 'lf',
}
```

**.prettierignore**：

```
node_modules
.next
out
coverage
dist
build
*.min.js
*.min.css
package-lock.json
yarn.lock
pnpm-lock.yaml
```

#### 3.5 生产环境配置

##### 3.5.1 构建优化

**构建脚本**：

```json
{
  "scripts": {
    "build": "next build",
    "build:analyze": "ANALYZE=true next build",
    "build:profile": "next build --profile"
  }
}
```

**构建分析**：

```javascript
// next.config.mjs
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer(nextConfig)
```

##### 3.5.2 性能优化

**图片优化配置**：

```javascript
// next.config.mjs
images: {
  formats: ['image/avif', 'image/webp'],
  deviceSizes: [640, 750, 828, 1080, 1200, 1920],
  imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  minimumCacheTTL: 60,
  dangerouslyAllowSVG: true,
  contentDispositionType: 'attachment',
  contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
}
```

**缓存策略**：

```javascript
// next.config.mjs
headers: async () => {
  return [
    {
      source: '/:all*(svg|jpg|png|webp|avif)',
      locale: false,
      headers: [
        {
          key: 'Cache-Control',
          value: 'public, max-age=31536000, immutable',
        },
      ],
    },
    {
      source: '/api/:path*',
      headers: [
        {
          key: 'Cache-Control',
          value: 'public, max-age=60, s-maxage=60',
        },
      ],
    },
  ]
}
```

#### 3.6 环境变量管理

##### 3.6.1 安全最佳实践

**环境变量安全原则**：

1. **永远不要提交敏感信息到Git**
   - 使用.gitignore排除.env文件
   - 使用环境变量管理工具

2. **使用不同的密钥**
   - 每个环境使用不同的密钥
   - 定期轮换密钥

3. **最小权限原则**
   - 只授予必要的权限
   - 使用短期有效的令牌

4. **加密存储**
   - 使用加密工具存储敏感信息
   - 使用密钥管理服务

##### 3.6.2 环境变量验证

**验证脚本**：

```typescript
// scripts/validate-env.ts
import dotenv from 'dotenv'

dotenv.config()

const requiredEnvVars = {
  development: [
    'NODE_ENV',
    'NEXT_PUBLIC_APP_NAME',
    'NEXT_PUBLIC_APP_URL',
  ],
  production: [
    'NODE_ENV',
    'DATABASE_URL',
    'REDIS_URL',
    'API_SECRET_KEY',
    'JWT_SECRET',
  ],
}

const env = process.env.NODE_ENV || 'development'
const required = requiredEnvVars[env as keyof typeof requiredEnvVars] || []

const missing = required.filter((key) => !env[key])

if (missing.length > 0) {
  console.error(`Missing required environment variables: ${missing.join(', ')}`)
  process.exit(1)
}

console.log('✅ All required environment variables are set')
```

**使用验证脚本**：

```bash
# 在package.json中添加
{
  "scripts": {
    "validate-env": "ts-node scripts/validate-env.ts",
    "prebuild": "npm run validate-env",
    "predev": "npm run validate-env"
  }
}
```

##### 3.6.3 环境变量加载

**加载顺序**：

```
1. 系统环境变量
2. .env.local (最高优先级)
3. .env.development / .env.production
4. .env (默认配置)
```

**加载示例**：

```typescript
// lib/config.ts
export const config = {
  app: {
    name: process.env.NEXT_PUBLIC_APP_NAME || 'YYC³ AI Landing',
    url: process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:3000',
    defaultLocale: process.env.NEXT_PUBLIC_DEFAULT_LOCALE || 'zh',
    supportedLocales: (process.env.NEXT_PUBLIC_SUPPORTED_LOCALES || 'zh,en').split(','),
  },
  api: {
    secretKey: process.env.API_SECRET_KEY || '',
    jwtSecret: process.env.JWT_SECRET || '',
  },
  database: {
    url: process.env.DATABASE_URL || '',
  },
  redis: {
    url: process.env.REDIS_URL || '',
  },
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
