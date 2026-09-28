---
@file: 081-YYC3-AI-LANDING-测试文档-单元测试规范.md
@description: YYC3-AI-LANDING 单元测试的编写规范、测试用例设计、覆盖率要求
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [测试文档],[单元测试],[测试规范]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 081-YYC3-AI-LANDING-测试文档

## 概述

本文档详细描述YYC3-AI-LANDING-测试文档-单元测试规范相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范单元测试规范相关的业务标准与技术落地要求
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

### 3. 单元测试规范

#### 3.1 测试框架选择

##### 3.1.1 Vitest配置

**安装依赖**：

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event
npm install -D @vitejs/plugin-react jsdom
```

**配置文件**：

```typescript
// vitest.config.ts
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
        '**/mockData',
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
      '@/components': path.resolve(__dirname, './src/components'),
      '@/lib': path.resolve(__dirname, './src/lib'),
      '@/hooks': path.resolve(__dirname, './src/hooks'),
      '@/types': path.resolve(__dirname, './src/types'),
      '@/utils': path.resolve(__dirname, './src/utils'),
    },
  },
})
```

##### 3.1.2 测试工具库

**Testing Library**：

```typescript
// src/test/setup.ts
import { expect, afterEach, vi } from 'vitest'
import { cleanup } from '@testing-library/react'
import * as matchers from '@testing-library/jest-dom/matchers'

expect.extend(matchers)

afterEach(() => {
  cleanup()
})
```

#### 3.2 测试文件组织

##### 3.2.1 目录结构

```
src/
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   └── index.ts
│   ├── Card/
│   │   ├── Card.tsx
│   │   ├── Card.test.tsx
│   │   └── index.ts
│   └── Navbar/
│       ├── Navbar.tsx
│       ├── Navbar.test.tsx
│       └── index.ts
├── lib/
│   ├── i18n.ts
│   ├── i18n.test.ts
│   ├── utils.ts
│   └── utils.test.ts
└── test/
    ├── setup.ts
    ├── mocks/
    │   ├── data.ts
    │   └── handlers.ts
    └── helpers.ts
```

##### 3.2.2 命名规范

**测试文件命名**：
- 组件测试：`ComponentName.test.tsx`
- 工具函数测试：`utilName.test.ts`
- Hook测试：`hookName.test.ts`

**测试用例命名**：
- 使用描述性名称
- 以"应该"或"should"开头
- 描述被测试的行为

```typescript
describe('Button', () => {
  it('应该渲染正确的文本', () => {})
  it('应该在点击时调用onClick', () => {})
  it('应该在禁用状态下不响应点击', () => {})
})
```

#### 3.3 组件测试规范

##### 3.3.1 基础组件测试

**Button组件测试**：

```typescript
// src/components/Button/Button.test.tsx
import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Button } from './Button'

describe('Button', () => {
  it('应该渲染正确的文本', () => {
    render(<Button>点击我</Button>)
    expect(screen.getByText('点击我')).toBeInTheDocument()
  })

  it('应该在点击时调用onClick', async () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>点击我</Button>)
    
    const button = screen.getByText('点击我')
    await userEvent.click(button)
    
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('应该在禁用状态下不响应点击', async () => {
    const handleClick = vi.fn()
    render(
      <Button onClick={handleClick} disabled>
        点击我
      </Button>
    )
    
    const button = screen.getByText('点击我')
    await userEvent.click(button)
    
    expect(handleClick).not.toHaveBeenCalled()
  })

  it('应该应用正确的variant样式', () => {
    const { container } = render(<Button variant="destructive">删除</Button>)
    expect(container.firstChild).toHaveClass('bg-destructive')
  })
})
```

##### 3.3.2 复杂组件测试

**Navbar组件测试**：

```typescript
// src/components/Navbar/Navbar.test.tsx
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { Navbar } from './Navbar'

const mockLinks = [
  { label: '服务', href: '/services' },
  { label: '定价', href: '/pricing' },
  { label: '联系我们', href: '/contact' },
]

describe('Navbar', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('应该渲染所有导航链接', () => {
    render(<Navbar links={mockLinks} />)
    
    mockLinks.forEach(link => {
      expect(screen.getByText(link.label)).toBeInTheDocument()
    })
  })

  it('应该在移动端隐藏导航菜单', () => {
    render(<Navbar links={mockLinks} />)
    const menu = screen.queryByRole('navigation')
    expect(menu).not.toBeVisible()
  })

  it('应该在语言切换时调用onLocaleChange', async () => {
    const handleLocaleChange = vi.fn()
    render(
      <Navbar 
        links={mockLinks} 
        currentLocale="zh"
        onLocaleChange={handleLocaleChange}
      />
    )
    
    const languageSwitcher = screen.getByRole('combobox')
    await userEvent.click(languageSwitcher)
    
    expect(handleLocaleChange).toHaveBeenCalled()
  })
})
```

#### 3.4 Hook测试规范

##### 3.4.1 自定义Hook测试

**useLocale Hook测试**：

```typescript
// src/hooks/useLocale.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { useLocale } from './useLocale'

