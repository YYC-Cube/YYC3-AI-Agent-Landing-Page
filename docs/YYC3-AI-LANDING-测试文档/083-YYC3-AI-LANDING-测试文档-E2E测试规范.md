---
@file: 083-YYC3-AI-LANDING-测试文档-E2E测试规范.md
@description: YYC3-AI-LANDING 端到端测试的编写规范、测试流程设计、自动化实现
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [测试文档],[E2E测试],[测试规范]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 083-YYC3-AI-LANDING-测试文档

## 概述

本文档详细描述YYC3-AI-LANDING-测试文档-E2E测试规范相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范E2E测试规范相关的业务标准与技术落地要求
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

### 3. E2E测试规范

#### 3.1 E2E测试概述

##### 3.1.1 测试目标

**E2E测试目的**：
- 验证完整的用户流程
- 测试跨页面的交互
- 验证关键业务场景
- 确保端到端的用户体验

**测试范围**：
- 用户注册和登录流程
- 服务浏览和选择流程
- 联系表单提交流程
- 语言切换流程
- 响应式布局测试

##### 3.1.2 测试框架选择

**Playwright配置**：

```bash
npm install -D @playwright/test
npx playwright install
```

**配置文件**：

```typescript
// playwright.config.ts
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
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

#### 3.2 E2E测试用例

##### 3.2.1 首页测试

**首页加载测试**：

```typescript
// e2e/home.spec.ts
import { test, expect } from '@playwright/test'

test.describe('首页', () => {
  test('应该正确加载首页', async ({ page }) => {
    await page.goto('/')
    
    await expect(page).toHaveTitle(/YYC³ AI Landing/)
    await expect(page.locator('h1')).toContainText('AI 驱动业绩增长')
  })

  test('应该显示所有主要部分', async ({ page }) => {
    await page.goto('/')
    
    await expect(page.getByText('服务')).toBeVisible()
    await expect(page.getByText('定价')).toBeVisible()
    await expect(page.getByText('联系我们')).toBeVisible()
  })

  test('应该支持语言切换', async ({ page }) => {
    await page.goto('/')
    
    const languageSwitcher = page.getByRole('combobox')
    await languageSwitcher.selectOption('en')
    
    await expect(page.getByText('Services')).toBeVisible()
  })

  test('应该响应CTA按钮点击', async ({ page }) => {
    await page.goto('/')
    
    const ctaButton = page.getByRole('button', { name: /预约免费咨询/ })
    await ctaButton.click()
    
    await expect(page).toHaveURL(/#contact/)
  })
})
```

##### 3.2.2 服务页面测试

**服务浏览测试**：

```typescript
// e2e/services.spec.ts
import { test, expect } from '@playwright/test'

test.describe('服务页面', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/services')
  })

  test('应该显示所有服务', async ({ page }) => {
    const services = page.getByRole('article')
    await expect(services.first()).toBeVisible()
  })

  test('应该支持服务筛选', async ({ page }) => {
    const filterButton = page.getByRole('button', { name: '聊天机器人' })
    await filterButton.click()
    
    const services = page.getByRole('article')
    const count = await services.count()
    expect(count).toBeGreaterThan(0)
  })

  test('应该显示服务详情', async ({ page }) => {
    const firstService = page.getByRole('article').first()
    await firstService.click()
    
    await expect(page).toHaveURL(/\/services\/.+/)
    await expect(page.getByText('服务详情')).toBeVisible()
  })
})
```

##### 3.2.3 联系表单测试

**表单提交测试**：

```typescript
// e2e/contact.spec.ts
import { test, expect } from '@playwright/test'

