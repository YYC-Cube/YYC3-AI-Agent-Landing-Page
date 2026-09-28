---
@file: 060-YYC3-AI-LANDING-API文档-业务域-服务接口手册.md
@description: YYC3-AI-LANDING 服务展示相关接口的详细定义，包含入参、出参、调用示例
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [API接口],[业务域],[服务]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 060-YYC3-AI-LANDING-API文档

## 概述

本文档详细描述YYC3-AI-LANDING-API文档-业务域-服务接口手册相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范业务域-服务接口手册相关的业务标准与技术落地要求
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

### 3. 业务域-服务接口手册

#### 3.1 接口概述

YYC³ AI代理服务落地页的服务接口用于管理展示的AI服务信息，包括：
- 服务列表查询
- 服务详情获取
- 服务分类管理
- 服务特性管理
- 服务定价信息

由于本项目是静态落地页，服务信息通过前端配置管理。以下接口为未来CMS扩展预留。

#### 3.2 服务查询接口

##### 3.2.1 获取服务列表

**接口描述**：获取所有可用的AI服务列表，支持分页、筛选和排序。

**请求信息**：
```
GET /api/v1/services
```

**请求头**：
```http
Accept: application/json
Accept-Language: zh-CN
X-Request-ID: uuid-v4
```

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| page | number | 否 | 页码，默认1 | 1 |
| pageSize | number | 否 | 每页数量，默认20 | 20 |
| category | string | 否 | 服务分类 | chatbot, workflow, integration, analytics, custom |
| status | string | 否 | 服务状态 | active, inactive |
| featured | boolean | 否 | 是否精选 | true, false |
| sortBy | string | 否 | 排序字段 | createdAt, name, price |
| sortOrder | string | 否 | 排序方向 | asc, desc |
| locale | string | 否 | 语言代码 | zh-CN, en-US |

**请求示例**：
```bash
curl -X GET "https://api.yyc3.com/api/v1/services?page=1&pageSize=20&category=chatbot&status=active&sortBy=createdAt&sortOrder=desc&locale=zh-CN"
```

