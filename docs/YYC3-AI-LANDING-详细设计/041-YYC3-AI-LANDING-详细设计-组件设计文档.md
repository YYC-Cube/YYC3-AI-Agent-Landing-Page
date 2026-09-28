---
@file: 041-YYC3-AI-LANDING-详细设计-组件设计文档.md
@description: YYC3-AI-LANDING 前端组件的详细设计，包含组件Props、状态管理、事件处理的规范
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [详细设计],[组件设计],[前端组件]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 041-YYC3-AI-LANDING-详细设计

## 概述

本文档详细描述YYC3-AI-LANDING-详细设计-组件设计文档相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范组件设计文档相关的业务标准与技术落地要求
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

### 3. 组件设计文档

#### 3.1 组件设计原则

##### 3.1.1 设计原则
- **可复用性**：组件设计考虑复用场景，提供灵活的Props
- **可组合性**：使用Slot模式，支持asChild模式
- **类型安全**：完整的TypeScript类型定义，编译时检查
- **性能优化**：避免不必要的重渲染，使用React.memo优化
- **可访问性**：遵循WAI-ARIA标准，支持键盘导航
- **主题一致**：使用Tailwind CSS设计令牌，保持视觉一致性

##### 3.1.2 命名规范
- **组件文件**：PascalCase，如`Button.tsx`、`Card.tsx`
- **组件导出**：PascalCase，如`export { Button }`
- **Props接口**：组件名 + Props，如`ButtonProps`
- **事件处理**：on + 动作名，如`onClick`、`onSubmit`
- **布尔Props**：is + 形容词，如`isLoading`、`isDisabled`

##### 3.1.3 文件结构
```
components/
├── ui/                    # 基础UI组件
│   ├── button.tsx
│   ├── card.tsx
│   ├── dropdown-menu.tsx
│   ├── label.tsx
│   ├── navbar.tsx
│   ├── pricing.tsx
│   ├── sparkles.tsx
│   ├── spline-scene.tsx
│   └── spotlight.tsx
├── theme-provider.tsx    # 主题提供者
└── index.ts             # 统一导出
```

#### 3.2 基础组件设计

##### 3.2.1 Button组件

**组件路径**：`components/ui/button.tsx`

**功能描述**：
- 提供多种样式变体（default、destructive、outline、secondary、ghost、link）
- 支持多种尺寸（default、sm、lg、icon）
- 支持asChild模式，可渲染为其他元素
- 集成class-variance-authority进行样式管理

**Props定义**：
```typescript
interface ButtonProps extends React.ComponentProps<'button'> {
  variant?: 'default' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link'
  size?: 'default' | 'sm' | 'lg' | 'icon'
  asChild?: boolean
}
```

**使用示例**：
```typescript
// 默认按钮
<Button>点击我</Button>

// 主要操作按钮
<Button variant="default" size="lg">提交</Button>

// 次要按钮
<Button variant="secondary">取消</Button>

// 危险操作
<Button variant="destructive">删除</Button>

// 图标按钮
<Button size="icon">
  <Icon />
</Button>

// asChild模式
<Button asChild>
  <Link href="/contact">联系我们</Link>
</Button>
```

**样式变体**：
- **default**：主色调背景，白色文字，带阴影
- **destructive**：红色背景，白色文字，用于删除操作
- **outline**：透明背景，边框样式
- **secondary**：次要背景色
- **ghost**：透明背景，悬停时显示背景
- **link**：链接样式，带下划线

**尺寸规格**：
- **default**：高度36px，内边距8px
- **sm**：高度32px，内边距6px
- **lg**：高度40px，内边距12px
- **icon**：36px正方形

##### 3.2.2 Card组件

**组件路径**：`components/ui/card.tsx`

**功能描述**：
- 提供卡片容器组件
- 支持Header、Content、Footer子组件
- 提供样式变体（default、outline）
- 集成聚光灯效果

**Props定义**：
```typescript
interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  className?: string
}

interface CardHeaderProps extends React.HTMLAttributes<HTMLDivElement> {
  className?: string
}

interface CardContentProps extends React.HTMLAttributes<HTMLDivElement> {
  className?: string
}
```

**使用示例**：
```typescript
// 基础卡片
<Card>
  <CardHeader>
    <h2>标题</h2>
  </CardHeader>
  <CardContent>
    <p>内容</p>
  </CardContent>
</Card>

// 带聚光灯效果
<Card className="relative overflow-hidden">
  <Spotlight className="-top-40 left-0" fill="white" />
  <CardContent>
    内容
  </CardContent>
</Card>
```

##### 3.2.3 Navbar组件

**组件路径**：`components/ui/navbar.tsx`

**功能描述**：
- 响应式导航栏
- 桌面端：水平导航链接
- 移动端：汉堡菜单
- 集成语言切换器
- 滚动时样式变化（透明/固定）

**Props定义**：
```typescript
interface NavbarProps {
  className?: string
}
```

**使用示例**：
```typescript
<Navbar />
```

**导航链接**：
- 服务 / Services
- 客户评价 / Testimonials
- 定价 / Pricing
- 联系我们 / Contact

##### 3.2.4 LanguageSwitcher组件

**组件路径**：`components/ui/language-switcher.tsx`

**功能描述**：
- 语言切换下拉菜单
- 支持中文和英文
- 保存语言偏好到localStorage
- 更新HTML lang属性

**Props定义**：
```typescript
interface LanguageSwitcherProps {
  className?: string
}
```

**使用示例**：
```typescript
<LanguageSwitcher />
```

##### 3.2.5 Pricing组件

