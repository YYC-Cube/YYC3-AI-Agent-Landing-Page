---
file: 108-YYC3-AI-LANDING-开发者规范-CI-CD自动化部署规范.md
description: YYC3-AI-Landing-Page CI 质量门禁与 GitHub Pages 自动化部署规范（ai-landing.yyc3.top）
author: YYC³ Team
version: v1.0.0
created: 2026-09-28
updated: 2026-09-28
status: published
tags: [CI-CD, GitHub Actions, GitHub Pages, 自动化部署]
category: standard
---

# 🚀 CI/CD 自动化部署规范

> 状态：✅ 与项目实况对齐（2026-09-28）| 校准来源：.github/workflows/ci.yml / deploy-pages.yml
> 生产站点：**https://ai-landing.yyc3.top**（CNAME 已随静态产物部署）

## 一、流水线全景

```
push main / PR ──► CI（ci.yml）                    push main ──► Deploy（deploy-pages.yml）
 ├─ pnpm install --frozen-lockfile                 ├─ build job
 ├─ pnpm lint                                       │  ├─ install --frozen-lockfile
 ├─ pnpm typecheck                                  │  ├─ lint + typecheck（质量门禁前置）
 ├─ pnpm build（静态导出 out/）                      │  ├─ pnpm build → out/
 └─ upload-artifact（7 天留存）                      │  ├─ configure-pages@v5
                                                     │  └─ upload-pages-artifact@v3
                                                     └─ deploy job：deploy-pages@v4 → 线上
```

| 维度 | CI（ci.yml） | Deploy（deploy-pages.yml） |
| ---- | ------------ | -------------------------- |
| 触发 | push main + PR → main | push main + 手动（workflow_dispatch） |
| 门禁 | lint / typecheck / build | lint / typecheck / build（部署前置） |
| 并发 | `ci-${ref}` 同引用取消旧跑 | `pages` 组串行，**不取消**进行中的部署 |
| 权限 | 默认 | `contents: read` / `pages: write` / `id-token: write`（最小化） |
| 环境 | ubuntu-latest + Node 22 + pnpm 11 | 同左 + github-pages environment |

## 二、CI 质量门禁标准

- **安装必须 `--frozen-lockfile`**：锁文件与 package.json 不一致直接失败，杜绝本地能跑线上炸
- **静态导出产物上传**为 `static-export` artifact，保留 7 天，供排查与人工验收
- 任何一项失败即整条流水线红灯，PR 不得合入

## 三、GitHub Pages 部署规范

### 3.1 首次启用（一次性，仓库管理员操作）

1. 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**
2. 确认自定义域：**Settings → Pages → Custom domain** 填 `ai-landing.yyc3.top`（或依赖仓库内 `CNAME` 文件自动识别）
3. DNS 侧配置 CNAME 记录指向 `<owner>.github.io`
4. 推送 main 或手动 **Actions → Deploy to GitHub Pages → Run workflow** 触发首次部署

### 3.2 静态导出约束（不可违反）

| 约束 | 配置位置 | 原因 |
| ---- | -------- | ---- |
| `output: 'export'` | [next.config.mjs](../../next.config.mjs) | Pages 仅服务静态文件 |
| `trailingSlash: true` | 同上 | 目录式 URL 与 404.html 兜底兼容 |
| `images.unoptimized: true` | 同上 | 无图片优化服务运行时 |
| 无 `next start` 脚本 | package.json | 纯静态产物，预览用 `npx serve out` |

### 3.3 部署流程纪律

- **只有 main 分支触发部署**；feature 分支由 ci.yml 验证，不部署
- 并发组 `pages` + `cancel-in-progress: false`：保证正在进行的发布不被中断，后续变更排队执行
- 部署地址由 `deploy-pages@v4` 的 environment url 输出，可在 Actions 运行详情查看

### 3.4 回滚

1. GitHub 界面：**Actions → Deploy to GitHub Pages → 选择历史成功运行 → Re-run**（以历史 commit 重建）
2. Git 层面：`git revert <bad-commit> && git push origin main` 触发新一轮部署（推荐，保持历史可溯）

## 四、变更规范

- 修改 workflow 文件必须走 PR 并附运行截图/链接验证
- 升级 Actions 版本（如 checkout v4 → v5）需确认 changelog 无 breaking changes
- 新增质量门禁（如测试）先加 ci.yml，稳定后再纳入 deploy-pages.yml build job

## 五、检查清单（发布前）

- [ ] 本地 `pnpm lint && pnpm typecheck && pnpm build` 全绿
- [ ] CI 徽章状态绿色（见 README 顶部）
- [ ] 部署后访问 https://ai-landing.yyc3.top 验证首页/404/子路由（privacy、terms）
- [ ] 浏览器控制台无报错，favicon 与 og-image 正常加载

---

> 「***YanYuCloudCube***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
