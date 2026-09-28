---
@file: 076-YYC3-AI-LANDING-类型定义-前端-请求响应数据类型.md
@description: YYC3-AI-LANDING 前端接口请求与响应数据的类型定义，保障前后端数据一致性
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [类型定义],[前端],[接口数据]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 076-YYC3-AI-LANDING-类型定义

## 概述

本文档详细描述YYC3-AI-LANDING-类型定义-前端-请求响应数据类型相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范前端-请求响应数据类型相关的业务标准与技术落地要求
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

### 3. 前端-请求响应数据类型

#### 3.1 请求类型定义

##### 3.1.1 基础请求类型

```typescript
/**
 * 基础请求配置
 */
export interface BaseRequestConfig {
  /**
   * 请求超时时间（毫秒）
   * @default 30000
   */
  timeout?: number
  
  /**
   * 是否携带凭证
   * @default 'include'
   */
  credentials?: 'include' | 'same-origin' | 'omit'
  
  /**
   * 请求头
   */
  headers?: Record<string, string>
  
  /**
   * 请求取消令牌
   */
  signal?: AbortSignal
}

/**
 * 查询参数类型
 */
export interface QueryParams {
  [key: string]: string | number | boolean | undefined | null | (string | number | boolean)[]
}

/**
 * 分页查询参数
 */
export interface PaginationQueryParams extends QueryParams {
  /**
   * 页码
   * @default 1
   */
  page?: number
  
  /**
   * 每页数量
   * @default 20
   */
  pageSize?: number
  
  /**
   * 排序字段
   */
  sortBy?: string
  
  /**
   * 排序方向
   * @default 'desc'
   */
  sortOrder?: 'asc' | 'desc'
}

/**
 * 排序查询参数
 */
export interface SortQueryParams {
  /**
   * 排序字段
   */
  sortBy?: string
  
  /**
   * 排序方向
   * @default 'desc'
   */
  sortOrder?: 'asc' | 'desc'
}

/**
 * 筛选查询参数
 */
export interface FilterQueryParams {
  /**
   * 筛选条件
   */
  filters?: Record<string, any>
  
  /**
   * 搜索关键词
   */
  search?: string
  
  /**
   * 时间范围
   */
  dateRange?: {
    start?: DateString
    end?: DateString
  }
}
```

##### 3.1.2 首页请求类型

```typescript
/**
 * 获取首页配置请求参数
 */
export interface GetHomeConfigRequest {
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 获取首页统计数据请求参数
 */
export interface GetHomeMetricsRequest {
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 获取首页评价请求参数
 */
export interface GetHomeTestimonialsRequest {
  /**
   * 语言代码
   */
  locale?: Locale
  
  /**
   * 是否只显示精选评价
   */
  featured?: boolean
  
  /**
   * 数量限制
   */
  limit?: number
}
```

##### 3.1.3 服务请求类型

```typescript
/**
 * 获取服务列表请求参数
 */
export interface GetServicesRequest extends PaginationQueryParams, FilterQueryParams {
  /**
   * 服务分类
   */
  category?: ServiceCategory
  
  /**
   * 服务状态
   */
  status?: ServiceStatus
  
  /**
   * 是否只显示精选服务
   */
  featured?: boolean
  
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 获取服务详情请求参数
 */
export interface GetServiceDetailRequest {
  /**
   * 服务ID或Slug
   */
  idOrSlug: string
  
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 获取服务分类请求参数
 */
export interface GetServiceCategoriesRequest {
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 获取服务FAQ请求参数
 */
export interface GetServiceFAQsRequest {
  /**
   * 服务ID
   */
  serviceId: ID
  
  /**
   * FAQ分类
   */
  category?: string
  
  /**
   * 语言代码
   */
  locale?: Locale
}
```

##### 3.1.4 联系请求类型

