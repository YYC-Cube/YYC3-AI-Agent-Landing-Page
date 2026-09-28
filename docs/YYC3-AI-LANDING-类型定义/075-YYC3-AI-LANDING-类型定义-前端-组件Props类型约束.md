---
@file: 075-YYC3-AI-LANDING-类型定义-前端-组件Props类型约束.md
@description: YYC3-AI-LANDING 前端组件Props的类型定义、默认值、校验规则的统一规范
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [类型定义],[前端],[组件约束]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 075-YYC3-AI-LANDING-类型定义

## 概述

本文档详细描述YYC3-AI-LANDING-类型定义-前端-组件Props类型约束相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范前端-组件Props类型约束相关的业务标准与技术落地要求
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

### 3. 前端-组件Props类型约束

#### 3.1 组件Props设计原则

##### 3.1.1 Props命名规范

**命名规则**：
- 使用camelCase命名
- 事件处理函数使用on前缀
- 布尔值使用is/has前缀
- 回调函数使用handle前缀

**示例**：
```typescript
interface ButtonProps {
  onClick: () => void
  isLoading: boolean
  isDisabled: boolean
  handleHover: () => void
  className?: string
}
```

##### 3.1.2 Props默认值规范

**默认值设置原则**：
- 必填属性不设置默认值
- 可选属性提供合理的默认值
- 布尔值默认为false
- 数组默认为空数组[]
- 对象默认为空对象{}

**示例**：
```typescript
interface CardProps {
  variant?: 'default' | 'outlined' | 'elevated'
  shadow?: boolean
  padding?: 'none' | 'sm' | 'md' | 'lg'
}

const defaultProps: Partial<CardProps> = {
  variant: 'default',
  shadow: false,
  padding: 'md'
}
```

##### 3.1.3 Props类型校验

**使用PropTypes进行运行时校验**：
```typescript
import PropTypes from 'prop-types'

interface ButtonProps {
  variant?: ButtonVariant
  size?: ButtonSize
  disabled?: boolean
  onClick?: () => void
}

const buttonPropTypes = {
  variant: PropTypes.oneOf(['default', 'destructive', 'outline', 'secondary', 'ghost', 'link']),
  size: PropTypes.oneOf(['default', 'sm', 'lg', 'icon']),
  disabled: PropTypes.bool,
  onClick: PropTypes.func
}
```

#### 3.2 核心组件Props定义

##### 3.2.1 Button组件Props

```typescript
/**
 * Button组件属性
 * @component Button
 */
export interface ButtonProps extends React.ComponentProps<'button'> {
  /**
   * 按钮变体样式
   * @default 'default'
   */
  variant?: 'default' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link'
  
  /**
   * 按钮尺寸
   * @default 'default'
   */
  size?: 'default' | 'sm' | 'lg' | 'icon'
  
  /**
   * 是否渲染为子元素
   * @default false
   */
  asChild?: boolean
  
  /**
   * 是否禁用
   * @default false
   */
  disabled?: boolean
  
  /**
   * 是否加载中
   * @default false
   */
  isLoading?: boolean
  
  /**
   * 加载时显示的文本
   */
  loadingText?: string
  
  /**
   * 自定义样式类名
   */
  className?: string
  
  /**
   * 点击事件处理
   */
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void
  
  /**
   * 鼠标移入事件
   */
  onMouseEnter?: (event: React.MouseEvent<HTMLButtonElement>) => void
  
  /**
   * 鼠标移出事件
   */
  onMouseLeave?: (event: React.MouseEvent<HTMLButtonElement>) => void
}

/**
 * Button组件默认Props
 */
export const buttonDefaultProps: Partial<ButtonProps> = {
  variant: 'default',
  size: 'default',
  asChild: false,
  disabled: false,
  isLoading: false
}
```

##### 3.2.2 Card组件Props

