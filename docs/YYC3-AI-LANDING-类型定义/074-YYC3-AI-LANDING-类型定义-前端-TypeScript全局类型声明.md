---
@file: 074-YYC3-AI-LANDING-类型定义-前端-TypeScript全局类型声明.md
@description: YYC3-AI-LANDING 前端TS全局公共类型、接口、枚举的统一声明与约束
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [类型定义],[前端],[TypeScript]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 074-YYC3-AI-LANDING-类型定义

## 概述

本文档详细描述YYC3-AI-LANDING-类型定义-前端-TypeScript全局类型声明相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范前端-TypeScript全局类型声明相关的业务标准与技术落地要求
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

### 3. 前端-TypeScript全局类型声明

#### 3.1 基础类型定义

##### 3.1.1 通用类型

```typescript
/**
 * 基础ID类型
 */
export type ID = string

/**
 * 时间戳类型
 */
export type Timestamp = string

/**
 * 日期类型
 */
export type DateString = string

/**
 * URL类型
 */
export type URL = string

/**
 * 邮箱类型
 */
export type Email = string

/**
 * 手机号类型
 */
export type PhoneNumber = string

/**
 * 货币类型
 */
export type Currency = 'USD' | 'CNY' | 'EUR' | 'GBP' | 'JPY'

/**
 * 语言类型
 */
export type Locale = 'zh' | 'en' | 'zh-CN' | 'en-US'

/**
 * 时区类型
 */
export type TimeZone = string

/**
 * 状态类型
 */
export type Status = 'active' | 'inactive' | 'pending' | 'archived'

/**
 * 排序方向
 */
export type SortOrder = 'asc' | 'desc'

/**
 * 分页参数
 */
export interface PaginationParams {
  page: number
  pageSize: number
  sortBy?: string
  sortOrder?: SortOrder
}

/**
 * 分页响应
 */
export interface PaginationResponse {
  page: number
  pageSize: number
  total: number
  totalPages: number
  hasNext: boolean
  hasPrevious: boolean
}

/**
 * API响应基础类型
 */
export interface ApiResponse<T = any> {
  success: boolean
  data?: T
  message?: string
  timestamp: Timestamp
  requestId?: string
}

/**
 * API错误响应
 */
export interface ApiErrorResponse {
  success: false
  error: {
    code: string
    message: string
    message_en?: string
    details?: Record<string, any>
    suggestion?: string
  }
  timestamp: Timestamp
  requestId?: string
}
```

##### 3.1.2 国际化类型

```typescript
/**
 * 翻译字典
 */
export interface Translations {
  nav: NavTranslations
  hero: HeroTranslations
  problemSolution: ProblemSolutionTranslations
  services: ServicesTranslations
  testimonials: TestimonialsTranslations
  metrics: MetricsTranslations
  pricing: PricingTranslations
  process: ProcessTranslations
  cta: CTATranslations
  footer: FooterTranslations
}

/**
 * 导航栏翻译
 */
export interface NavTranslations {
  services: string
  testimonials: string
  pricing: string
  contact: string
}

/**
 * Hero区域翻译
 */
export interface HeroTranslations {
  title: string
  subtitle: string
  ctaPrimary: string
  ctaSecondary: string
  badge1: string
  badge2: string
}

/**
 * 问题与解决方案翻译
 */
export interface ProblemSolutionTranslations {
  problemTitle: string
  problem1: string
  problem2: string
  problem3: string
  problem4: string
  solutionTitle: string
  solution1: string
  solution2: string
  solution3: string
  solution4: string
}

/**
 * 服务翻译
 */
export interface ServicesTranslations {
  title: string
  subtitle: string
  chatbot: ServiceItemTranslations
  workflow: ServiceItemTranslations
  integration: ServiceItemTranslations
  analytics: ServiceItemTranslations
  custom: ServiceItemTranslations
}

/**
 * 服务项翻译
 */
export interface ServiceItemTranslations {
  name: string
  description: string
  cta: string
}

/**
 * 客户评价翻译
 */
export interface TestimonialsTranslations {
  title: string
  testimonial1: TestimonialItemTranslations
  testimonial2: TestimonialItemTranslations
  testimonial3: TestimonialItemTranslations
}

/**
 * 评价项翻译
 */
export interface TestimonialItemTranslations {
  content: string
  name: string
  title: string
}

/**
 * 数据指标翻译
 */
export interface MetricsTranslations {
  title: string
  subtitle: string
  timeSaved: string
  roi: string
  conversion: string
  support: string
}

/**
 * 定价翻译
 */
export interface PricingTranslations {
  title: string
  description: string
  starter: PricingPlanTranslations
  professional: PricingPlanTranslations
  enterprise: PricingPlanTranslations
}

/**
 * 定价计划翻译
 */
export interface PricingPlanTranslations {
  name: string
  description: string
  buttonText: string
  features: string[]
}

/**
 * 流程翻译
 */
export interface ProcessTranslations {
  title: string
  subtitle: string
  step1: ProcessStepTranslations
  step2: ProcessStepTranslations
  step3: ProcessStepTranslations
}

/**
 * 流程步骤翻译
 */
export interface ProcessStepTranslations {
  title: string
  description: string
}

/**
 * CTA翻译
 */
export interface CTATranslations {
  title: string
  buttonPrimary: string
  buttonSecondary: string
}

/**
 * 页脚翻译
 */
export interface FooterTranslations {
  description: string
  servicesTitle: string
  companyTitle: string
  contactTitle: string
  aboutUs: string
  caseStudies: string
  blog: string
  careers: string
  contact: string
  email: string
  phone: string
  address: string
  copyright: string
  privacy: string
  terms: string
}
```

