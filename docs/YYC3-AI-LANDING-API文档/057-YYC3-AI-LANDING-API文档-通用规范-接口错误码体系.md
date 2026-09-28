---
@file: 057-YYC3-AI-LANDING-API文档-通用规范-接口错误码体系.md
@description: YYC3-AI-LANDING 全局统一的接口错误码定义，包含业务码、技术码、错误描述规范
@author: YYC³
@version: v1.0.0
@created: 2026-01-23
@updated: 2026-01-23
@status: published
@tags: [API接口],[通用规范],[错误码]
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# 057-YYC3-AI-LANDING-API文档

## 概述

本文档详细描述YYC3-AI-LANDING-API文档-通用规范-接口错误码体系相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 16构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范通用规范-接口错误码体系相关的业务标准与技术落地要求
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

### 3. 接口错误码体系

#### 3.1 错误码设计原则

##### 3.1.1 错误码格式规范

**错误码结构**：
```
{业务域}_{错误类型}_{具体错误}
```

**业务域定义**：
| 业务域 | 代码 | 说明 |
|--------|------|------|
| 通用 | COMMON | 通用错误 |
| 服务 | SERVICE | 服务相关错误 |
| 用户 | USER | 用户相关错误 |
| 认证 | AUTH | 认证授权错误 |
| 验证 | VALIDATION | 参数验证错误 |
| 外部 | EXTERNAL | 第三方服务错误 |

**错误类型定义**：
| 错误类型 | 代码 | 说明 |
|---------|------|------|
| 参数错误 | PARAM | 参数相关错误 |
| 业务错误 | BUSINESS | 业务逻辑错误 |
| 系统错误 | SYSTEM | 系统级错误 |
| 网络错误 | NETWORK | 网络相关错误 |
| 数据错误 | DATA | 数据相关错误 |

##### 3.1.2 错误码命名规范

**命名规则**：
- 使用大写字母
- 使用下划线分隔单词
- 语义清晰，易于理解
- 避免使用缩写

**示例**：
```
✅ 正确示例：
SERVICE_NOT_FOUND
USER_INVALID_CREDENTIALS
VALIDATION_REQUIRED_FIELD_MISSING

❌ 错误示例：
SERVICE_404
USR_ERR_CRED
VAL_ERR_REQ
```

#### 3.2 通用错误码

##### 3.2.1 成功响应

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| SUCCESS | 200 | 操作成功 | - |

##### 3.2.2 通用参数错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| COMMON_PARAM_MISSING | 400 | 缺少必要参数 | 检查请求参数完整性 |
| COMMON_PARAM_INVALID | 400 | 参数格式错误 | 检查参数格式是否符合要求 |
| COMMON_PARAM_TYPE_ERROR | 400 | 参数类型错误 | 检查参数类型是否正确 |
| COMMON_PARAM_OUT_OF_RANGE | 400 | 参数超出范围 | 检查参数值是否在允许范围内 |
| COMMON_PARAM_TOO_LONG | 400 | 参数过长 | 缩短参数长度 |
| COMMON_PARAM_TOO_SHORT | 400 | 参数过短 | 增加参数长度 |

##### 3.2.3 通用业务错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| COMMON_RESOURCE_NOT_FOUND | 404 | 资源不存在 | 检查资源ID是否正确 |
| COMMON_RESOURCE_ALREADY_EXISTS | 409 | 资源已存在 | 使用不同的资源标识 |
| COMMON_RESOURCE_CONFLICT | 409 | 资源冲突 | 检查资源状态 |
| COMMON_OPERATION_NOT_ALLOWED | 403 | 操作不允许 | 检查操作权限 |
| COMMON_OPERATION_TIMEOUT | 408 | 操作超时 | 重试或联系管理员 |

##### 3.2.4 通用系统错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| COMMON_INTERNAL_ERROR | 500 | 内部服务器错误 | 联系技术支持 |
| COMMON_SERVICE_UNAVAILABLE | 503 | 服务不可用 | 稍后重试 |
| COMMON_DATABASE_ERROR | 500 | 数据库错误 | 联系技术支持 |
| COMMON_NETWORK_ERROR | 502 | 网络错误 | 检查网络连接 |
| COMMON_RATE_LIMIT_EXCEEDED | 429 | 请求频率超限 | 降低请求频率 |

#### 3.3 业务域错误码

