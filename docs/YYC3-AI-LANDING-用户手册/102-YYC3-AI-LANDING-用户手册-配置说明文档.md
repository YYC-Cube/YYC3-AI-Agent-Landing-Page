---
@file: 102-YYC3-AI-LANDING-用户手册-配置说明文档.md
@description: YYC3-AI-LANDING 项目配置的详细说明，包含配置项、配置示例、配置验证
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [用户手册],[配置说明],[配置指南]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 102-YYC3-AI-LANDING-用户手册

## 概述

本文档详细描述YYC3-AI-LANDING-用户手册-配置说明文档相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范配置说明文档相关的业务标准与技术落地要求
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

### 3. 配置说明文档

#### 3.1 环境变量配置

##### 3.1.1 应用配置

**公开环境变量**：

```env
# 应用基本信息
NEXT_PUBLIC_APP_NAME=YYC³ AI Landing
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_APP_DESCRIPTION=AI驱动的现代化落地页

# 国际化配置
NEXT_PUBLIC_DEFAULT_LOCALE=zh
NEXT_PUBLIC_SUPPORTED_LOCALES=zh,en
NEXT_PUBLIC_LOCALE_COOKIE_NAME=yyc3-locale

# SEO配置
NEXT_PUBLIC_SITE_NAME=YYC³ AI Landing
NEXT_PUBLIC_SITE_DESCRIPTION=AI驱动的现代化落地页
NEXT_PUBLIC_DEFAULT_IMAGE=/public/yyc3-article-cover-03.png
```

**配置说明**：

| 变量名 | 类型 | 必填 | 说明 | 示例值 |
|--------|------|------|------|----------|
| NEXT_PUBLIC_APP_NAME | string | 是 | 应用名称 | YYC³ AI Landing |
| NEXT_PUBLIC_APP_URL | string | 是 | 应用URL | http://localhost:3000 |
| NEXT_PUBLIC_DEFAULT_LOCALE | string | 是 | 默认语言 | zh |
| NEXT_PUBLIC_SUPPORTED_LOCALES | string | 是 | 支持的语言列表 | zh,en |

##### 3.1.2 API配置

**API相关配置**：

```env
# API配置
NEXT_PUBLIC_API_URL=http://localhost:3000/api
NEXT_PUBLIC_API_VERSION=v1
NEXT_PUBLIC_API_TIMEOUT=30000

# API密钥（仅服务端）
API_SECRET_KEY=your-secret-key-here
API_ENCRYPTION_KEY=your-encryption-key-here
```

**配置说明**：

| 变量名 | 类型 | 必填 | 说明 | 示例值 |
|--------|------|------|------|----------|
| NEXT_PUBLIC_API_URL | string | 是 | API基础URL | http://localhost:3000/api |
| NEXT_PUBLIC_API_VERSION | string | 否 | API版本 | v1 |
| NEXT_PUBLIC_API_TIMEOUT | number | 否 | 请求超时时间(ms) | 30000 |
| API_SECRET_KEY | string | 是 | API密钥（服务端） | your-secret-key |
| API_ENCRYPTION_KEY | string | 是 | 加密密钥（服务端） | your-encryption-key |

##### 3.1.3 第三方服务配置

**第三方服务集成**：

```env
# Google Analytics
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_GA_ENABLED=true

# Sentry
NEXT_PUBLIC_SENTRY_DSN=https://xxx@sentry.io/xxx
NEXT_PUBLIC_SENTRY_ENVIRONMENT=development
NEXT_PUBLIC_SENTRY_TRACES_SAMPLE_RATE=0.1

# Spline 3D场景
NEXT_PUBLIC_SPLINE_SCENE=https://prod.spline.design/xxx/scene.splinecode
NEXT_PUBLIC_SPLINE_ENABLED=true
NEXT_PUBLIC_SPLINE_LOADING_TIMEOUT=5000
```

**配置说明**：

| 变量名 | 类型 | 必填 | 说明 | 示例值 |
|--------|------|------|------|----------|
| NEXT_PUBLIC_GA_ID | string | 否 | Google Analytics ID | G-XXXXXXXXXX |
| NEXT_PUBLIC_SENTRY_DSN | string | 否 | Sentry DSN | https://xxx@sentry.io/xxx |
| NEXT_PUBLIC_SPLINE_SCENE | string | 否 | Spline场景URL | https://prod.spline.design/xxx/scene.splinecode |