##### 3.1.3 媒体类型

```typescript
/**
 * 图片类型
 */
export interface Image {
  url: URL
  alt: string
  width?: number
  height?: number
  mimeType?: string
}

/**
 * 视频类型
 */
export interface Video {
  url: URL
  thumbnail?: Image
  duration?: number
  mimeType?: string
}

/**
 * 图标类型
 */
export type IconName = 
  | 'Bot'
  | 'Workflow'
  | 'Cog'
  | 'Brain'
  | 'MessageSquare'
  | 'Clock'
  | 'DollarSign'
  | 'BarChart3'
  | 'TrendingUp'
  | 'CheckCircle'
  | 'ArrowRight'
  | 'Linkedin'
  | 'Twitter'
  | 'Facebook'
  | 'Mail'
  | 'Phone'
  | 'MapPin'
```

##### 3.1.4 主题类型

```typescript
/**
 * 主题模式
 */
export type ThemeMode = 'light' | 'dark' | 'system'

/**
 * 主题颜色
 */
export interface ThemeColors {
  primary: string
  secondary: string
  accent: string
  background: string
  foreground: string
  muted: string
  border: string
}

/**
 * 主题配置
 */
export interface ThemeConfig {
  mode: ThemeMode
  colors: ThemeColors
  radius: string
  fontSize: string
}
```

#### 3.2 业务类型定义

##### 3.2.1 服务类型

```typescript
/**
 * 服务分类
 */
export type ServiceCategory = 
  | 'chatbot'
  | 'workflow'
  | 'integration'
  | 'analytics'
  | 'custom'

/**
 * 服务状态
 */
export type ServiceStatus = 'active' | 'inactive' | 'coming-soon'

/**
 * 服务类型
 */
export interface Service {
  id: ID
  name: string
  nameEn: string
  slug: string
  category: ServiceCategory
  description: string
  descriptionEn: string
  icon: IconName
  features: string[]
  status: ServiceStatus
  featured: boolean
  order: number
  createdAt: Timestamp
  updatedAt: Timestamp
}

/**
 * 服务详情
 */
export interface ServiceDetail extends Service {
  longDescription?: string
  longDescriptionEn?: string
  thumbnail?: Image
  banner?: Image
  benefits: string[]
  useCases: UseCase[]
  pricing: ServicePricing
  testimonials?: Testimonial[]
  faqs?: FAQ[]
  cta?: ServiceCTA
  seo?: ServiceSEO
}

/**
 * 用例
 */
export interface UseCase {
  title: string
  description: string
  icon?: IconName
}

/**
 * 服务定价
 */
export interface ServicePricing {
  starter: PricingPlan
  professional: PricingPlan
  enterprise: PricingPlan
}

/**
 * 定价计划
 */
export interface PricingPlan {
  name: string
  nameEn: string
  price: number
  currency: Currency
  period: 'month' | 'year'
  yearlyPrice?: number
  isPopular?: boolean
  features: string[]
}

/**
 * 服务CTA
 */
export interface ServiceCTA {
  primary: string
  primaryEn: string
  secondary: string
  secondaryEn: string
}

/**
 * 服务SEO
 */
export interface ServiceSEO {
  title: string
  description: string
  keywords: string[]
}
```

##### 3.2.2 评价类型

```typescript
/**
 * 客户评价
 */
export interface Testimonial {
  id: ID
  content: string
  author: TestimonialAuthor
  rating: number
  featured: boolean
  createdAt: Timestamp
}

/**
 * 评价作者
 */
export interface TestimonialAuthor {
  name: string
  title: string
  company: string
  avatar?: Image
}
```

##### 3.2.3 FAQ类型

```typescript
/**
 * 常见问题
 */
export interface FAQ {
  id: ID
  question: string
  answer: string
  category?: string
  order?: number
}
```

#### 3.3 组件类型定义

##### 3.3.1 按钮组件类型

```typescript
/**
 * 按钮变体
 */
export type ButtonVariant = 
  | 'default'
  | 'destructive'
  | 'outline'
  | 'secondary'
  | 'ghost'
  | 'link'

/**
 * 按钮尺寸
 */
export type ButtonSize = 'default' | 'sm' | 'lg' | 'icon'

/**
 * 按钮属性
 */
export interface ButtonProps extends React.ComponentProps<'button'> {
  variant?: ButtonVariant
  size?: ButtonSize
  asChild?: boolean
  className?: string
}
```

##### 3.3.2 卡片组件类型