test.describe('联系表单', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/#contact')
  })

  test('应该显示联系表单', async ({ page }) => {
    await expect(page.getByPlaceholder('您的姓名')).toBeVisible()
    await expect(page.getByPlaceholder('您的邮箱')).toBeVisible()
    await expect(page.getByPlaceholder('请输入您的消息')).toBeVisible()
  })

  test('应该验证必填字段', async ({ page }) => {
    const submitButton = page.getByRole('button', { name: '发送消息' })
    await submitButton.click()
    
    await expect(page.getByText('请填写所有必填字段')).toBeVisible()
  })

  test('应该成功提交表单', async ({ page }) => {
    await page.getByPlaceholder('您的姓名').fill('测试用户')
    await page.getByPlaceholder('您的邮箱').fill('test@example.com')
    await page.getByPlaceholder('请输入您的消息').fill('这是一条测试消息')
    
    const submitButton = page.getByRole('button', { name: '发送消息' })
    await submitButton.click()
    
    await expect(page.getByText('消息已发送')).toBeVisible()
  })
})
```

##### 3.2.4 定价页面测试

**定价计划测试**：

```typescript
// e2e/pricing.spec.ts
import { test, expect } from '@playwright/test'

test.describe('定价页面', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/pricing')
  })

  test('应该显示所有定价计划', async ({ page }) => {
    await expect(page.getByText('Starter')).toBeVisible()
    await expect(page.getByText('Professional')).toBeVisible()
    await expect(page.getByText('Enterprise')).toBeVisible()
  })

  test('应该支持年付/月付切换', async ({ page }) => {
    const toggle = page.getByRole('switch')
    await toggle.click()
    
    const prices = page.locator('.price')
    const firstPrice = await prices.first().textContent()
    expect(firstPrice).toMatch(/\$\d+/)
  })

  test('应该支持计划选择', async ({ page }) => {
    const selectButton = page.getByRole('button', { name: '选择计划' }).first()
    await selectButton.click()
    
    await expect(page.getByText('计划已选择')).toBeVisible()
  })
})
```

#### 3.3 响应式测试

##### 3.3.1 移动端测试

**移动设备测试**：

```typescript
// e2e/responsive.spec.ts
import { test, expect, devices } from '@playwright/test'

test.describe('响应式设计', () => {
  test('应该在移动设备上正确显示', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 })
    await page.goto('/')
    
    await expect(page.getByRole('navigation')).not.toBeVisible()
    
    const menuButton = page.getByRole('button', { name: '菜单' })
    await menuButton.click()
    await expect(page.getByRole('navigation')).toBeVisible()
  })

  test('应该在平板设备上正确显示', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 })
    await page.goto('/')
    
    await expect(page.getByRole('navigation')).toBeVisible()
  })

  test('应该在桌面设备上正确显示', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 })
    await page.goto('/')
    
    await expect(page.getByRole('navigation')).toBeVisible()
  })
})
```

#### 3.4 性能测试

##### 3.4.1 页面加载性能

**性能指标测试**：

```typescript
// e2e/performance.spec.ts
import { test, expect } from '@playwright/test'

test.describe('性能测试', () => {
  test('首页应该在3秒内加载完成', async ({ page }) => {
    const startTime = Date.now()
    await page.goto('/')
    await page.waitForLoadState('networkidle')
    const loadTime = Date.now() - startTime
    
    expect(loadTime).toBeLessThan(3000)
  })

  test('应该有良好的LCP性能', async ({ page }) => {
    const metrics = await page.evaluate(() => {
      return new Promise((resolve) => {
        new PerformanceObserver((list) => {
          const entries = list.getEntries()
          const lcp = entries[entries.length - 1]
          resolve({
            lcp: lcp.startTime,
            fid: performance.getEntriesByType('first-input')[0]?.processingStart,
            cls: performance.getEntriesByType('layout-shift')
              .reduce((sum, entry) => sum + entry.value, 0),
          })
        }).observe({ entryTypes: ['largest-contentful-paint', 'first-input', 'layout-shift'] })
      })
    })
    
    expect(metrics.lcp).toBeLessThan(2500)
    expect(metrics.cls).toBeLessThan(0.1)
  })

  test('应该正确缓存静态资源', async ({ page }) => {
    await page.goto('/')
    const response = await page.goto('/')
    
    const cacheHeader = response?.headers()['cache-control']
    expect(cacheHeader).toBeDefined()
  })
})
```

#### 3.5 可访问性测试

##### 3.5.1 A11y测试

**可访问性验证**：

```typescript
// e2e/accessibility.spec.ts
import { test, expect } from '@playwright/test'
import { injectAxe, checkA11y } from 'axe-playwright'