```typescript
/**
 * Card组件属性
 * @component Card
 */
export interface CardProps extends React.ComponentProps<'div'> {
  /**
   * 卡片变体
   * @default 'default'
   */
  variant?: 'default' | 'outlined' | 'elevated'
  
  /**
   * 是否显示阴影
   * @default false
   */
  shadow?: boolean
  
  /**
   * 内边距大小
   * @default 'md'
   */
  padding?: 'none' | 'sm' | 'md' | 'lg'
  
  /**
   * 圆角大小
   * @default 'md'
   */
  radius?: 'none' | 'sm' | 'md' | 'lg' | 'full'
  
  /**
   * 背景颜色
   */
  backgroundColor?: string
  
  /**
   * 自定义样式类名
   */
  className?: string
  
  /**
   * 点击事件
   */
  onClick?: (event: React.MouseEvent<HTMLDivElement>) => void
}

/**
 * CardContent组件属性
 * @component CardContent
 */
export interface CardContentProps extends React.ComponentProps<'div'> {
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * CardHeader组件属性
 * @component CardHeader
 */
export interface CardHeaderProps extends React.ComponentProps<'div'> {
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * CardTitle组件属性
 * @component CardTitle
 */
export interface CardTitleProps extends React.ComponentProps<'h3'> {
  /**
   * 标题级别
   * @default 'h3'
   */
  level?: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6'
  
  /**
   * 文本对齐方式
   * @default 'left'
   */
  align?: 'left' | 'center' | 'right'
  
  /**
   * 自定义样式类名
   */
  className?: string
}
```

##### 3.2.3 Navbar组件Props

```typescript
/**
 * Navbar组件属性
 * @component Navbar
 */
export interface NavbarProps {
  /**
   * 导航栏变体
   * @default 'default'
   */
  variant?: 'default' | 'transparent' | 'sticky' | 'floating'
  
  /**
   * Logo图片
   */
  logo?: {
    src: string
    alt: string
    width?: number
    height?: number
  }
  
  /**
   * 导航链接列表
   */
  links?: NavLink[]
  
  /**
   * 导航栏操作按钮
   */
  actions?: NavbarAction[]
  
  /**
   * 当前激活的链接
   */
  activeLink?: string
  
  /**
   * 是否显示语言切换器
   * @default true
   */
  showLanguageSwitcher?: boolean
  
  /**
   * 当前语言
   */
  currentLocale?: Locale
  
  /**
   * 语言切换回调
   */
  onLocaleChange?: (locale: Locale) => void
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * 导航链接类型
 */
export interface NavLink {
  /**
   * 链接文本
   */
  label: string
  
  /**
   * 链接地址
   */
  href: string
  
  /**
   * 是否外部链接
   * @default false
   */
  external?: boolean
  
  /**
   * 是否新窗口打开
   * @default false
   */
  target?: '_blank' | '_self' | '_parent' | '_top'
  
  /**
   * 图标
   */
  icon?: React.ReactNode
  
  /**
   * 是否禁用
   * @default false
   */
  disabled?: boolean
}

/**
 * 导航栏操作类型
 */
export interface NavbarAction {
  /**
   * 操作按钮文本
   */
  label: string
  
  /**
   * 点击回调
   */
  onClick: () => void
  
  /**
   * 按钮变体
   * @default 'default'
   */
  variant?: 'default' | 'outline' | 'ghost'
  
  /**
   * 按钮尺寸
   * @default 'sm'
   */
  size?: 'default' | 'sm' | 'lg'
  
  /**
   * 图标
   */
  icon?: React.ReactNode
}
```

##### 3.2.4 LanguageSwitcher组件Props