describe('useLocale', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('应该返回当前语言', () => {
    const { result } = renderHook(() => useLocale())
    expect(result.current.locale).toBe('zh')
  })

  it('应该提供切换语言的方法', () => {
    const { result } = renderHook(() => useLocale())
    
    act(() => {
      result.current.setLocale('en')
    })
    
    expect(result.current.locale).toBe('en')
  })

  it('应该更新翻译内容', () => {
    const { result } = renderHook(() => useLocale())
    
    act(() => {
      result.current.setLocale('en')
    })
    
    expect(result.current.t('services')).toBe('Services')
  })
})
```

#### 3.5 工具函数测试规范

##### 3.5.1 纯函数测试

**工具函数测试**：

```typescript
// src/lib/utils.test.ts
import { describe, it, expect } from 'vitest'
import { formatCurrency, formatDate, validateEmail } from './utils'

describe('formatCurrency', () => {
  it('应该正确格式化美元', () => {
    expect(formatCurrency(100, 'USD')).toBe('$100.00')
  })

  it('应该正确格式化人民币', () => {
    expect(formatCurrency(100, 'CNY')).toBe('¥100.00')
  })

  it('应该处理小数', () => {
    expect(formatCurrency(99.99, 'USD')).toBe('$99.99')
  })
})

describe('validateEmail', () => {
  it('应该验证有效的邮箱', () => {
    expect(validateEmail('test@example.com')).toBe(true)
  })

  it('应该拒绝无效的邮箱', () => {
    expect(validateEmail('invalid-email')).toBe(false)
    expect(validateEmail('test@')).toBe(false)
  })

  it('应该拒绝空字符串', () => {
    expect(validateEmail('')).toBe(false)
  })
})
```

#### 3.6 Mock和Stub

##### 3.6.1 Mock外部依赖

**Mock API调用**：

```typescript
// src/lib/api.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { fetchServices } from './api'

describe('fetchServices', () => {
  beforeEach(() => {
    global.fetch = vi.fn()
  })

  it('应该获取服务列表', async () => {
    const mockServices = [
      { id: '1', name: '服务1' },
      { id: '2', name: '服务2' },
    ]
    
    vi.mocked(global.fetch).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: mockServices }),
    } as Response)

    const result = await fetchServices()
    
    expect(result).toEqual(mockServices)
  })

  it('应该处理API错误', async () => {
    vi.mocked(global.fetch).mockResolvedValueOnce({
      ok: false,
      status: 500,
    } as Response)

    await expect(fetchServices()).rejects.toThrow('API Error')
  })
})
```

##### 3.6.2 Mock React组件

**Mock子组件**：

```typescript
// src/components/Parent.test.tsx
import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { Parent } from './Parent'

vi.mock('./Child', () => ({
  Child: ({ onClick }) => (
    <button onClick={onClick}>Mock Child</button>
  ),
}))

describe('Parent', () => {
  it('应该渲染子组件', () => {
    render(<Parent />)
    expect(screen.getByText('Mock Child')).toBeInTheDocument()
  })
})
```

#### 3.7 测试覆盖率

##### 3.7.1 覆盖率要求

**覆盖率阈值**：

| 类型 | 阈值 | 说明 |
|------|------|------|
| 语句覆盖率 | ≥ 80% | 代码语句覆盖 |
| 分支覆盖率 | ≥ 75% | 条件分支覆盖 |
| 函数覆盖率 | ≥ 80% | 函数定义覆盖 |
| 行覆盖率 | ≥ 80% | 代码行覆盖 |

##### 3.7.2 生成覆盖率报告

**运行测试并生成报告**：

```bash
# 运行所有测试并生成覆盖率报告
npm run test:unit -- --coverage

# 生成HTML报告
npm run test:unit -- --coverage --reporter=html

# 查看覆盖率报告
open coverage/index.html
```

**覆盖率报告配置**：

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      all: true,
      include: ['src/**/*.{ts,tsx}'],
      exclude: [
        'src/**/*.d.ts',
        'src/**/*.test.{ts,tsx}',
        'src/**/*.spec.{ts,tsx}',
        'src/test/**/*',
      ],
    },
  },
})
```

#### 3.8 测试最佳实践

##### 3.8.1 AAA原则

**Arrange-Act-Assert模式**：

```typescript
it('应该正确计算总价', () => {
  // Arrange (准备)
  const price = 100
  const quantity = 2
  const discount = 0.1
  
  // Act (执行)
  const total = calculateTotal(price, quantity, discount)
  
  // Assert (断言)
  expect(total).toBe(180)
})
```

##### 3.8.2 测试隔离

**每个测试独立运行**：

```typescript
describe('UserService', () => {
  beforeEach(() => {
    // 每个测试前重置状态
    vi.clearAllMocks()
  })
  
  afterEach(() => {
    // 每个测试后清理
    cleanup()
  })
})
```

##### 3.8.3 避免测试实现细节

**测试行为而非实现**：

```typescript
// ❌ 错误：测试实现细节
it('应该设置内部状态', () => {
  const { result } = renderHook(() => useCounter())
  expect(result.current.count).toBe(0)
})

// ✅ 正确：测试行为
it('应该从0开始计数', () => {
  const { result } = renderHook(() => useCounter())
  expect(result.current.count).toBe(0)
})
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