test.describe('可访问性', () => {
  test('首页应该符合WCAG标准', async ({ page }) => {
    await page.goto('/')
    await injectAxe(page)
    await checkA11y(page)
  })

  test('应该支持键盘导航', async ({ page }) => {
    await page.goto('/')
    
    await page.keyboard.press('Tab')
    const firstElement = page.locator(':focus')
    await expect(firstElement).toBeVisible()
    
    await page.keyboard.press('Enter')
    await expect(page).toHaveURL(/#/)
  })

  test('应该有正确的ARIA标签', async ({ page }) => {
    await page.goto('/')
    
    const navigation = page.getByRole('navigation')
    await expect(navigation).toHaveAttribute('aria-label', '主导航')
    
    const main = page.getByRole('main')
    await expect(main).toBeVisible()
  })
})
```

#### 3.6 测试数据管理

##### 3.6.1 测试数据准备

**测试数据管理**：

```typescript
// e2e/fixtures.ts
import { test as base } from '@playwright/test'

type TestFixtures = {
  testData: {
    user: {
      name: string
      email: string
      message: string
    }
  }
}

export const test = base.extend<TestFixtures>({
  testData: async ({}, use) => {
    const data = {
      user: {
        name: '测试用户',
        email: 'test@example.com',
        message: '这是一条测试消息',
      },
    }
    await use(data)
  },
})

export const expect = test.expect
```

##### 3.6.2 测试环境配置

**环境变量配置**：

```typescript
// e2e/env.ts
export const testEnv = {
  baseURL: process.env.BASE_URL || 'http://localhost:3000',
  apiURL: process.env.API_URL || 'http://localhost:3000/api',
  testUser: {
    email: process.env.TEST_USER_EMAIL || 'test@example.com',
    password: process.env.TEST_USER_PASSWORD || 'test123',
  },
}
```

#### 3.7 E2E测试最佳实践

##### 3.7.1 测试组织

**测试文件组织**：

```
e2e/
├── fixtures/
│   ├── auth.ts
│   └── data.ts
├── pages/
│   ├── HomePage.ts
│   ├── ServicesPage.ts
│   └── ContactPage.ts
├── utils/
│   ├── helpers.ts
│   └── selectors.ts
├── auth.spec.ts
├── home.spec.ts
├── services.spec.ts
├── contact.spec.ts
└── pricing.spec.ts
```

##### 3.7.2 页面对象模式

**Page Object实现**：

```typescript
// e2e/pages/HomePage.ts
import { Page, expect } from '@playwright/test'

export class HomePage {
  readonly page: Page
  readonly heroTitle: string
  readonly ctaButton: string
  readonly languageSwitcher: string

  constructor(page: Page) {
    this.page = page
    this.heroTitle = 'AI 驱动业绩增长'
    this.ctaButton = '预约免费咨询'
    this.languageSwitcher = '[role="combobox"]'
  }

  async goto() {
    await this.page.goto('/')
  }

  async waitForHero() {
    await expect(this.page.getByText(this.heroTitle)).toBeVisible()
  }

  async clickCTA() {
    await this.page.getByRole('button', { name: this.ctaButton }).click()
  }

  async switchLanguage(locale: string) {
    await this.page.locator(this.languageSwitcher).selectOption(locale)
  }
}
```

**使用Page Object**：

```typescript
// e2e/home.spec.ts
import { test } from './fixtures'
import { HomePage } from './pages/HomePage'

test('首页应该正确加载', async ({ page }) => {
  const homePage = new HomePage(page)
  await homePage.goto()
  await homePage.waitForHero()
})
```

##### 3.7.3 测试稳定性

**等待策略**：

```typescript
test('应该等待元素可见', async ({ page }) => {
  await page.goto('/')
  
  await page.waitForSelector('[data-testid="services"]', {
    state: 'visible',
    timeout: 5000,
  })
})

test('应该等待网络请求完成', async ({ page }) => {
  await page.goto('/')
  
  await page.waitForLoadState('networkidle')
  
  const response = await page.waitForResponse(
    response => response.url().includes('/api/services') && response.status() === 200
  )
  expect(response.ok()).toBeTruthy()
})
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
