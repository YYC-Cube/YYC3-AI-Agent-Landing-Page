---
@file: 059-YYC3-AI-LANDING-API文档-业务域-首页接口手册.md
@description: YYC3-AI-LANDING 首页所有业务接口的详细定义，包含入参、出参、调用示例
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [API接口],[业务域],[首页]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 059-YYC3-AI-LANDING-API文档

## 概述

本文档详细描述YYC3-AI-LANDING-API文档-业务域-首页接口手册相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范业务域-首页接口手册相关的业务标准与技术落地要求
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

### 3. 业务域-首页接口手册

#### 3.1 接口概述

YYC³ AI代理服务落地页的首页接口主要用于获取首页展示的各类数据，包括：
- Hero区域内容
- 问题与解决方案内容
- 服务列表
- 客户评价
- 数据指标
- 定价信息
- 流程步骤
- 页脚信息

由于本项目是静态落地页，大部分内容通过前端配置和国际化系统管理。以下接口为未来扩展预留。

#### 3.2 首页内容接口

##### 3.2.1 获取首页配置

**接口描述**：获取首页的完整配置信息，包括各区域的文本内容和配置参数。

**请求信息**：
```
GET /api/v1/home/config
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
| locale | string | 否 | 语言代码 | zh-CN, en-US |

**请求示例**：
```bash
curl -X GET "https://api.yyc3.com/api/v1/home/config?locale=zh-CN" \
  -H "Accept: application/json" \
  -H "Accept-Language: zh-CN"
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "hero": {
      "title": "AI 驱动业绩增长，降低运营成本",
      "subtitle": "我们帮助企业自动化工作流程，构建智能聊天机器人，集成 7×24 小时工作的 AI 代理，提升生产力并推动业务增长。",
      "ctaPrimary": "预约免费咨询",
      "ctaSecondary": "查看案例研究",
      "badge1": "无设置费用",
      "badge2": "30 天投资回报保证"
    },
    "problemSolution": {
      "problemTitle": "还在手动管理一切？",
      "problems": [
        "在重复性任务上花费大量时间，而这些任务本可以自动化",
        "因无法 7×24 小时响应咨询而错失潜在客户",
        "在不增加人员的情况下难以扩展运营规模",
        "在 AI 驱动的竞争对手面前失去竞争优势"
      ],
      "solutionTitle": "我们构建真正有效的 AI 解决方案",
      "solutions": [
        "定制 AI 代理，即时处理客户咨询",
        "工作流自动化，每周节省 20+ 小时",
        "与现有工具和系统无缝集成",
        "实施后 30 天内实现可证明的投资回报"
      ]
    },
    "metrics": {
      "title": "可衡量的重要成果",
      "subtitle": "我们的客户看到了对其业务底线的即时影响",
      "items": [
        {
          "icon": "Clock",
          "value": "80%",
          "label": "手动任务节省时间"
        },
        {
          "icon": "DollarSign",
          "value": "300%",
          "label": "6 个月内平均投资回报率"
        },
        {
          "icon": "BarChart3",
          "value": "150%",
          "label": "潜在客户转化率提升"
        },
        {
          "icon": "TrendingUp",
          "value": "24/7",
          "label": "自动化客户支持"
        }
      ]
    },
    "process": {
      "title": "简单的三步流程",
      "subtitle": "从咨询到实施，我们让 AI 采用变得无缝",
      "steps": [
        {
          "step": 1,
          "title": "预约咨询",
          "description": "安排免费咨询，讨论您的业务需求并识别自动化机会"
        },
        {
          "step": 2,
          "title": "AI 策略",
          "description": "我们分析您的工作流程，创建针对您特定业务目标的定制 AI 策略"
        },
        {
          "step": 3,
          "title": "实施",
          "description": "我们的团队构建、测试和部署您的 AI 解决方案，提供持续支持和优化"
        }
      ]
    },
    "cta": {
      "title": "准备好用 AI 降低成本了吗？",
      "buttonPrimary": "预约免费咨询",
      "buttonSecondary": "致电 (555) 123-4567"
    }
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
    "code": "COMMON_RESOURCE_NOT_FOUND",
    "message": "首页配置不存在",
    "suggestion": "请联系管理员配置首页内容"
  },
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

##### 3.2.2 更新首页配置

**接口描述**：更新首页的配置信息（需要管理员权限）。

