---
@file: 056-YYC3-AI-LANDING-API文档-通用规范-RESTful接口设计标准.md
@description: YYC3-AI-LANDING 全项目RESTful接口的统一设计标准，包含请求、响应、路径规范
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [API接口],[通用规范],[RESTful]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 056-YYC3-AI-LANDING-API文档

## 概述

本文档详细描述YYC3-AI-LANDING-API文档-通用规范-RESTful接口设计标准相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范通用规范-RESTful接口设计标准相关的业务标准与技术落地要求
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

### 3. RESTful接口设计标准

#### 3.1 接口命名规范

##### 3.1.1 URL路径规范

**基本规则**：
- 使用小写字母
- 使用连字符（-）分隔单词
- 使用复数形式表示资源集合
- 使用名词而非动词
- 避免使用文件扩展名（如.json, .xml）

**URL层级结构**：
```
/api/v{version}/{resource}/{id}/{sub-resource}/{sub-id}
```

**示例**：
```
✅ 正确示例：
GET    /api/v1/services
GET    /api/v1/services/{serviceId}
POST   /api/v1/services
PUT    /api/v1/services/{serviceId}
DELETE /api/v1/services/{serviceId}

❌ 错误示例：
GET    /api/v1/getServices
GET    /api/v1/service/{id}
GET    /api/v1/services.json
GET    /api/V1/Services
```

##### 3.1.2 HTTP方法规范

| 方法 | 用途 | 是否幂等 | 安全性 |
|------|------|---------|--------|
| GET | 获取资源 | ✅ 是 | ✅ 安全 |
| POST | 创建资源 | ❌ 否 | ❌ 不安全 |
| PUT | 完整更新资源 | ✅ 是 | ❌ 不安全 |
| PATCH | 部分更新资源 | ❌ 否 | ❌ 不安全 |
| DELETE | 删除资源 | ✅ 是 | ❌ 不安全 |
| OPTIONS | 获取支持的HTTP方法 | ✅ 是 | ✅ 安全 |
| HEAD | 获取响应头 | ✅ 是 | ✅ 安全 |

**使用场景**：
```typescript
// 获取服务列表
GET /api/v1/services

// 获取单个服务详情
GET /api/v1/services/{serviceId}

// 创建新服务
POST /api/v1/services

// 完整更新服务
PUT /api/v1/services/{serviceId}

// 部分更新服务
PATCH /api/v1/services/{serviceId}

// 删除服务
DELETE /api/v1/services/{serviceId}
```

##### 3.1.3 查询参数规范

**分页参数**：
```
?page=1&pageSize=20
```

**排序参数**：
```
?sort=createdAt:desc,updatedAt:asc
```

**过滤参数**：
```
?status=active&category=chatbot
```

**搜索参数**：
```
?keyword=AI&fields=name,description
```

**字段选择**：
```
?fields=id,name,description,price
```

**完整示例**：
```
GET /api/v1/services?page=1&pageSize=20&sort=createdAt:desc&status=active&keyword=AI&fields=id,name,description,price
```

#### 3.2 请求规范

##### 3.2.1 请求头规范

**通用请求头**：
```http
Content-Type: application/json
Accept: application/json
Accept-Language: zh-CN
User-Agent: YYC3-AI-LANDING/1.0.0
X-Request-ID: uuid-v4
X-Client-Version: 1.0.0
X-Client-Platform: web
```

**认证请求头**：
```http
Authorization: Bearer {access_token}
X-API-Key: {api_key}
```

**请求头示例**：
```typescript
const headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Accept-Language': 'zh-CN',
  'User-Agent': 'YYC3-AI-LANDING/1.0.0',
  'X-Request-ID': crypto.randomUUID(),
  'X-Client-Version': '1.0.0',
  'X-Client-Platform': 'web',
}
```

##### 3.2.2 请求体规范

**JSON格式要求**：
- 使用UTF-8编码
- 使用camelCase命名属性
- 日期使用ISO 8601格式
- 布尔值使用true/false
- 数字不使用引号

