---
@file: 082-YYC3-AI-LANDING-测试文档-集成测试规范.md
@description: YYC3-AI-LANDING 集成测试的编写规范、测试场景设计、环境配置
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [测试文档],[集成测试],[测试规范]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 082-YYC3-AI-LANDING-测试文档

## 概述

本文档详细描述YYC3-AI-LANDING-测试文档-集成测试规范相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范集成测试规范相关的业务标准与技术落地要求
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

### 3. 集成测试规范

#### 3.1 集成测试概述

##### 3.1.1 测试目标

**集成测试目的**：
- 验证多个组件或模块之间的交互
- 测试API集成和数据流
- 验证状态管理和副作用
- 确保模块间的接口契约

**测试范围**：
- 组件集成测试
- API集成测试
- 状态管理集成测试
- 第三方服务集成测试

##### 3.1.2 测试环境

**测试环境配置**：

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.integration.ts'],
    include: ['**/*.integration.test.{ts,tsx}'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'lcov'],
      include: ['src/**/*.{ts,tsx}'],
      exclude: [
        'src/**/*.test.{ts,tsx}',
        'src/**/*.spec.{ts,tsx}',
        'src/test/**/*',
      ],
    },
  },
})
```

#### 3.2 API集成测试

##### 3.2.1 API Mock配置

**MSW (Mock Service Worker)配置**：

```bash
npm install -D msw @msw/node
```

**Mock服务器设置**：

```typescript
// src/test/mocks/handlers.ts
import { http, HttpResponse } from 'msw'

export const handlers = [
  // 获取首页配置
  http.get('/api/v1/home/config', () => {
    return HttpResponse.json({
      success: true,
      data: {
        hero: {
          title: 'AI 驱动业绩增长，降低运营成本',
          subtitle: '我们帮助企业自动化工作流程...',
        },
      },
      timestamp: new Date().toISOString(),
    })
  }),

  // 获取服务列表
  http.get('/api/v1/services', ({ request }) => {
    const url = new URL(request.url)
    const page = url.searchParams.get('page') || '1'
    const pageSize = url.searchParams.get('pageSize') || '20'

    return HttpResponse.json({
      success: true,
      data: mockServices,
      pagination: {
        page: parseInt(page),
        pageSize: parseInt(pageSize),
        total: mockServices.length,
        totalPages: Math.ceil(mockServices.length / parseInt(pageSize)),
      },
      timestamp: new Date().toISOString(),
    })
  }),

  // 提交联系表单
  http.post('/api/v1/contact', async ({ request }) => {
    const body = await request.json()
    
    if (!body.email || !body.message) {
      return HttpResponse.json(
        {
          success: false,
          error: {
            code: 'VALIDATION_REQUIRED_FIELD',
            message: '缺少必填字段',
          },
          timestamp: new Date().toISOString(),
        },
        { status: 400 }
      )
    }

    return HttpResponse.json({
      success: true,
      data: {
        id: 'contact-123',
        status: 'pending',
        estimatedResponseTime: '24小时内',
      },
      timestamp: new Date().toISOString(),
    })
  }),
]

// Mock数据
const mockServices = [
  {
    id: 'service-001',
    name: 'AI 聊天机器人与虚拟助手',
    category: 'chatbot',
    description: '智能对话代理...',
    icon: 'Bot',
    status: 'active',
    featured: true,
  },
  // ...更多服务
]
```

##### 3.2.2 API集成测试用例

**首页API集成测试**：

```typescript
// src/lib/api/home.integration.test.ts
import { describe, it, expect, beforeAll, afterEach } from 'vitest'
import { setupServer } from 'msw/node'
import { handlers } from '@/test/mocks/handlers'
import { getHomeConfig } from './home'

const server = setupServer(...handlers)

describe('Home API Integration', () => {
  beforeAll(() => {
    server.listen()
  })

  afterEach(() => {
    server.resetHandlers()
  })

  it('应该成功获取首页配置', async () => {
    const config = await getHomeConfig()
    
    expect(config).toBeDefined()
    expect(config.hero).toBeDefined()
    expect(config.hero.title).toBe('AI 驱动业绩增长，降低运营成本')
  })

  it('应该处理API错误', async () => {
    server.use(
      http.get('/api/v1/home/config', () => {
        return new HttpResponse(null, { status: 500 })
      })
    )

    await expect(getHomeConfig()).rejects.toThrow('API Error')
  })
})
```

**服务API集成测试**：

```typescript
// src/lib/api/services.integration.test.ts
import { describe, it, expect, beforeAll, afterEach } from 'vitest'
import { setupServer } from 'msw/node'
import { handlers } from '@/test/mocks/handlers'
import { getServices, getServiceDetail } from './services'