```typescript
/**
 * LanguageSwitcher组件属性
 * @component LanguageSwitcher
 */
export interface LanguageSwitcherProps {
  /**
   * 当前语言
   */
  currentLocale: Locale
  
  /**
   * 语言切换回调
   */
  onLocaleChange: (locale: Locale) => void
  
  /**
   * 可用语言列表
   * @default ['zh', 'en']
   */
  availableLocales?: Locale[]
  
  /**
   * 语言显示名称映射
   */
  localeNames?: Record<Locale, string>
  
  /**
   * 语言标志映射
   */
  localeFlags?: Record<Locale, string>
  
  /**
   * 显示模式
   * @default 'dropdown'
   */
  mode?: 'dropdown' | 'tabs' | 'buttons'
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * LanguageSwitcher默认Props
 */
export const languageSwitcherDefaultProps: Partial<LanguageSwitcherProps> = {
  availableLocales: ['zh', 'en'],
  localeNames: {
    zh: '中文',
    en: 'English'
  },
  localeFlags: {
    zh: '🇨🇳',
    en: '🇺🇸'
  },
  mode: 'dropdown'
}
```

##### 3.2.5 Pricing组件Props

```typescript
/**
 * PricingCard组件属性
 * @component PricingCard
 */
export interface PricingCardProps {
  /**
   * 计划名称
   */
  name: string
  
  /**
   * 计划描述
   */
  description: string
  
  /**
   * 价格
   */
  price: number
  
  /**
   * 货币
   * @default 'USD'
   */
  currency?: Currency
  
  /**
   * 计费周期
   * @default 'month'
   */
  period?: 'month' | 'year'
  
  /**
   * 年付价格
   */
  yearlyPrice?: number
  
  /**
   * 功能列表
   */
  features: string[]
  
  /**
   * 按钮文本
   */
  buttonText: string
  
  /**
   * 按钮点击回调
   */
  onButtonClick?: () => void
  
  /**
   * 是否为热门计划
   * @default false
   */
  isPopular?: boolean
  
  /**
   * 热门标签文本
   */
  popularLabel?: string
  
  /**
   * 是否禁用
   * @default false
   */
  disabled?: boolean
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * Pricing组件属性
 * @component Pricing
 */
export interface PricingProps {
  /**
   * 标题
   */
  title: string
  
  /**
   * 描述
   */
  description: string
  
  /**
   * 定价计划列表
   */
  plans: PricingCardProps[]
  
  /**
   * 是否显示年付切换
   * @default true
   */
  showYearlyToggle?: boolean
  
  /**
   * 当前计费周期
   */
  currentPeriod?: 'month' | 'year'
  
  /**
   * 计费周期切换回调
   */
  onPeriodChange?: (period: 'month' | 'year') => void
  
  /**
   * 自定义样式类名
   */
  className?: string
}
```

##### 3.2.6 SplineScene组件Props

```typescript
/**
 * SplineScene组件属性
 * @component SplineScene
 */
export interface SplineSceneProps {
  /**
   * Spline场景URL
   */
  scene: string
  
  /**
   * 容器宽度
   * @default '100%'
   */
  width?: number | string
  
  /**
   * 容器高度
   * @default '100%'
   */
  height?: number | string
  
  /**
   * 是否自动播放
   * @default true
   */
  autoPlay?: boolean
  
  /**
   * 是否循环播放
   * @default true
   */
  loop?: boolean
  
  /**
   * 是否显示加载指示器
   * @default true
   */
  showLoader?: boolean
  
  /**
   * 加载成功回调
   */
  onLoad?: () => void
  
  /**
   * 加载错误回调
   */
  onError?: (error: Error) => void
  
  /**
   * 自定义样式类名
   */
  className?: string
}
```

##### 3.2.7 动画组件Props