**组件路径**：`components/ui/pricing.tsx`

**功能描述**：
- 展示三个定价层级（Starter、Professional、Enterprise）
- 每个层级包含功能列表和CTA按钮
- 响应式布局（移动端堆叠，桌面端并排）
- 悬停效果增强交互

**Props定义**：
```typescript
interface PricingProps {
  className?: string
}
```

**使用示例**：
```typescript
<Pricing />
```

**定价层级**：
- **Starter**：入门版，适合小型企业
- **Professional**：专业版，适合成长型企业
- **Enterprise**：企业版，适合大型组织

##### 3.2.6 SplineScene组件

**组件路径**：`components/ui/spline-scene.tsx`

**功能描述**：
- 集成Spline 3D场景
- 响应式加载和显示
- 支持懒加载和降级方案
- 交互式3D模型

**Props定义**：
```typescript
interface SplineSceneProps {
  scene: string
  className?: string
}
```

**使用示例**：
```typescript
<SplineScene
  scene="https://prod.spline.design/UbM7F-HZcyTbZ4y3/scene.splinecode"
  className="w-full h-full"
/>
```

**当前场景**：
- Hero区域3D模型
- 交互效果：鼠标移动响应
- 响应式适配：桌面、平板、移动

##### 3.2.7 Spotlight组件

**组件路径**：`components/ui/spotlight.tsx`

**功能描述**：
- 聚光灯背景效果
- 可配置位置和颜色
- 增强视觉吸引力
- GPU加速渲染

**Props定义**：
```typescript
interface SpotlightProps {
  className?: string
  fill?: string
}
```

**使用示例**：
```typescript
<Spotlight className="-top-40 left-0" fill="white" />
```

##### 3.2.8 AnimatedGradientBackground组件

**组件路径**：`components/ui/animated-gradient-background.tsx`

**功能描述**：
- 动态渐变背景
- 流畅的颜色过渡
- 性能优化的动画
- 增强页面视觉效果

**Props定义**：
```typescript
interface AnimatedGradientBackgroundProps {
  className?: string
}
```

**使用示例**：
```typescript
<AnimatedGradientBackground />
```

##### 3.2.9 Sparkles组件

**组件路径**：`components/ui/sparkles.tsx`

**功能描述**：
- 粒子闪光效果
- 鼠标交互响应
- 可配置粒子数量和行为
- 轻量级实现

**Props定义**：
```typescript
interface SparklesProps {
  className?: string
}
```

**使用示例**：
```typescript
<SparklesCore />
```

##### 3.2.10 BentoGrid组件

**组件路径**：`components/ui/bento-grid.tsx`

**功能描述**：
- Bento网格布局
- 响应式卡片排列
- 悬停效果和动画
- 现代化UI设计

**Props定义**：
```typescript
interface BentoGridProps {
  className?: string
}

interface BentoCardProps {
  className?: string
  children?: React.ReactNode
}
```

**使用示例**：
```typescript
<BentoGrid>
  <BentoCard>卡片1</BentoCard>
  <BentoCard>卡片2</BentoCard>
  <BentoCard>卡片3</BentoCard>
</BentoGrid>
```

#### 3.3 上下文和Hook设计

##### 3.3.1 LocaleContext

**文件路径**：`contexts/locale-context.tsx`

**功能描述**：
- 提供全局语言状态管理
- 支持语言切换和持久化
- 提供useLocale Hook

**Context接口**：
```typescript
interface LocaleContextType {
  locale: Locale
  setLocale: (locale: Locale) => void
  t: Translations
}
```

**使用示例**：
```typescript
// 在组件中使用
function MyComponent() {
  const { locale, setLocale, t } = useLocale()
  
  return (
    <div>
      <p>{t.hero.title}</p>
      <button onClick={() => setLocale('en')}>English</button>
      <button onClick={() => setLocale('zh')}>中文</button>
    </div>
  )
}
```

##### 3.3.2 useMediaQuery Hook

**文件路径**：`hooks/use-media-query.ts`

**功能描述**：
- 响应式媒体查询Hook
- 提供断点检测
- 支持移动、平板、桌面判断

**Hook签名**：
```typescript
function useMediaQuery(query: string): boolean
```

**使用示例**：
```typescript
function MyComponent() {
  const isMobile = useMediaQuery('(max-width: 768px)')
  const isTablet = useMediaQuery('(min-width: 768px) and (max-width: 1024px)')
  const isDesktop = useMediaQuery('(min-width: 1024px)')
  
  return (
    <div>
      {isMobile && <MobileView />}
      {isTablet && <TableView />}
      {isDesktop && <DesktopView />}
    </div>
  )
}
```

#### 3.4 组件性能优化

##### 3.4.1 React.memo使用
- 对纯展示组件使用React.memo
- 避免不必要的重渲染
- Props相同时跳过渲染

##### 3.4.2 useCallback优化
- 事件处理函数使用useCallback
- 避免子组件不必要的重渲染
- 保持函数引用稳定

##### 3.4.3 useMemo优化
- 复杂计算使用useMemo
- 避免每次渲染重新计算
- 提升渲染性能

#### 3.5 组件测试策略

##### 3.5.1 单元测试
- 使用React Testing Library
- 测试组件渲染和交互
- Mock Context和Hook

##### 3.5.2 可访问性测试
- 使用axe-core进行可访问性测试
- 验证键盘导航
- 检查颜色对比度
- 确保ARIA标签正确

##### 3.5.3 响应式测试
- 测试不同屏幕尺寸
- 验证移动端、平板端、桌面端显示
- 检查断点切换逻辑

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