```typescript
/**
 * 卡片属性
 */
export interface CardProps extends React.ComponentProps<'div'> {
  className?: string
}

/**
 * 卡片内容属性
 */
export interface CardContentProps extends React.ComponentProps<'div'> {
  className?: string
}

/**
 * 卡片头部属性
 */
export interface CardHeaderProps extends React.ComponentProps<'div'> {
  className?: string
}

/**
 * 卡片标题属性
 */
export interface CardTitleProps extends React.ComponentProps<'h3'> {
  className?: string
}
```

##### 3.3.3 导航栏组件类型

```typescript
/**
 * 导航栏属性
 */
export interface NavbarProps {
  className?: string
  logo?: Image
  links?: NavLink[]
  actions?: NavbarAction[]
}

/**
 * 导航链接
 */
export interface NavLink {
  label: string
  href: string
  external?: boolean
}

/**
 * 导航栏操作
 */
export interface NavbarAction {
  label: string
  onClick: () => void
  variant?: ButtonVariant
}
```

##### 3.3.4 语言切换器类型

```typescript
/**
 * 语言切换器属性
 */
export interface LanguageSwitcherProps {
  currentLocale: Locale
  onLocaleChange: (locale: Locale) => void
  availableLocales?: Locale[]
  className?: string
}
```

##### 3.3.5 定价组件类型

```typescript
/**
 * 定价卡片属性
 */
export interface PricingCardProps {
  name: string
  description: string
  price: number
  currency: Currency
  period: 'month' | 'year'
  yearlyPrice?: number
  features: string[]
  buttonText: string
  onButtonClick?: () => void
  isPopular?: boolean
  className?: string
}

/**
 * 定价组件属性
 */
export interface PricingProps {
  title: string
  description: string
  plans: PricingCardProps[]
  className?: string
}
```

##### 3.3.6 3D场景组件类型

```typescript
/**
 * Spline场景属性
 */
export interface SplineSceneProps {
  scene: URL
  className?: string
  width?: number | string
  height?: number | string
  onLoad?: () => void
  onError?: (error: Error) => void
}
```

##### 3.3.7 动画组件类型

```typescript
/**
 * 聚光灯效果属性
 */
export interface SpotlightProps {
  className?: string
  fill?: string
}

/**
 * 粒子效果属性
 */
export interface SparklesProps {
  id?: string
  background?: string
  minSize?: number
  maxSize?: number
  particleDensity?: number
  className?: string
  particleColor?: string
  speed?: number
}

/**
 * 渐变背景属性
 */
export interface AnimatedGradientBackgroundProps {
  Breathing?: boolean
  gradientColors?: string[]
  gradientStops?: number[]
  className?: string
}
```

##### 3.3.8 Bento网格组件类型

```typescript
/**
 * Bento卡片属性
 */
export interface BentoCardProps {
  name: string
  className?: string
  background?: React.ReactNode
  Icon?: React.ComponentType<{ className?: string }>
  description: string
  href?: string
  cta?: string
}

/**
 * Bento网格属性
 */
export interface BentoGridProps {
  className?: string
  children: React.ReactNode
}
```

#### 3.4 工具类型定义

##### 3.4.1 类型守卫

```typescript
/**
 * 检查是否为有效的API响应
 */
export function isApiResponse<T>(response: any): response is ApiResponse<T> {
  return response && typeof response === 'object' && 'success' in response
}

/**
 * 检查是否为错误响应
 */
export function isApiErrorResponse(response: any): response is ApiErrorResponse {
  return response && typeof response === 'object' && response.success === false && 'error' in response
}

/**
 * 检查是否为有效的ID
 */
export function isValidId(id: any): id is ID {
  return typeof id === 'string' && id.length > 0
}

/**
 * 检查是否为有效的URL
 */
export function isValidUrl(url: any): url is URL {
  return typeof url === 'string' && (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('/'))
}

/**
 * 检查是否为有效的邮箱
 */
export function isValidEmail(email: any): email is Email {
  return typeof email === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}
```

##### 3.4.2 类型工具

```typescript
/**
 * 深度Partial
 */
export type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P]
}

/**
 * 深度Required
 */
export type DeepRequired<T> = {
  [P in keyof T]-?: T[P] extends object ? DeepRequired<T[P]> : T[P]
}

/**
 * 深度Readonly
 */
export type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P]
}

/**
 * 提取函数返回类型
 */
export type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any

/**
 * 提取Promise返回类型
 */
export type PromiseType<T extends Promise<any>> = T extends Promise<infer U> ? U : never

/**
 * 提取数组元素类型
 */
export type ArrayElement<T> = T extends (infer U)[] ? U : never

/**
 * 提取对象键类型
 */
export type Keys<T> = keyof T

/**
 * 提取对象值类型
 */
export type Values<T> = T[keyof T]

/**
 * 提取必需的键
 */
export type RequiredKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never
}[keyof T]

/**
 * 提取可选的键
 */
export type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? never : K
}[keyof T]

/**
 * 合并两个对象类型
 */
export type Merge<T, U> = Omit<T, keyof U> & U
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