**成功响应**：
```json
{
  "success": true,
  "data": [
    {
      "id": "service-001",
      "name": "AI 聊天机器人与虚拟助手",
      "nameEn": "AI Chatbots & Virtual Assistants",
      "slug": "ai-chatbots",
      "category": "chatbot",
      "description": "智能对话代理，通过自然语言处理 7×24 小时处理客户支持、潜在客户筛选和销售咨询。",
      "descriptionEn": "Intelligent conversational agents that handle customer support, lead qualification, and sales inquiries 24/7 with natural language processing.",
      "icon": "Bot",
      "features": [
        "自然语言处理",
        "7×24小时支持",
        "多语言支持",
        "智能路由",
        "情感分析"
      ],
      "pricing": {
        "starter": {
          "price": 997,
          "currency": "USD",
          "period": "month"
        },
        "professional": {
          "price": 2497,
          "currency": "USD",
          "period": "month"
        },
        "enterprise": {
          "price": 4997,
          "currency": "USD",
          "period": "month"
        }
      },
      "status": "active",
      "featured": true,
      "order": 1,
      "createdAt": "2025-01-01T10:00:00.000Z",
      "updatedAt": "2025-01-23T10:00:00.000Z"
    },
    {
      "id": "service-002",
      "name": "工作流自动化",
      "nameEn": "Workflow Automation",
      "slug": "workflow-automation",
      "category": "workflow",
      "description": "简化重复流程，通过智能自动化系统消除手动任务，每周节省 20+ 小时。",
      "descriptionEn": "Streamline repetitive processes and eliminate manual tasks with intelligent automation systems that save 20+ hours per week.",
      "icon": "Workflow",
      "features": [
        "任务自动化",
        "流程可视化",
        "条件分支",
        "集成能力",
        "实时监控"
      ],
      "pricing": {
        "starter": {
          "price": 997,
          "currency": "USD",
          "period": "month"
        },
        "professional": {
          "price": 2497,
          "currency": "USD",
          "period": "month"
        },
        "enterprise": {
          "price": 4997,
          "currency": "USD",
          "period": "month"
        }
      },
      "status": "active",
      "featured": true,
      "order": 2,
      "createdAt": "2025-01-01T10:00:00.000Z",
      "updatedAt": "2025-01-23T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 5,
    "totalPages": 1,
    "hasNext": false,
    "hasPrevious": false
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

**错误响应**：
```json
{
  "success": false,
  "error": {
    "code": "COMMON_PARAM_INVALID",
    "message": "参数无效",
    "details": {
      "field": "category",
      "message": "无效的服务分类"
    }
  },
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

##### 3.2.2 获取服务详情

**接口描述**：根据服务ID获取单个服务的详细信息。

**请求信息**：
```
GET /api/v1/services/{serviceId}
```

**路径参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| serviceId | string | 是 | 服务ID | service-001 |

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| locale | string | 否 | 语言代码 | zh-CN, en-US |

**请求示例**：
```bash
curl -X GET "https://api.yyc3.com/api/v1/services/service-001?locale=zh-CN"
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "service-001",
    "name": "AI 聊天机器人与虚拟助手",
    "nameEn": "AI Chatbots & Virtual Assistants",
    "slug": "ai-chatbots",
    "category": {
      "id": "category-001",
      "name": "聊天机器人",
      "nameEn": "Chatbot",
      "slug": "chatbot"
    },
    "description": "智能对话代理，通过自然语言处理 7×24 小时处理客户支持、潜在客户筛选和销售咨询。",
    "descriptionEn": "Intelligent conversational agents that handle customer support, lead qualification, and sales inquiries 24/7 with natural language processing.",
    "longDescription": "我们的AI聊天机器人解决方案采用最先进的自然语言处理技术，能够理解用户意图并提供准确的响应。支持多语言对话，可以无缝集成到您的网站、社交媒体和消息平台。",
    "longDescriptionEn": "Our AI chatbot solution uses state-of-the-art natural language processing technology to understand user intent and provide accurate responses. Supports multilingual conversations and can be seamlessly integrated into your website, social media, and messaging platforms.",
    "icon": "Bot",
    "thumbnail": "/images/services/chatbot-thumbnail.jpg",
    "banner": "/images/services/chatbot-banner.jpg",
    "features": [
      {
        "id": "feature-001",
        "name": "自然语言处理",
        "nameEn": "Natural Language Processing",
        "description": "理解复杂查询并提供准确响应",
        "descriptionEn": "Understand complex queries and provide accurate responses",
        "icon": "MessageSquare"
      },
      {
        "id": "feature-002",
        "name": "7×24小时支持",
        "nameEn": "24/7 Support",
        "description": "全天候处理客户咨询",
        "descriptionEn": "Handle customer inquiries around the clock",
        "icon": "Clock"
      },
      {
        "id": "feature-003",
        "name": "多语言支持",
        "nameEn": "Multi-language Support",
        "description": "支持50+种语言",
        "descriptionEn": "Supports 50+ languages",
        "icon": "Globe"
      }
    ],
    "benefits": [
      "提高客户满意度",
      "降低运营成本",
      "增加潜在客户转化",
      "提升响应速度"
    ],
    "useCases": [
      {
        "title": "客户支持",
        "description": "自动回答常见问题，减少人工客服工作量"
      },
      {
        "title": "销售咨询",
        "description": "引导潜在客户，提供产品推荐"
      },
      {
        "title": "预约管理",
        "description": "自动安排预约和会议"
      }
    ],
    "pricing": {
      "starter": {
        "name": "入门版",
        "nameEn": "Starter",
        "price": 997,
        "currency": "USD",
        "period": "month",
        "yearlyPrice": 797,
        "features": [
          "客户支持 AI 聊天机器人",
          "基础工作流自动化（3 个流程）",
          "电子邮件集成",
          "标准分析仪表板",
          "电子邮件支持",
          "30 天退款保证"
        ]
      },
      "professional": {
        "name": "专业版",
        "nameEn": "Professional",
        "price": 2497,
        "currency": "USD",
        "period": "month",
        "yearlyPrice": 1997,
        "isPopular": true,
        "features": [
          "高级 AI 聊天机器人与潜在客户筛选",
          "完整工作流自动化（10+ 流程）",
          "CRM 与电子商务集成",
          "高级分析与报告",
          "优先电话与电子邮件支持",
          "定制 AI 训练",
          "每月优化咨询",
          "ROI 跟踪与报告"
        ]
      },
      "enterprise": {
        "name": "企业版",
        "nameEn": "Enterprise",
        "price": 4997,
        "currency": "USD",
        "period": "month",
        "yearlyPrice": 3997,
        "features": [
          "定制 AI 开发与部署",
          "无限工作流自动化",
          "完整系统集成",
          "专属 AI 策略师",
          "7×24 小时优先支持",
          "高级安全与合规",
          "白标解决方案",
          "季度业务审查",
          "定制培训与研讨会"
        ]
      }
    },
    "testimonials": [
      {
        "id": "testimonial-001",
        "content": "AI 聊天机器人使我们的潜在客户转化率提高了 200%。",
        "author": "Sarah Johnson",
        "company": "TechStart Solutions"
      }
    ],
    "faqs": [
      {
        "question": "AI聊天机器人如何学习我们的业务？",
        "answer": "我们使用您的文档、FAQ和过往对话记录来训练AI模型，确保它理解您的业务和产品。"
      },
      {
        "question": "支持哪些语言？",
        "answer": "我们的AI聊天机器人支持50多种语言，包括中文、英语、西班牙语、法语、德语等。"
      }
    ],
    "cta": {
      "primary": "开始免费试用",
      "primaryEn": "Start Free Trial",
      "secondary": "预约演示",
      "secondaryEn": "Book a Demo"
    },
    "status": "active",
    "featured": true,
    "order": 1,
    "seo": {
      "title": "AI聊天机器人服务 | YYC³ AI代理服务",
      "description": "专业的AI聊天机器人解决方案，提供7×24小时客户支持，提升客户满意度和转化率。",
      "keywords": ["AI聊天机器人", "虚拟助手", "客户支持", "自动化"]
    },
    "createdAt": "2025-01-01T10:00:00.000Z",
    "updatedAt": "2025-01-23T10:00:00.000Z"
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

**错误响应**：
```json
{
  "success": false,
  "error": {
    "code": "SERVICE_NOT_FOUND",
    "message": "服务不存在",
    "details": {
      "serviceId": "service-001"
    },
    "suggestion": "请检查服务ID是否正确"
  },
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.3 服务分类接口

##### 3.3.1 获取服务分类列表

**接口描述**：获取所有服务分类。

**请求信息**：
```
GET /api/v1/services/categories
```

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| locale | string | 否 | 语言代码 | zh-CN, en-US |

**成功响应**：
```json
{
  "success": true,
  "data": [
    {
      "id": "category-001",
      "name": "聊天机器人",
      "nameEn": "Chatbot",
      "slug": "chatbot",
      "description": "智能对话代理和虚拟助手",
      "descriptionEn": "Intelligent conversational agents and virtual assistants",
      "icon": "Bot",
      "order": 1,
      "serviceCount": 1
    },
    {
      "id": "category-002",
      "name": "工作流自动化",
      "nameEn": "Workflow Automation",
      "slug": "workflow",
      "description": "自动化业务流程和任务",
      "descriptionEn": "Automate business processes and tasks",
      "icon": "Workflow",
      "order": 2,
      "serviceCount": 1
    },
    {
      "id": "category-003",
      "name": "AI集成服务",
      "nameEn": "AI Integration",
      "slug": "integration",
      "description": "将AI功能集成到现有系统",
      "descriptionEn": "Integrate AI capabilities into existing systems",
      "icon": "Cog",
      "order": 3,
      "serviceCount": 1
    },
    {
      "id": "category-004",
      "name": "智能分析",
      "nameEn": "Smart Analytics",
      "slug": "analytics",
      "description": "数据分析和商业智能",
      "descriptionEn": "Data analytics and business intelligence",
      "icon": "Brain",
      "order": 4,
      "serviceCount": 1
    },
    {
      "id": "category-005",
      "name": "定制AI开发",
      "nameEn": "Custom AI Development",
      "slug": "custom",
      "description": "量身定制的AI解决方案",
      "descriptionEn": "Bespoke AI solutions",
      "icon": "MessageSquare",
      "order": 5,
      "serviceCount": 1
    }
  ],
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.4 服务管理接口

##### 3.4.1 创建服务

**接口描述**：创建新的服务（需要管理员权限）。

**请求信息**：
```
POST /api/v1/services
```

**请求头**：
```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer {access_token}
```

**请求体**：
```json
{
  "name": "AI 聊天机器人与虚拟助手",
  "nameEn": "AI Chatbots & Virtual Assistants",
  "slug": "ai-chatbots",
  "categoryId": "category-001",
  "description": "智能对话代理，通过自然语言处理 7×24 小时处理客户支持。",
  "descriptionEn": "Intelligent conversational agents that handle customer support 24/7 with NLP.",
  "icon": "Bot",
  "features": [
    "自然语言处理",
    "7×24小时支持",
    "多语言支持"
  ],
  "status": "active",
  "featured": true,
  "order": 1
}
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "service-001",
    "name": "AI 聊天机器人与虚拟助手",
    "slug": "ai-chatbots",
    "createdAt": "2025-01-23T10:00:00.000Z"
  },
  "message": "创建成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

##### 3.4.2 更新服务

**接口描述**：更新服务信息（需要管理员权限）。

**请求信息**：
```
PUT /api/v1/services/{serviceId}
```

**请求体**：
```json
{
  "name": "AI 聊天机器人与虚拟助手（更新版）",
  "description": "更新后的描述内容"
}
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "service-001",
    "updatedAt": "2025-01-23T11:00:00.000Z"
  },
  "message": "更新成功",
  "timestamp": "2025-01-23T11:00:00.000Z"
}
```

##### 3.4.3 删除服务

**接口描述**：删除服务（需要管理员权限）。

**请求信息**：
```
DELETE /api/v1/services/{serviceId}
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "service-001",
    "deletedAt": "2025-01-23T12:00:00.000Z"
  },
  "message": "删除成功",
  "timestamp": "2025-01-23T12:00:00.000Z"
}
```

#### 3.5 类型定义

```typescript
interface Service {
  id: string
  name: string
  nameEn: string
  slug: string
  category: ServiceCategory
  description: string
  descriptionEn: string
  longDescription?: string
  longDescriptionEn?: string
  icon: string
  thumbnail?: string
  banner?: string
  features: ServiceFeature[]
  benefits: string[]
  useCases?: UseCase[]
  pricing: ServicePricing
  testimonials?: Testimonial[]
  faqs?: FAQ[]
  cta?: ServiceCTA
  status: 'active' | 'inactive'
  featured: boolean
  order: number
  seo?: ServiceSEO
  createdAt: string
  updatedAt: string
}

interface ServiceCategory {
  id: string
  name: string
  nameEn: string
  slug: string
  description: string
  descriptionEn: string
  icon: string
  order: number
  serviceCount: number
}

interface ServiceFeature {
  id: string
  name: string
  nameEn: string
  description: string
  descriptionEn: string
  icon: string
}

interface UseCase {
  title: string
  description: string
}

interface ServicePricing {
  starter: PricingPlan
  professional: PricingPlan
  enterprise: PricingPlan
}

interface PricingPlan {
  name: string
  nameEn: string
  price: number
  currency: string
  period: 'month' | 'year'
  yearlyPrice?: number
  isPopular?: boolean
  features: string[]
}

interface ServiceCTA {
  primary: string
  primaryEn: string
  secondary: string
  secondaryEn: string
}

interface ServiceSEO {
  title: string
  description: string
  keywords: string[]
}

interface FAQ {
  question: string
  answer: string
}

interface Testimonial {
  id: string
  content: string
  author: string
  company: string
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