**请求体示例**：
```json
{
  "name": "AI Chatbot Service",
  "description": "智能聊天机器人服务",
  "price": 997,
  "currency": "USD",
  "isActive": true,
  "features": [
    "Natural Language Processing",
    "24/7 Support",
    "Multi-language Support"
  ],
  "createdAt": "2025-01-23T10:00:00Z"
}
```

##### 3.2.3 版本控制规范

**URL版本控制**（推荐）：
```
/api/v1/services
/api/v2/services
```

**请求头版本控制**：
```http
Accept: application/vnd.yyc3.v1+json
```

**查询参数版本控制**：
```
/api/services?version=1
```

**版本策略**：
- v1: 初始版本
- v2: 重大变更，不兼容v1
- v1.1: 小版本更新，向后兼容v1

#### 3.3 响应规范

##### 3.3.1 响应状态码规范

**成功响应**：
| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 200 | OK | GET/PUT/PATCH成功 |
| 201 | Created | POST创建成功 |
| 204 | No Content | DELETE成功 |
| 206 | Partial Content | 分页/部分内容 |

**客户端错误**：
| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 400 | Bad Request | 请求参数错误 |
| 401 | Unauthorized | 未认证 |
| 403 | Forbidden | 无权限 |
| 404 | Not Found | 资源不存在 |
| 409 | Conflict | 资源冲突 |
| 422 | Unprocessable Entity | 业务逻辑错误 |
| 429 | Too Many Requests | 请求频率超限 |

**服务端错误**：
| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 500 | Internal Server Error | 服务器内部错误 |
| 502 | Bad Gateway | 网关错误 |
| 503 | Service Unavailable | 服务不可用 |
| 504 | Gateway Timeout | 网关超时 |

##### 3.3.2 响应体规范

**成功响应格式**：
```json
{
  "success": true,
  "data": {
    "id": "service-001",
    "name": "AI Chatbot Service",
    "description": "智能聊天机器人服务"
  },
  "message": "操作成功",
  "timestamp": "2025-01-23T10:00:00Z"
}
```

**列表响应格式**：
```json
{
  "success": true,
  "data": [
    {
      "id": "service-001",
      "name": "AI Chatbot Service"
    },
    {
      "id": "service-002",
      "name": "Workflow Automation"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 100,
    "totalPages": 5
  },
  "message": "查询成功",
  "timestamp": "2025-01-23T10:00:00Z"
}
```

**错误响应格式**：
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "请求参数验证失败",
    "details": [
      {
        "field": "name",
        "message": "名称不能为空"
      },
      {
        "field": "price",
        "message": "价格必须大于0"
      }
    ]
  },
  "timestamp": "2025-01-23T10:00:00Z"
}
```

##### 3.3.3 分页响应规范

**分页参数**：
```typescript
interface PaginationParams {
  page: number
  pageSize: number
  sortBy?: string
  sortOrder?: 'asc' | 'desc'
}

