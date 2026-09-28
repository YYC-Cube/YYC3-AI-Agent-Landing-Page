# 安全政策

## 支持的版本

| 版本 | 支持状态 |
| ---- | -------- |
| 1.0.x | ✅ 接收安全更新 |
| < 1.0.0 | ❌ 不再支持 |

## 报告漏洞

我们高度重视安全问题，**请勿通过公开 Issue 报告安全漏洞**。

### 报告渠道

1. **GitHub 私密漏洞报告**（推荐）：仓库 **Security → Report a vulnerability**
2. **邮件**：<admin@0379.email>（标题注明 `[SECURITY] YYC3-AI-Agent-Landing-Page`）

### 报告内容请包含

- 漏洞类型与影响的组件/文件
- 复现步骤或概念验证（PoC）
- 影响评估（数据泄露 / XSS / 供应链等）
- 建议的修复方案（如有）

### 响应承诺

| 阶段 | 时限 |
| ---- | ---- |
| 确认收到 | 48 小时内 |
| 初步评估 | 7 天内 |
| 修复发布 | 视严重程度（高危尽快，中低危随下个版本） |

修复发布后将在 [CHANGELOG.md](CHANGELOG.md) 的 Security 段落披露（细节在漏洞被修复并合理披露后公开）。

## 安全基线

本项目遵循的安全实践（详见 [开发者规范 106/108](docs/YYC3-AI-LANDING-开发者规范/)）：

- **供应链防护**：pnpm 11 `allowBuilds` 构建脚本白名单，默认拒绝第三方安装脚本
- **锁文件锁定**：CI 强制 `--frozen-lockfile`，杜绝依赖漂移
- **依赖安全**：Dependabot 自动跟进安全通告，经 CI 门禁后合入
- **无密钥入库**：敏感信息仅经环境变量注入，`.env*` 不入库
- **最小权限**：部署工作流权限仅 `contents: read` / `pages: write` / `id-token: write`

> 本站为纯静态导出（无服务端运行时），主要风险面为客户端脚本与第三方依赖。

---

> 「***YanYuCloudCube***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