**请求信息**：
```
PUT /api/v1/home/config
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
  "hero": {
    "title": "AI 驱动业绩增长，降低运营成本",
    "subtitle": "我们帮助企业自动化工作流程，构建智能聊天机器人，集成 7×24 小时工作的 AI 代理，提升生产力并推动业务增长。",
    "ctaPrimary": "预约免费咨询",
    "ctaSecondary": "查看案例研究"
  }
}
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "config-001",
    "updatedAt": "2025-01-23T10:00:00.000Z"
  },
  "message": "更新成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.3 客户评价接口

##### 3.3.1 获取客户评价列表

**接口描述**：获取首页展示的客户评价列表。

**请求信息**：
```
GET /api/v1/home/testimonials
```

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| page | number | 否 | 页码 | 1 |
| pageSize | number | 否 | 每页数量 | 10 |
| locale | string | 否 | 语言代码 | zh-CN |

**请求示例**：
```bash
curl -X GET "https://api.yyc3.com/api/v1/home/testimonials?page=1&pageSize=10&locale=zh-CN"
```

**成功响应**：
```json
{
  "success": true,
  "data": [
    {
      "id": "testimonial-001",
      "content": "AI 聊天机器人使我们的潜在客户转化率提高了 200%，并自动处理 90% 的客户咨询。第一个月就看到了明显的投资回报。",
      "author": {
        "name": "Sarah Johnson",
        "title": "CEO",
        "company": "TechStart Solutions"
      },
      "rating": 5,
      "featured": true,
      "createdAt": "2025-01-15T10:00:00.000Z"
    },
    {
      "id": "testimonial-002",
      "content": "工作流自动化每周为我们节省了 25 小时。我们的团队现在可以专注于战略增长，而不是重复性任务。",
      "author": {
        "name": "Michael Chen",
        "title": "运营总监",
        "company": "GrowthCorp"
      },
      "rating": 5,
      "featured": true,
      "createdAt": "2025-01-10T10:00:00.000Z"
    },
    {
      "id": "testimonial-003",
      "content": "AI 集成改变了我们的电子商务平台。通过个性化客户体验，销售额增长了 180%。",
      "author": {
        "name": "Emily Rodriguez",
        "title": "创始人",
        "company": "RetailMax"
      },
      "rating": 5,
      "featured": true,
      "createdAt": "2025-01-05T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "total": 3,
    "totalPages": 1,
    "hasNext": false,
    "hasPrevious": false
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

##### 3.3.2 创建客户评价

**接口描述**：创建新的客户评价（需要管理员权限）。

**请求信息**：
```
POST /api/v1/home/testimonials
```

**请求体**：
```json
{
  "content": "这是一条新的客户评价",
  "author": {
    "name": "张三",
    "title": "CEO",
    "company": "示例公司"
  },
  "rating": 5,
  "featured": true
}
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "id": "testimonial-004",
    "content": "这是一条新的客户评价",
    "author": {
      "name": "张三",
      "title": "CEO",
      "company": "示例公司"
    },
    "rating": 5,
    "featured": true,
    "createdAt": "2025-01-23T10:00:00.000Z"
  },
  "message": "创建成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.4 页脚信息接口

##### 3.4.1 获取页脚配置

**接口描述**：获取页脚的配置信息。

**请求信息**：
```
GET /api/v1/home/footer
```

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| locale | string | 否 | 语言代码 | zh-CN |

**成功响应**：
```json
{
  "success": true,
  "data": {
    "company": {
      "name": "AI Agency",
      "description": "通过智能自动化和前沿 AI 集成解决方案转型企业。",
      "logo": "/yyc3-logo-white.png"
    },
    "services": [
      {
        "name": "AI 聊天机器人与虚拟助手",
        "href": "#services"
      },
      {
        "name": "工作流自动化",
        "href": "#services"
      },
      {
        "name": "AI 集成服务",
        "href": "#services"
      },
      {
        "name": "智能分析与洞察",
        "href": "#services"
      },
      {
        "name": "定制 AI 开发",
        "href": "#services"
      }
    ],
    "companyLinks": [
      {
        "name": "关于我们",
        "href": "/about"
      },
      {
        "name": "案例研究",
        "href": "/case-studies"
      },
      {
        "name": "博客",
        "href": "/blog"
      },
      {
        "name": "招聘",
        "href": "/careers"
      }
    ],
    "contact": {
      "email": "hello@aiagency.com",
      "phone": "(555) 123-4567",
      "address": "123 AI Street, Tech City"
    },
    "social": [
      {
        "platform": "linkedin",
        "url": "https://linkedin.com/company/aiagency"
      },
      {
        "platform": "twitter",
        "url": "https://twitter.com/aiagency"
      },
      {
        "platform": "facebook",
        "url": "https://facebook.com/aiagency"
      }
    ],
    "legal": {
      "copyright": "© 2025 AI Agency. 保留所有权利。",
      "privacy": {
        "name": "隐私政策",
        "href": "/privacy"
      },
      "terms": {
        "name": "服务条款",
        "href": "/terms"
      }
    }
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.5 国际化接口

##### 3.5.1 获取翻译字典

**接口描述**：获取指定语言的翻译字典。

**请求信息**：
```
GET /api/v1/i18n/translations
```

**查询参数**：
| 参数名 | 类型 | 必填 | 说明 | 示例 |
|--------|------|------|------|------|
| locale | string | 是 | 语言代码 | zh-CN, en-US |
| namespace | string | 否 | 命名空间 | common, home, services |

**请求示例**：
```bash
curl -X GET "https://api.yyc3.com/api/v1/i18n/translations?locale=zh-CN&namespace=home"
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "hero": {
      "title": "AI 驱动业绩增长，降低运营成本",
      "subtitle": "我们帮助企业自动化工作流程，构建智能聊天机器人，集成 7×24 小时工作的 AI 代理，提升生产力并推动业务增长。",
      "ctaPrimary": "预约免费咨询",
      "ctaSecondary": "查看案例研究",
      "badge1": "无设置费用",
      "badge2": "30 天投资回报保证"
    },
    "services": {
      "title": "我们的 AI 解决方案",
      "subtitle": "全面的 AI 服务，旨在转型您的业务运营"
    }
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

##### 3.5.2 获取支持的语言列表

**接口描述**：获取系统支持的所有语言列表。

**请求信息**：
```
GET /api/v1/i18n/locales
```

**成功响应**：
```json
{
  "success": true,
  "data": [
    {
      "code": "zh-CN",
      "name": "简体中文",
      "nativeName": "简体中文",
      "flag": "🇨🇳",
      "default": true
    },
    {
      "code": "en-US",
      "name": "English (US)",
      "nativeName": "English",
      "flag": "🇺🇸",
      "default": false
    }
  ],
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.6 数据统计接口

##### 3.6.1 获取首页统计数据

**接口描述**：获取首页展示的统计数据（如客户数量、项目数量等）。

**请求信息**：
```
GET /api/v1/home/stats
```

**成功响应**：
```json
{
  "success": true,
  "data": {
    "clients": {
      "count": 500,
      "label": "服务客户",
      "growth": "+25%"
    },
    "projects": {
      "count": 1200,
      "label": "完成项目",
      "growth": "+30%"
    },
    "satisfaction": {
      "score": 98,
      "label": "客户满意度",
      "unit": "%"
    },
    "countries": {
      "count": 45,
      "label": "覆盖国家"
    }
  },
  "message": "获取成功",
  "timestamp": "2025-01-23T10:00:00.000Z"
}
```

#### 3.7 类型定义

```typescript
interface HomeConfig {
  hero: HeroConfig
  problemSolution: ProblemSolutionConfig
  metrics: MetricsConfig
  process: ProcessConfig
  cta: CTAConfig
}

interface HeroConfig {
  title: string
  subtitle: string
  ctaPrimary: string
  ctaSecondary: string
  badge1: string
  badge2: string
}

interface ProblemSolutionConfig {
  problemTitle: string
  problems: string[]
  solutionTitle: string
  solutions: string[]
}

interface MetricsConfig {
  title: string
  subtitle: string
  items: MetricItem[]
}

interface MetricItem {
  icon: string
  value: string
  label: string
}

interface ProcessConfig {
  title: string
  subtitle: string
  steps: ProcessStep[]
}

interface ProcessStep {
  step: number
  title: string
  description: string
}

interface CTAConfig {
  title: string
  buttonPrimary: string
  buttonSecondary: string
}

interface Testimonial {
  id: string
  content: string
  author: {
    name: string
    title: string
    company: string
  }
  rating: number
  featured: boolean
  createdAt: string
}

interface FooterConfig {
  company: {
    name: string
    description: string
    logo: string
  }
  services: FooterLink[]
  companyLinks: FooterLink[]
  contact: {
    email: string
    phone: string
    address: string
  }
  social: SocialLink[]
  legal: {
    copyright: string
    privacy: {
      name: string
      href: string
    }
    terms: {
      name: string
      href: string
    }
  }
}

interface FooterLink {
  name: string
  href: string
}

interface SocialLink {
  platform: string
  url: string
}

interface Translation {
  [key: string]: string | Translation
}

interface Locale {
  code: string
  name: string
  nativeName: string
  flag: string
  default: boolean
}

interface HomeStats {
  clients: StatItem
  projects: StatItem
  satisfaction: StatItem
  countries: StatItem
}

interface StatItem {
  count: number
  label: string
  growth?: string
  unit?: string
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