const server = setupServer(...handlers)

describe('Services API Integration', () => {
  beforeAll(() => {
    server.listen()
  })

  afterEach(() => {
    server.resetHandlers()
  })

  describe('getServices', () => {
    it('应该获取服务列表', async () => {
      const services = await getServices({ page: 1, pageSize: 20 })
      
      expect(services).toHaveLength(5)
      expect(services[0]).toHaveProperty('id')
      expect(services[0]).toHaveProperty('name')
    })

    it('应该支持分页', async () => {
      const page1 = await getServices({ page: 1, pageSize: 2 })
      const page2 = await getServices({ page: 2, pageSize: 2 })
      
      expect(page1[0].id).not.toBe(page2[0].id)
    })

    it('应该支持分类筛选', async () => {
      const chatbotServices = await getServices({ category: 'chatbot' })
      
      chatbotServices.forEach(service => {
        expect(service.category).toBe('chatbot')
      })
    })
  })

  describe('getServiceDetail', () => {
    it('应该获取服务详情', async () => {
      const detail = await getServiceDetail('service-001')
      
      expect(detail).toBeDefined()
      expect(detail.id).toBe('service-001')
      expect(detail.pricing).toBeDefined()
      expect(detail.features).toBeDefined()
    })

    it('应该处理不存在的服务', async () => {
      server.use(
        http.get('/api/v1/services/not-found', () => {
          return new HttpResponse(null, { status: 404 })
        })
      )

      await expect(getServiceDetail('not-found')).rejects.toThrow('Service not found')
    })
  })
})
```

#### 3.3 组件集成测试

##### 3.3.1 页面级组件测试

**首页集成测试**：

```typescript
// src/app/page.integration.test.tsx
import { describe, it, expect, beforeAll, afterEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { setupServer } from 'msw/node'
import { handlers } from '@/test/mocks/handlers'
import HomePage from './page'

const server = setupServer(...handlers)

describe('HomePage Integration', () => {
  beforeAll(() => {
    server.listen()
  })

  afterEach(() => {
    server.resetHandlers()
  })

  it('应该渲染完整的首页', async () => {
    render(<HomePage />)
    
    await waitFor(() => {
      expect(screen.getByText('AI 驱动业绩增长，降低运营成本')).toBeInTheDocument()
    })
  })

  it('应该加载并显示服务列表', async () => {
    render(<HomePage />)
    
    await waitFor(() => {
      const services = screen.getAllByRole('article')
      expect(services.length).toBeGreaterThan(0)
    })
  })

  it('应该显示语言切换器', () => {
    render(<HomePage />)
    
    const languageSwitcher = screen.getByRole('combobox')
    expect(languageSwitcher).toBeInTheDocument()
  })
})
```

##### 3.3.2 复杂组件集成测试

**定价页面集成测试**：

```typescript
// src/components/Pricing/Pricing.integration.test.tsx
import { describe, it, expect, beforeAll, afterEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { setupServer } from 'msw/node'
import { handlers } from '@/test/mocks/handlers'
import { Pricing } from './Pricing'

const server = setupServer(...handlers)

describe('Pricing Integration', () => {
  beforeAll(() => {
    server.listen()
  })

  afterEach(() => {
    server.resetHandlers()
  })

  it('应该渲染所有定价计划', async () => {
    render(<Pricing />)
    
    await waitFor(() => {
      expect(screen.getByText('Starter')).toBeInTheDocument()
      expect(screen.getByText('Professional')).toBeInTheDocument()
      expect(screen.getByText('Enterprise')).toBeInTheDocument()
    })
  })

  it('应该支持年付/月付切换', async () => {
    render(<Pricing />)
    
    const toggle = await screen.findByRole('switch')
    await userEvent.click(toggle)
    
    const prices = screen.getAllByText(/\$\d+/)
    expect(prices.length).toBeGreaterThan(0)
  })

  it('应该在点击CTA按钮时调用回调', async () => {
    const handleSelect = vi.fn()
    render(<Pricing onSelectPlan={handleSelect} />)
    
    await waitFor(() => {
      const buttons = screen.getAllByRole('button')
      await userEvent.click(buttons[0])
    })
    
    expect(handleSelect).toHaveBeenCalled()
  })
})
```

#### 3.4 状态管理集成测试

##### 3.4.1 Context集成测试

**国际化Context集成测试**：

```typescript
// src/lib/i18n/integration.test.tsx
import { describe, it, expect, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { LocaleProvider } from './LocaleProvider'
import { useLocale } from './useLocale'

describe('LocaleContext Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('应该提供翻译功能', () => {
    const TestComponent = () => {
      const { t } = useLocale()
      return <div>{t('services')}</div>
    }

    render(
      <LocaleProvider defaultLocale="zh">
        <TestComponent />
      </LocaleProvider>
    )

    expect(screen.getByText('服务')).toBeInTheDocument()
  })

  it('应该支持语言切换', () => {
    const TestComponent = () => {
      const { t, locale, setLocale } = useLocale()
      return (
        <div>
          <span data-testid="locale">{locale}</span>
          <span>{t('services')}</span>
          <button onClick={() => setLocale('en')}>Switch to English</button>
        </div>
      )
    }

    render(
      <LocaleProvider defaultLocale="zh">
        <TestComponent />
      </LocaleProvider>
    )

    expect(screen.getByTestId('locale')).toHaveTextContent('zh')
    expect(screen.getByText('服务')).toBeInTheDocument()

    const button = screen.getByText('Switch to English')
    fireEvent.click(button)

    expect(screen.getByTestId('locale')).toHaveTextContent('en')
    expect(screen.getByText('Services')).toBeInTheDocument()
  })
})
```

#### 3.5 第三方服务集成测试

##### 3.5.1 Spline 3D场景测试

**Spline组件集成测试**：

```typescript
// src/components/SplineScene/SplineScene.integration.test.tsx
import { describe, it, expect, vi, beforeAll, afterEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { SplineScene } from './SplineScene'

vi.mock('@splinetool/react-spline', () => ({
  Spline: ({ scene, onLoad }) => {
    React.useEffect(() => {
      if (onLoad) onLoad()
    }, [onLoad])
    return <div data-testid="spline-mock">{scene}</div>
  },
}))

describe('SplineScene Integration', () => {
  it('应该渲染Spline场景', () => {
    const scene = 'https://prod.spline.design/xxx/scene.splinecode'
    render(<SplineScene scene={scene} />)
    
    const spline = screen.getByTestId('spline-mock')
    expect(spline).toBeInTheDocument()
    expect(spline).toHaveTextContent(scene)
  })

  it('应该在加载时调用onLoad回调', async () => {
    const onLoad = vi.fn()
    const scene = 'https://prod.spline.design/xxx/scene.splinecode'
    
    render(<SplineScene scene={scene} onLoad={onLoad} />)
    
    await waitFor(() => {
      expect(onLoad).toHaveBeenCalledTimes(1)
    })
  })

  it('应该处理加载错误', async () => {
    const onError = vi.fn()
    const scene = 'invalid-url'
    
    render(<SplineScene scene={scene} onError={onError} />)
    
    await waitFor(() => {
      expect(onError).toHaveBeenCalled()
    })
  })
})
```

#### 3.6 集成测试最佳实践

##### 3.6.1 测试隔离

**使用独立的测试服务器**：

```typescript
// src/test/setup.integration.ts
import { setupServer } from 'msw/node'
import { handlers } from './mocks/handlers'

export const server = setupServer(...handlers)

beforeAll(() => {
  server.listen({ onUnhandledRequest: 'error' })
})

afterEach(() => {
  server.resetHandlers()
})

afterAll(() => {
  server.close()
})
```

##### 3.6.2 测试数据管理

**使用固定的测试数据**：

```typescript
// src/test/mocks/data.ts
export const mockHomeConfig = {
  hero: {
    title: 'AI 驱动业绩增长，降低运营成本',
    subtitle: '我们帮助企业自动化工作流程...',
    ctaPrimary: '预约免费咨询',
    ctaSecondary: '查看案例研究',
  },
  problemSolution: {
    problemTitle: '还在手动管理一切？',
    problems: [
      '在重复性任务上花费大量时间',
      '因无法 7×24 小时响应咨询而错失潜在客户',
    ],
    solutionTitle: '我们构建真正有效的 AI 解决方案',
    solutions: [
      '定制 AI 代理，即时处理客户咨询',
      '工作流自动化，每周节省 20+ 小时',
    ],
  },
}

export const mockServices = [
  {
    id: 'service-001',
    name: 'AI 聊天机器人与虚拟助手',
    category: 'chatbot',
    description: '智能对话代理...',
    icon: 'Bot',
    status: 'active',
    featured: true,
  },
  // ...更多服务
]
```

##### 3.6.3 异步测试处理

**使用waitFor处理异步操作**：

```typescript
it('应该异步加载数据', async () => {
  render(<Component />)
  
  await waitFor(
    () => {
      expect(screen.getByText('加载完成')).toBeInTheDocument()
    },
    { timeout: 5000 }
  )
})
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