```typescript
/**
 * 提交联系表单请求
 */
export interface SubmitContactFormRequest {
  /**
   * 姓名
   */
  name: string
  
  /**
   * 邮箱
   */
  email: Email
  
  /**
   * 公司
   */
  company?: string
  
  /**
   * 电话
   */
  phone?: PhoneNumber
  
  /**
   * 感兴趣的服务
   */
  interestedServices?: ServiceCategory[]
  
  /**
   * 消息内容
   */
  message: string
  
  /**
   * 预约时间
   */
  preferredTime?: DateString
  
  /**
   * 语言代码
   */
  locale?: Locale
}

/**
 * 预约咨询请求
 */
export interface BookConsultationRequest {
  /**
   * 姓名
   */
  name: string
  
  /**
   * 邮箱
   */
  email: Email
  
  /**
   * 公司
   */
  company?: string
  
  /**
   * 电话
   */
  phone?: PhoneNumber
  
  /**
   * 感兴趣的服务
   */
  interestedServices?: ServiceCategory[]
  
  /**
   * 预约时间
   */
  preferredTime: DateString
  
  /**
   * 备注
   */
  notes?: string
  
  /**
   * 语言代码
   */
  locale?: Locale
}
```

##### 3.1.5 国际化请求类型

```typescript
/**
 * 获取翻译请求参数
 */
export interface GetTranslationsRequest {
  /**
   * 语言代码
   */
  locale: Locale
  
  /**
   * 命名空间
   */
  namespace?: string
}

/**
 * 切换语言请求参数
 */
export interface SwitchLocaleRequest {
  /**
   * 目标语言
   */
  locale: Locale
  
  /**
   * 是否保存到本地存储
   * @default true
   */
  persist?: boolean
}
```

#### 3.2 响应类型定义

##### 3.2.1 基础响应类型

```typescript
/**
 * 成功响应
 */
export interface SuccessResponse<T = any> {
  /**
   * 是否成功
   */
  success: true
  
  /**
   * 响应数据
   */
  data: T
  
  /**
   * 响应消息
   */
  message?: string
  
  /**
   * 响应时间戳
   */
  timestamp: Timestamp
  
  /**
   * 请求ID
   */
  requestId?: string
}

/**
 * 错误响应
 */
export interface ErrorResponse {
  /**
   * 是否成功
   */
  success: false
  
  /**
   * 错误信息
   */
  error: {
    /**
     * 错误码
     */
    code: string
    
    /**
     * 错误消息
     */
    message: string
    
    /**
     * 英文错误消息
     */
    message_en?: string
    
    /**
     * 错误详情
     */
    details?: Record<string, any>
    
    /**
     * 解决建议
     */
    suggestion?: string
    
    /**
     * 堆栈信息（仅开发环境）
     */
    stack?: string
  }
  
  /**
   * 响应时间戳
   */
  timestamp: Timestamp
  
  /**
   * 请求ID
   */
  requestId?: string
}

/**
 * API响应联合类型
 */
export type ApiResponse<T = any> = SuccessResponse<T> | ErrorResponse

/**
 * 分页响应数据
 */
export interface PaginatedResponse<T> {
  /**
   * 数据列表
   */
  items: T[]
  
  /**
   * 分页信息
   */
  pagination: PaginationResponse
  
  /**
   * 总数
   */
  total: number
}
```

##### 3.2.2 首页响应类型

```typescript
/**
 * 首页配置响应数据
 */
export interface HomeConfigData {
  /**
   * Hero区域配置
   */
  hero: {
    title: string
    subtitle: string
    ctaPrimary: string
    ctaSecondary: string
    badge1: string
    badge2: string
  }
  
  /**
   * 问题与解决方案配置
   */
  problemSolution: {
    problemTitle: string
    problems: string[]
    solutionTitle: string
    solutions: string[]
  }
  
  /**
   * 服务区域配置
   */
  services: {
    title: string
    subtitle: string
  }
  
  /**
   * 评价区域配置
   */
  testimonials: {
    title: string
  }
  
  /**
   * 指标区域配置
   */
  metrics: {
    title: string
    subtitle: string
    timeSaved: string
    roi: string
    conversion: string
    support: string
  }
  
  /**
   * 定价区域配置
   */
  pricing: {
    title: string
    description: string
  }
  
  /**
   * 流程区域配置
   */
  process: {
    title: string
    subtitle: string
  }
  
  /**
   * CTA区域配置
   */
  cta: {
    title: string
    buttonPrimary: string
    buttonSecondary: string
  }
  
  /**
   * 页脚配置
   */
  footer: {
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
}

/**
 * 首页统计数据
 */
export interface HomeMetricsData {
  /**
   * 节省时间（小时）
   */
  timeSaved: number
  
  /**
   * 投资回报率（%）
   */
  roi: number
  
  /**
   * 转化率提升（%）
   */
  conversion: number
  
  /**
   * 客户满意度（%）
   */
  satisfaction: number
  
  /**
   * 服务客户数
   */
  clients: number
  
  /**
   * 成功项目数
   */
  projects: number
}

/**
 * 首页评价列表
 */
export interface HomeTestimonialsData {
  /**
   * 评价列表
   */
  testimonials: Testimonial[]
}
```