##### 3.3.1 服务相关错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| SERVICE_NOT_FOUND | 404 | 服务不存在 | 检查服务ID |
| SERVICE_INVALID_STATUS | 400 | 服务状态无效 | 检查服务状态 |
| SERVICE_CREATE_FAILED | 500 | 服务创建失败 | 联系技术支持 |
| SERVICE_UPDATE_FAILED | 500 | 服务更新失败 | 联系技术支持 |
| SERVICE_DELETE_FAILED | 500 | 服务删除失败 | 联系技术支持 |
| SERVICE_ALREADY_ACTIVE | 409 | 服务已激活 | 无需重复激活 |
| SERVICE_ALREADY_INACTIVE | 409 | 服务已停用 | 无需重复停用 |
| SERVICE_QUOTA_EXCEEDED | 429 | 服务配额超限 | 升级服务套餐 |

##### 3.3.2 用户相关错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| USER_NOT_FOUND | 404 | 用户不存在 | 检查用户ID |
| USER_INVALID_CREDENTIALS | 401 | 凭证无效 | 检查用户名密码 |
| USER_ACCOUNT_LOCKED | 403 | 账户已锁定 | 联系管理员解锁 |
| USER_ACCOUNT_DISABLED | 403 | 账户已禁用 | 联系管理员 |
| USER_EMAIL_ALREADY_EXISTS | 409 | 邮箱已存在 | 使用其他邮箱 |
| USER_PHONE_ALREADY_EXISTS | 409 | 手机号已存在 | 使用其他手机号 |
| USER_PASSWORD_TOO_WEAK | 400 | 密码强度不足 | 使用更强的密码 |
| USER_PASSWORD_EXPIRED | 401 | 密码已过期 | 修改密码 |

##### 3.3.3 认证授权错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| AUTH_TOKEN_MISSING | 401 | 缺少认证令牌 | 提供有效的认证令牌 |
| AUTH_TOKEN_INVALID | 401 | 认证令牌无效 | 重新登录获取令牌 |
| AUTH_TOKEN_EXPIRED | 401 | 认证令牌已过期 | 重新登录获取令牌 |
| AUTH_PERMISSION_DENIED | 403 | 权限不足 | 联系管理员授权 |
| AUTH_ROLE_NOT_ALLOWED | 403 | 角色不允许 | 检查角色权限 |
| AUTH_SESSION_INVALID | 401 | 会话无效 | 重新登录 |

##### 3.3.4 参数验证错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| VALIDATION_REQUIRED_FIELD_MISSING | 400 | 缺少必填字段 | 填写所有必填字段 |
| VALIDATION_EMAIL_FORMAT_ERROR | 400 | 邮箱格式错误 | 检查邮箱格式 |
| VALIDATION_PHONE_FORMAT_ERROR | 400 | 手机号格式错误 | 检查手机号格式 |
| VALIDATION_URL_FORMAT_ERROR | 400 | URL格式错误 | 检查URL格式 |
| VALIDATION_DATE_FORMAT_ERROR | 400 | 日期格式错误 | 使用正确的日期格式 |
| VALIDATION_ENUM_VALUE_INVALID | 400 | 枚举值无效 | 使用有效的枚举值 |
| VALIDATION_MIN_LENGTH_ERROR | 400 | 长度不足 | 增加字段长度 |
| VALIDATION_MAX_LENGTH_ERROR | 400 | 长度超限 | 减少字段长度 |

##### 3.3.5 第三方服务错误

| 错误码 | HTTP状态码 | 说明 | 解决方案 |
|--------|-----------|------|---------|
| EXTERNAL_SERVICE_UNAVAILABLE | 503 | 第三方服务不可用 | 稍后重试 |
| EXTERNAL_SERVICE_TIMEOUT | 504 | 第三方服务超时 | 稍后重试 |
| EXTERNAL_API_RATE_LIMIT | 429 | 第三方API频率限制 | 降低请求频率 |
| EXTERNAL_API_ERROR | 500 | 第三方API错误 | 联系技术支持 |
| EXTERNAL_PAYMENT_FAILED | 400 | 支付失败 | 检查支付信息 |
| EXTERNAL_SMS_SEND_FAILED | 500 | 短信发送失败 | 稍后重试 |

#### 3.4 错误响应格式

##### 3.4.1 标准错误响应

**TypeScript类型定义**：
```typescript
interface ErrorResponse {
  success: false
  error: {
    code: string
    message: string
    message_en?: string
    details?: Record<string, any>
    suggestion?: string
  }
  timestamp: string
  requestId?: string
}
```

