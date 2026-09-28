---
@file: 091-YYC3-AI-LANDING-部署运维-CI/CD配置文档.md
@description: YYC3-AI-LANDING 持续集成和持续部署的配置文档，包含GitHub Actions、自动构建、自动部署
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [部署运维],[CI/CD],[自动化部署]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 091-YYC3-AI-LANDING-部署运维

## 概述

本文档详细描述YYC3-AI-LANDING-部署运维-CI/CD配置文档相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范CI/CD配置文档相关的业务标准与技术落地要求
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

### 3. CI/CD配置文档

#### 3.1 CI/CD架构

##### 3.1.1 持续集成流程

**CI流程图**：
```
开发者提交代码
    ↓
Git Push / Pull Request
    ↓
GitHub Actions触发
    ↓
代码检查 (Linting)
    ↓
类型检查 (TypeScript)
    ↓
单元测试 (Unit Tests)
    ↓
集成测试 (Integration Tests)
    ↓
构建 (Build)
    ↓
部署到Vercel
    ↓
通知结果
```

##### 3.1.2 持续部署流程

**CD流程图**：
```
构建成功
    ↓
检查目标分支
    ↓
┌─────────┬─────────┬─────────┐
│ main    │ develop │ PR      │
└────┬────┴────┬────┴────┬────┘
     │         │         │
     ↓         ↓         ↓
Production Staging  Preview
     │         │         │
     └─────────┴─────────┘
             ↓
      部署通知
```

#### 3.2 GitHub Actions配置

##### 3.2.1 工作流文件结构

**目录结构**：
```
.github/
└── workflows/
    ├── ci.yml              # 持续集成工作流
    ├── cd.yml              # 持续部署工作流
    ├── lint.yml            # 代码检查工作流
    ├── test.yml            # 测试工作流
    └── security.yml        # 安全扫描工作流
```

##### 3.2.2 CI工作流配置

**.github/workflows/ci.yml**：

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  NODE_VERSION: '18.x'

jobs:
  lint:
    name: Lint Code
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run ESLint
        run: npm run lint
      
      - name: Run Prettier check
        run: npm run format:check

  type-check:
    name: TypeScript Type Check
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run TypeScript check
        run: npm run type-check

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit
      
      - name: Run integration tests
        run: npm run test:integration
      
      - name: Upload coverage reports
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          name: codecov-umbrella

  build:
    name: Build Application
    runs-on: ubuntu-latest
    needs: [lint, type-check, test]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build application
        run: npm run build
        env:
          NODE_ENV: production
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-output
          path: .next/
          retention-days: 7
```

##### 3.2.3 CD工作流配置

**.github/workflows/cd.yml**：

```yaml
name: CD

on:
  push:
    branches: [main, develop]
  workflow_dispatch:

env:
  NODE_VERSION: '18.x'
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}

jobs:
  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install Vercel CLI
        run: npm install --global vercel@latest
      
      - name: Pull Vercel Environment Information
        run: vercel pull --yes --environment=production --token=${{ secrets.VERCEL_TOKEN }}
      
      - name: Build Project Artifacts
        run: vercel build --prod --token=${{ secrets.VERCEL_TOKEN }}
      
      - name: Deploy to Vercel
        id: deploy
        run: |
          url=$(vercel deploy --prebuilt --prod --token=${{ secrets.VERCEL_TOKEN }})
          echo "url=$url" >> $GITHUB_OUTPUT
      
      - name: Comment deployment URL
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🚀 Production deployment successful!\n\nURL: ${{ steps.deploy.outputs.url }}'
            })

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop' && github.event_name == 'push'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install Vercel CLI
        run: npm install --global vercel@latest
      
      - name: Pull Vercel Environment Information
        run: vercel pull --yes --environment=preview --token=${{ secrets.VERCEL_TOKEN }}
      
      - name: Build Project Artifacts
        run: vercel build --token=${{ secrets.VERCEL_TOKEN }}
      
      - name: Deploy to Vercel
        id: deploy
        run: |
          url=$(vercel deploy --prebuilt --token=${{ secrets.VERCEL_TOKEN }})
          echo "url=$url" >> $GITHUB_OUTPUT
      
      - name: Notify deployment
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Staging deployment completed'
          webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
        if: always()
```

##### 3.2.4 代码检查工作流

**.github/workflows/lint.yml**：

```yaml
name: Lint

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  eslint:
    name: ESLint
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run ESLint
        run: npm run lint
      
      - name: Annotate code with ESLint results
        if: always()
        uses: reviewdog/action-eslint@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          reporter: github-pr-review
          eslint_flags: 'src/'

  prettier:
    name: Prettier
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run Prettier
        run: npm run format:check
      
      - name: Prettier check
        uses: creyD/prettier_action@v4.3
        with:
          prettier_options: '--check src/'
          only_changed: true
```

##### 3.2.5 测试工作流

**.github/workflows/test.yml**：

```yaml
name: Test

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit -- --coverage
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unit
          name: unit-coverage

  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run integration tests
        run: npm run test:integration
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: integration
          name: integration-coverage

  e2e-tests:
    name: E2E Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright
        run: npx playwright install --with-deps
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/
```

##### 3.2.6 安全扫描工作流

**.github/workflows/security.yml**：

```yaml
name: Security

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
  schedule:
    - cron: '0 0 * * 0'