##### 3.2.3 服务响应类型

```typescript
/**
 * 服务列表响应数据
 */
export type ServicesListResponse = PaginatedResponse<Service>

/**
 * 服务详情响应数据
 */
export type ServiceDetailResponse = ServiceDetail

/**
 * 服务分类响应数据
 */
export interface ServiceCategoryData {
  /**
   * 分类代码
   */
  code: ServiceCategory
  
  /**
   * 分类名称
   */
  name: string
  
  /**
   * 分类名称（英文）
   */
  nameEn: string
  
  /**
   * 分类描述
   */
  description: string
  
  /**
   * 分类描述（英文）
   */
  descriptionEn: string
  
  /**
   * 分类图标
   */
  icon: IconName
  
  /**
   * 服务数量
   */
  count: number
}

/**
 * 服务分类列表响应
 */
export type ServiceCategoriesResponse = ServiceCategoryData[]

/**
 * 服务FAQ响应数据
 */
export type ServiceFAQsResponse = FAQ[]
```

##### 3.2.4 联系响应类型

```typescript
/**
 * 联系表单提交响应数据
 */
export interface ContactFormSubmitData {
  /**
   * 提交ID
   */
  id: ID
  
  /**
   * 提交状态
   */
  status: 'pending' | 'processing' | 'completed'
  
  /**
   * 预计回复时间
   */
  estimatedResponseTime: string
}

/**
 * 预约咨询响应数据
 */
export interface ConsultationBookingData {
  /**
   * 预约ID
   */
  id: ID
  
  /**
   * 预约状态
   */
  status: 'pending' | 'confirmed' | 'cancelled'
  
  /**
   * 预约时间
   */
  scheduledTime: DateString
  
  /**
   * 会议链接（如果在线）
   */
  meetingLink?: URL
  
  /**
   * 联系方式
   */
  contactInfo?: {
    email: Email
    phone?: PhoneNumber
  }
}
```

##### 3.2.5 国际化响应类型

```typescript
/**
 * 翻译数据
 */
export interface TranslationsData {
  /**
   * 语言代码
   */
  locale: Locale
  
  /**
   * 翻译字典
   */
  translations: Translations
  
  /**
   * 最后更新时间
   */
  lastUpdated: Timestamp
}

/**
 * 语言切换响应数据
 */
export interface LocaleSwitchData {
  /**
   * 当前语言
   */
  currentLocale: Locale
  
  /**
   * 前一个语言
   */
  previousLocale: Locale
  
  /**
   * 切换时间
   */
  switchedAt: Timestamp
}
```

#### 3.3 请求/响应工具类型

##### 3.3.1 请求方法类型

```typescript
/**
 * HTTP请求方法
 */
export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE' | 'HEAD' | 'OPTIONS'

/**
 * 请求配置
 */
export interface RequestConfig<T = any> extends BaseRequestConfig {
  /**
   * 请求方法
   */
  method: HttpMethod
  
  /**
   * 请求URL
   */
  url: string
  
  /**
   * 请求体
   */
  body?: T
  
  /**
   * 查询参数
   */
  params?: QueryParams
}
```

##### 3.3.2 API客户端类型