```typescript
/**
 * Spotlight组件属性
 * @component Spotlight
 */
export interface SpotlightProps {
  /**
   * 聚光灯填充颜色
   * @default 'white'
   */
  fill?: string
  
  /**
   * 聚光灯大小
   * @default 400
   */
  size?: number
  
  /**
   * 聚光灯X位置
   * @default 0
   */
  x?: number
  
  /**
   * 聚光灯Y位置
   * @default 0
   */
  y?: number
  
  /**
   * 聚光灯透明度
   * @default 0.5
   */
  opacity?: number
  
  /**
   * 是否跟随鼠标
   * @default false
   */
  followMouse?: boolean
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * SparklesCore组件属性
 * @component SparklesCore
 */
export interface SparklesProps {
  /**
   * 粒子ID
   */
  id?: string
  
  /**
   * 背景颜色
   * @default 'transparent'
   */
  background?: string
  
  /**
   * 最小粒子大小
   * @default 0.6
   */
  minSize?: number
  
  /**
   * 最大粒子大小
   * @default 1.4
   */
  maxSize?: number
  
  /**
   * 粒子密度
   * @default 100
   */
  particleDensity?: number
  
  /**
   * 粒子颜色
   * @default '#FFFFFF'
   */
  particleColor?: string
  
  /**
   * 粒子速度
   * @default 0.8
   */
  speed?: number
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * AnimatedGradientBackground组件属性
 * @component AnimatedGradientBackground
 */
export interface AnimatedGradientBackgroundProps {
  /**
   * 是否启用呼吸效果
   * @default true
   */
  Breathing?: boolean
  
  /**
   * 渐变颜色列表
   */
  gradientColors?: string[]
  
  /**
   * 渐变停止位置
   */
  gradientStops?: number[]
  
  /**
   * 动画持续时间（秒）
   * @default 15
   */
  duration?: number
  
  /**
   * 自定义样式类名
   */
  className?: string
}
```

##### 3.2.8 BentoGrid组件Props

```typescript
/**
 * BentoCard组件属性
 * @component BentoCard
 */
export interface BentoCardProps {
  /**
   * 卡片名称
   */
  name: string
  
  /**
   * 卡片描述
   */
  description: string
  
  /**
   * 卡片背景
   */
  background?: React.ReactNode
  
  /**
   * 卡片图标组件
   */
  Icon?: React.ComponentType<{ className?: string }>
  
  /**
   * 卡片链接地址
   */
  href?: string
  
  /**
   * CTA按钮文本
   */
  cta?: string
  
  /**
   * 是否新窗口打开
   * @default false
   */
  external?: boolean
  
  /**
   * 自定义样式类名
   */
  className?: string
}

/**
 * BentoGrid组件属性
 * @component BentoGrid
 */
export interface BentoGridProps {
  /**
   * 网格列数
   * @default 3
   */
  columns?: number
  
  /**
   * 网格行数
   * @default 3
   */
  rows?: number
  
  /**
   * 卡片间距
   * @default '1rem'
   */
  gap?: string
  
  /**
   * 自定义样式类名
   */
  className?: string
  
  /**
   * 子元素
   */
  children: React.ReactNode
}
```

#### 3.3 Props验证最佳实践

##### 3.3.1 TypeScript严格模式

**启用严格类型检查**：
```typescript
{
  "strict": true,
  "strictNullChecks": true,
  "strictFunctionTypes": true,
  "strictBindCallApply": true,
  "strictPropertyInitialization": true,
  "noImplicitAny": true,
  "noImplicitThis": true
}
```

##### 3.3.2 Props类型推导

**使用泛型提高类型复用性**：
```typescript
interface BaseProps<T extends React.ElementType> {
  as?: T
  className?: string
}

type Props<T extends React.ElementType> = BaseProps<T> & React.ComponentPropsWithoutRef<T>
```

##### 3.3.3 Props默认值处理

**使用默认值模式**：
```typescript
interface ComponentProps {
  value?: string
  onChange?: (value: string) => void
}

const defaultProps: Partial<ComponentProps> = {
  value: '',
  onChange: () => {}
}

const useComponentProps = (props: ComponentProps): Required<Pick<ComponentProps, 'value'>> & Omit<ComponentProps, 'value'> => {
  return {
    ...defaultProps,
    ...props,
    value: props.value ?? defaultProps.value!
  }
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