jobs:
  dependency-review:
    name: Dependency Review
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Dependency Review
        uses: actions/dependency-review-action@v3

  codeql:
    name: CodeQL Analysis
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: javascript, typescript
      
      - name: Autobuild
        uses: github/codeql-action/autobuild@v2
      
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2

  npm-audit:
    name: NPM Audit
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run npm audit
        run: npm audit --audit-level=high
```

#### 3.3 Secrets配置

##### 3.3.1 GitHub Secrets

**必需的Secrets**：

| Secret名称 | 说明 | 获取方式 |
|-----------|------|----------|
| VERCEL_TOKEN | Vercel API Token | Vercel Dashboard → Settings → Tokens |
| VERCEL_ORG_ID | Vercel Organization ID | vercel link后查看.vercel/project.json |
| VERCEL_PROJECT_ID | Vercel Project ID | vercel link后查看.vercel/project.json |
| SLACK_WEBHOOK_URL | Slack Webhook URL | Slack App设置 |
| GITHUB_TOKEN | GitHub Token | 自动提供 |
| CODECOV_TOKEN | Codecov Token | Codecov Dashboard |

**配置步骤**：

```bash
# 1. 生成Vercel Token
# 访问 https://vercel.com/account/tokens
# 点击 "Create Token"
# 设置名称和权限
# 复制生成的token

# 2. 获取Vercel Org ID和Project ID
vercel link
cat .vercel/project.json

# 3. 在GitHub中配置Secrets
# 进入仓库 → Settings → Secrets and variables → Actions
# 点击 "New repository secret"
# 添加上述所有secrets
```

##### 3.3.2 Vercel环境变量

**生产环境变量**：

| 变量名 | 值 | 说明 |
|--------|-----|------|
| NODE_ENV | production | 运行环境 |
| NEXT_PUBLIC_APP_URL | https://yyc3-ai-landing.vercel.app | 应用URL |
| NEXT_PUBLIC_DEFAULT_LOCALE | zh | 默认语言 |
| NEXT_PUBLIC_GA_ID | G-XXXXXXXXXX | Google Analytics ID |
| NEXT_PUBLIC_SENTRY_DSN | https://xxx@sentry.io/xxx | Sentry DSN |

**预览环境变量**：

| 变量名 | 值 | 说明 |
|--------|-----|------|
| NODE_ENV | development | 运行环境 |
| NEXT_PUBLIC_APP_URL | https://yyc3-ai-landing-pr-xxx.vercel.app | 应用URL |
| NEXT_PUBLIC_DEFAULT_LOCALE | zh | 默认语言 |

#### 3.4 通知配置

##### 3.4.1 Slack通知

**配置步骤**：

```bash
# 1. 创建Slack App
# 访问 https://api.slack.com/apps
# 点击 "Create New App"
# 配置Incoming Webhooks
# 复制Webhook URL

# 2. 添加到GitHub Secrets
# SLACK_WEBHOOK_URL = https://hooks.slack.com/services/XXX/XXX/XXX
```

**通知模板**：

```yaml
- name: Notify Slack on success
  if: success()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: '✅ Deployment successful!'
    webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}

- name: Notify Slack on failure
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: '❌ Deployment failed!'
    webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
```

##### 3.4.2 Email通知

**配置步骤**：

```yaml
- name: Send email notification
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: 'Deployment Failed - ${{ github.repository }}'
    to: ${{ secrets.NOTIFICATION_EMAIL }}
    from: GitHub Actions
    body: |
      Repository: ${{ github.repository }}
      Branch: ${{ github.ref }}
      Commit: ${{ github.sha }}
      Author: ${{ github.actor }}
      Workflow: ${{ github.workflow }}
      Run URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

#### 3.5 性能优化

##### 3.5.1 缓存策略

**依赖缓存**：

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '18.x'
    cache: 'npm'
```

**构建缓存**：

```yaml
- name: Cache build
  uses: actions/cache@v3
  with:
    path: |
      .next/cache
      node_modules/.cache
    key: ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-nextjs-
```

##### 3.5.2 并行执行

**并行任务配置**：

```yaml
jobs:
  lint:
    # ... lint job
  
  type-check:
    # ... type-check job
  
  test:
    needs: [lint, type-check]
    # ... test job
  
  build:
    needs: [test]
    # ... build job
```

#### 3.6 质量门禁

##### 3.6.1 代码覆盖率要求

**覆盖率阈值**：

| 类型 | 阈值 | 说明 |
|------|------|------|
| 语句覆盖率 | ≥ 80% | 代码语句覆盖 |
| 分支覆盖率 | ≥ 75% | 条件分支覆盖 |
| 函数覆盖率 | ≥ 80% | 函数定义覆盖 |
| 行覆盖率 | ≥ 80% | 代码行覆盖 |

**配置示例**：

```javascript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      lines: 80,
      functions: 80,
      branches: 75,
      statements: 80,
    },
  },
})
```

##### 3.6.2 代码质量检查

**ESLint规则**：

```javascript
// .eslintrc.js
module.exports = {
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'error',
    'prefer-const': 'error',
    'no-var': 'error',
    'eqeqeq': 'error',
    'curly': 'error',
  },
}
```

**Prettier配置**：

```javascript
// .prettierrc
module.exports = {
  semi: true,
  trailingComma: 'es5',
  singleQuote: true,
  printWidth: 100,
  tabWidth: 2,
  useTabs: false,
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