```typescript
/**
 * API客户端接口
 */
export interface ApiClient {
  /**
   * GET请求
   */
  get<T = any, P = QueryParams>(url: string, params?: P, config?: BaseRequestConfig): Promise<ApiResponse<T>>
  
  /**
   * POST请求
   */
  post<T = any, B = any>(url: string, body?: B, config?: BaseRequestConfig): Promise<ApiResponse<T>>
  
  /**
   * PUT请求
   */
  put<T = any, B = any>(url: string, body?: B, config?: BaseRequestConfig): Promise<ApiResponse<T>>
  
  /**
   * PATCH请求
   */
  patch<T = any, B = any>(url: string, body?: B, config?: BaseRequestConfig): Promise<ApiResponse<T>>
  
  /**
   * DELETE请求
   */
  delete<T = any, P = QueryParams>(url: string, params?: P, config?: BaseRequestConfig): Promise<ApiResponse<T>>
  
  /**
   * 请求拦截器
   */
  setRequestInterceptor(interceptor: (config: RequestConfig) => RequestConfig | Promise<RequestConfig>): void
  
  /**
   * 响应拦截器
   */
  setResponseInterceptor(interceptor: (response: ApiResponse) => ApiResponse | Promise<ApiResponse>): void
  
  /**
   * 错误拦截器
   */
  setErrorInterceptor(interceptor: (error: ErrorResponse) => ErrorResponse | Promise<ErrorResponse>): void
}
```

##### 3.3.3 类型守卫

```typescript
/**
 * 检查是否为成功响应
 */
export function isSuccessResponse<T>(response: ApiResponse<T>): response is SuccessResponse<T> {
  return response.success === true
}

/**
 * 检查是否为错误响应
 */
export function isErrorResponse(response: ApiResponse<any>): response is ErrorResponse {
  return response.success === false
}

/**
 * 从响应中提取数据
 */
export function extractData<T>(response: ApiResponse<T>): T | null {
  if (isSuccessResponse(response)) {
    return response.data
  }
  return null
}

/**
 * 从响应中提取错误
 */
export function extractError(response: ApiResponse<any>): Error | null {
  if (isErrorResponse(response)) {
    return new Error(response.error.message)
  }
  return null
}
```

#### 3.4 错误类型定义

##### 3.4.1 错误码类型

```typescript
/**
 * 错误码类型
 */
export type ErrorCode = 
  | 'COMMON_INVALID_PARAMS'
  | 'COMMON_NOT_FOUND'
  | 'COMMON_UNAUTHORIZED'
  | 'COMMON_FORBIDDEN'
  | 'COMMON_SERVER_ERROR'
  | 'COMMON_RATE_LIMIT'
  | 'COMMON_TIMEOUT'
  | 'SERVICE_NOT_FOUND'
  | 'SERVICE_INACTIVE'
  | 'VALIDATION_EMAIL_INVALID'
  | 'VALIDATION_PHONE_INVALID'
  | 'VALIDATION_REQUIRED_FIELD'
  | 'AUTH_TOKEN_EXPIRED'
  | 'AUTH_TOKEN_INVALID'
  | 'AUTH_LOGIN_FAILED'
  | 'EXTERNAL_SERVICE_UNAVAILABLE'
```

##### 3.4.2 错误类型

```typescript
/**
 * API错误类
 */
export class ApiError extends Error {
  /**
   * 错误码
   */
  code: ErrorCode
  
  /**
   * 错误详情
   */
  details?: Record<string, any>
  
  /**
   * 解决建议
   */
  suggestion?: string
  
  /**
   * HTTP状态码
   */
  statusCode?: number
  
  /**
   * 请求ID
   */
  requestId?: string
  
  constructor(
    message: string,
    code: ErrorCode,
    details?: Record<string, any>,
    suggestion?: string,
    statusCode?: number,
    requestId?: string
  ) {
    super(message)
    this.name = 'ApiError'
    this.code = code
    this.details = details
    this.suggestion = suggestion
    this.statusCode = statusCode
    this.requestId = requestId
  }
}

/**
 * 网络错误类
 */
export class NetworkError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'NetworkError'
  }
}

/**
 * 超时错误类
 */
export class TimeoutError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'TimeoutError'
  }
}

/**
 * 验证错误类
 */
export class ValidationError extends Error {
  /**
   * 验证字段
   */
  field?: string
  
  /**
   * 验证规则
   */
  rule?: string
  
  constructor(message: string, field?: string, rule?: string) {
    super(message)
    this.name = 'ValidationError'
    this.field = field
    this.rule = rule
  }
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