interface PaginationResponse {
  page: number
  pageSize: number
  total: number
  totalPages: number
  hasNext: boolean
  hasPrevious: boolean
}
```

**分页响应示例**：
```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 100,
    "totalPages": 5,
    "hasNext": true,
    "hasPrevious": false
  }
}
```

#### 3.4 数据规范

##### 3.4.1 命名规范

**属性命名**：
- 使用camelCase
- 避免缩写
- 使用有意义的名称
- 布尔值使用is/has前缀

**示例**：
```json
{
  "serviceId": "service-001",
  "serviceName": "AI Chatbot",
  "isActive": true,
  "hasTrial": true,
  "createdAt": "2025-01-23T10:00:00Z",
  "updatedAt": "2025-01-23T10:00:00Z"
}
```

##### 3.4.2 数据类型规范

**字符串**：
- 使用双引号
- 日期使用ISO 8601格式
- 枚举值使用字符串

**数字**：
- 不使用引号
- 整数和浮点数区分
- 金额使用字符串避免精度问题

**布尔值**：
- 使用true/false
- 不使用"true"/"false"字符串

**数组**：
- 使用方括号
- 空数组使用[]

**对象**：
- 使用花括号
- 空对象使用{}

**示例**：
```json
{
  "id": "service-001",
  "name": "AI Chatbot",
  "price": "997.00",
  "discount": 0.2,
  "isActive": true,
  "tags": ["AI", "Chatbot", "Automation"],
  "metadata": {},
  "features": []
}
```

##### 3.4.3 日期时间规范

**格式**：
- ISO 8601格式：YYYY-MM-DDTHH:mm:ss.sssZ
- 时区使用UTC
- 示例：2025-01-23T10:00:00.000Z

**字段命名**：
- createdAt: 创建时间
- updatedAt: 更新时间
- deletedAt: 删除时间（软删除）
- publishedAt: 发布时间

**示例**：
```json
{
  "createdAt": "2025-01-23T10:00:00.000Z",
  "updatedAt": "2025-01-23T11:30:00.000Z",
  "deletedAt": null
}
```

#### 3.5 安全规范

##### 3.5.1 认证规范

**Bearer Token认证**：
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**API Key认证**：
```http
X-API-Key: sk_live_xxxxxxxxxxxxx
```

**Basic Auth**：
```http
Authorization: Basic base64(username:password)
```

##### 3.5.2 敏感数据规范

**不返回敏感信息**：
- 密码
- 信用卡号
- 完整身份证号
- 完整手机号（脱敏处理）

**脱敏示例**：
```json
{
  "phone": "138****5678",
  "email": "u***@example.com",
  "idCard": "110101********1234"
}
```

##### 3.5.3 HTTPS规范

**强制HTTPS**：
- 生产环境必须使用HTTPS
- 开发环境可使用HTTP
- API响应头设置HSTS

**安全响应头**：
```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'
```

#### 3.6 性能规范

##### 3.6.1 响应时间要求

| 接口类型 | 响应时间要求 |
|---------|-------------|
| 简单查询 | < 100ms |
| 复杂查询 | < 500ms |
| 写操作 | < 200ms |
| 批量操作 | < 1000ms |

##### 3.6.2 缓存策略

**Cache-Control头**：
```http
Cache-Control: public, max-age=3600
Cache-Control: private, no-cache
Cache-Control: no-store
```

**ETag使用**：
```http
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```

##### 3.6.3 压缩规范

**启用压缩**：
- 使用gzip或brotli
- 响应体大于1KB时启用
- Accept-Encoding协商

**响应头**：
```http
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
```

#### 3.7 文档规范

##### 3.7.1 OpenAPI规范

**使用OpenAPI 3.0**：
```yaml
openapi: 3.0.0
info:
  title: YYC3 AI Landing API
  version: 1.0.0
  description: YYC3 AI代理服务落地页API文档
servers:
  - url: https://api.yyc3.com/v1
    description: 生产环境
  - url: https://api-staging.yyc3.com/v1
    description: 测试环境
paths:
  /services:
    get:
      summary: 获取服务列表
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServiceListResponse'
```

##### 3.7.2 接口文档要求

**每个接口必须包含**：
- 接口描述
- 请求方法
- 请求路径
- 请求参数
- 请求体（如果有）
- 响应示例
- 错误码说明
- 权限要求

#### 3.8 错误处理规范

##### 3.8.1 错误码设计

**错误码格式**：
```
{业务域}_{错误类型}_{具体错误}
```

**示例**：
```
SERVICE_NOT_FOUND
SERVICE_VALIDATION_ERROR
SERVICE_CREATE_FAILED
```

##### 3.8.2 错误信息规范

**错误信息要求**：
- 使用用户友好的语言
- 提供具体的错误原因
- 包含解决建议
- 支持国际化

**示例**：
```json
{
  "success": false,
  "error": {
    "code": "SERVICE_NOT_FOUND",
    "message": "服务不存在",
    "message_en": "Service not found",
    "details": {
      "serviceId": "service-001"
    },
    "suggestion": "请检查服务ID是否正确"
  }
}
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