**响应示例**：
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
  },
  "timestamp": "2025-01-23T10:00:00.000Z",
  "requestId": "req_1234567890"
}
```

##### 3.4.2 验证错误响应

**响应示例**：
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_REQUIRED_FIELD_MISSING",
    "message": "缺少必填字段",
    "message_en": "Required field missing",
    "details": {
      "fields": [
        {
          "field": "name",
          "message": "名称不能为空"
        },
        {
          "field": "email",
          "message": "邮箱不能为空"
        }
      ]
    },
    "suggestion": "请填写所有必填字段"
  },
  "timestamp": "2025-01-23T10:00:00.000Z",
  "requestId": "req_1234567890"
}
```

##### 3.4.3 业务错误响应

**响应示例**：
```json
{
  "success": false,
  "error": {
    "code": "SERVICE_QUOTA_EXCEEDED",
    "message": "服务配额已用尽",
    "message_en": "Service quota exceeded",
    "details": {
      "currentUsage": 1000,
      "quotaLimit": 1000,
      "resetTime": "2025-02-01T00:00:00.000Z"
    },
    "suggestion": "请升级服务套餐或等待配额重置"
  },
  "timestamp": "2025-01-23T10:00:00.000Z",
  "requestId": "req_1234567890"
}
```

#### 3.5 错误处理最佳实践

##### 3.5.1 前端错误处理

**错误处理示例**：
```typescript
async function fetchServices() {
  try {
    const response = await fetch('/api/v1/services')
    const data = await response.json()
    
    if (!data.success) {
      handleApiError(data.error)
      return
    }
    
    return data.data
  } catch (error) {
    handleNetworkError(error)
  }
}

function handleApiError(error: ErrorResponse['error']) {
  switch (error.code) {
    case 'SERVICE_NOT_FOUND':
      showNotification('服务不存在', 'error')
      break
    case 'AUTH_TOKEN_EXPIRED':
      redirectToLogin()
      break
    case 'VALIDATION_REQUIRED_FIELD_MISSING':
      showValidationErrors(error.details?.fields)
      break
    default:
      showNotification(error.message || '操作失败', 'error')
  }
}

function handleNetworkError(error: Error) {
  showNotification('网络错误，请检查网络连接', 'error')
}
```

##### 3.5.2 错误日志记录

**日志格式**：
```typescript
interface ErrorLog {
  timestamp: string
  requestId: string
  errorCode: string
  errorMessage: string
  userId?: string
  userAgent: string
  ip: string
  stackTrace?: string
  additionalInfo?: Record<string, any>
}
```

**日志记录示例**：
```typescript
function logError(error: Error, context: Record<string, any>) {
  const errorLog: ErrorLog = {
    timestamp: new Date().toISOString(),
    requestId: context.requestId || generateRequestId(),
    errorCode: error.name,
    errorMessage: error.message,
    userId: context.userId,
    userAgent: context.userAgent,
    ip: context.ip,
    stackTrace: error.stack,
    additionalInfo: context
  }
  
  sendToLoggingService(errorLog)
}
```

##### 3.5.3 错误监控告警

**告警规则**：
- 错误率超过5%时发送告警
- 特定错误码出现频率超过阈值时告警
- 系统错误（5xx）立即告警
- 关键业务错误立即告警

**告警通知**：
```typescript
function checkErrorRate() {
  const errorRate = calculateErrorRate()
  
  if (errorRate > 0.05) {
    sendAlert({
      level: 'warning',
      message: `错误率过高: ${(errorRate * 100).toFixed(2)}%`,
      metrics: {
        errorRate,
        totalRequests: getTotalRequests(),
        errorCount: getErrorCount()
      }
    })
  }
}
```

#### 3.6 错误码维护规范

##### 3.6.1 新增错误码流程

1. **申请**：在项目issue中提出新增错误码申请
2. **评审**：团队评审错误码的必要性和命名
3. **定义**：在错误码文档中添加定义
4. **实现**：在代码中实现错误码
5. **测试**：编写测试用例验证错误码
6. **文档**：更新API文档和错误码文档
7. **发布**：随版本发布

##### 3.6.2 废弃错误码流程

1. **标记**：在错误码文档中标记为deprecated
2. **通知**：通知相关开发人员
3. **替换**：使用新的错误码替换
4. **清理**：在下个大版本中移除

##### 3.6.3 错误码版本管理

**版本兼容性**：
- 新增错误码不影响现有功能
- 废弃错误码至少保留一个大版本
- 重大变更需要版本升级

**错误码文档版本**：
```markdown
## 版本历史

### v1.1.0 (2025-01-23)
- 新增 SERVICE_QUOTA_EXCEEDED 错误码
- 废弃 USER_LOGIN_FAILED 错误码

### v1.0.0 (2025-01-01)
- 初始版本
```

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