#### 3.2 Next.js配置

##### 3.2.1 基础配置

**next.config.mjs配置**：

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // 输出配置
  output: 'standalone',
  
  // 实验性功能
  experimental: {
    optimizePackageImports: ['lucide-react', '@radix-ui/react-icons'],
  },
  
  // 图片优化
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    minimumCacheTTL: 60,
    dangerouslyAllowSVG: true,
  },
  
  // 编译器配置
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  
  // 头部配置
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-DNS-Prefetch-Control',
            value: 'on'
          },
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=63072000; includeSubDomains; preload'
          },
        ],
      },
    ]
  },
  
  // 重定向配置
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ]
  },
}

export default nextConfig
```

##### 3.2.2 TypeScript配置

**tsconfig.json配置**：

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
      "@/utils/*": ["./src/utils/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

#### 3.3 Tailwind CSS配置

##### 3.3.1 基础配置

**tailwind.config.ts配置**：

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: ['class'],
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
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['var(--font-sans)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
```

#### 3.4 ESLint配置

##### 3.4.1 基础配置

**.eslintrc.json配置**：

```json
{
  "extends": [
    "next/core-web-vitals",
    "prettier"
  ],
  "plugins": ["@typescript-eslint", "import"],
  "rules": {
    "no-console": ["warn", { "allow": ["warn", "error"] }],
    "prefer-const": "error",
    "no-var": "error",
    "@typescript-eslint/no-unused-vars": ["error", {
      "argsIgnorePattern": "^_",
      "varsIgnorePattern": "^_"
    }],
    "import/order": ["error", {
      "groups": ["builtin", "external", "internal", "parent", "sibling", "index"],
      "newlines-between": "always",
      "alphabetize": {
        "order": "asc",
        "caseInsensitive": true
      }
    }]
  }
}
```

##### 3.4.2 Prettier配置

**.prettierrc配置**：

```json
{
  "semi": false,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

#### 3.5 测试配置

##### 3.5.1 Vitest配置

**vitest.config.ts配置**：

```typescript
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'src/test/',
        '**/*.d.ts',
        '**/*.config.*',
      ],
      lines: 80,
      functions: 80,
      branches: 75,
      statements: 80,
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
```

##### 3.5.2 Playwright配置

**playwright.config.ts配置**：

```typescript
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results/results.json' }],
    ['junit', { outputFile: 'test-results/junit.xml' }],
  ],
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

#### 3.6 配置验证

##### 3.6.1 环境变量验证

**验证脚本**：

```typescript
// src/lib/env.ts
import { z } from 'zod'

const envSchema = z.object({
  // 公开变量
  NEXT_PUBLIC_APP_NAME: z.string().min(1),
  NEXT_PUBLIC_APP_URL: z.string().url(),
  NEXT_PUBLIC_DEFAULT_LOCALE: z.enum(['zh', 'en']),
  NEXT_PUBLIC_SUPPORTED_LOCALES: z.string(),
  
  // 私有变量
  API_SECRET_KEY: z.string().min(32),
  API_ENCRYPTION_KEY: z.string().length(32),
  
  // 可选变量
  NEXT_PUBLIC_GA_ID: z.string().optional(),
  NEXT_PUBLIC_SENTRY_DSN: z.string().url().optional(),
  NEXT_PUBLIC_SPLINE_SCENE: z.string().url().optional(),
})

export const env = envSchema.parse(process.env)
```

##### 3.6.2 配置检查命令

**package.json脚本**：

```json
{
  "scripts": {
    "config:check": "node scripts/check-config.js",
    "config:validate": "node scripts/validate-env.js"
  }
}
```

**验证脚本**：

```javascript
// scripts/check-config.js
const fs = require('fs')
const path = require('path')

const requiredFiles = [
  '.env.local',
  'next.config.mjs',
  'tsconfig.json',
  'tailwind.config.ts',
]

console.log('检查配置文件...')

requiredFiles.forEach(file => {
  const filePath = path.join(process.cwd(), file)
  if (fs.existsSync(filePath)) {
    console.log(`✅ ${file} 存在`)
  } else {
    console.error(`❌ ${file} 不存在`)
    process.exit(1)
  }
})

console.log('配置检查完成！')
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
