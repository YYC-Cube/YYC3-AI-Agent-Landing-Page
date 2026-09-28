# 更新日志

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 格式，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Fixed 修复

- **CI/CD 部署失败**：pnpm 11 默认 `minimumReleaseAge`（24h）策略拒绝了 lockfile 中 27 个新发布包（sharp 生态），导致 Deploy 失败、ai-landing.yyc3.top 404；现于 pnpm-workspace.yaml 显式声明 `minimumReleaseAge: 1440` 并重新解析 lockfile（sharp 0.35.5 → 0.35.4）
- **Dependabot 全部 5 个开放漏洞清零**：通过 pnpm overrides 强制传递依赖修复下限——browserslist ^4.28.7（GHSA 内存增长/原型写入）、nanoid ^3.3.18（GHSA 零尺寸死循环）、baseline-browser-mapping ^2.11.0（DoS）、postcss ^8.5.23（sourceMappingURL 任意读取）
- **文档版本漂移**：全量同步 130+ 处过时的 "Next.js 14" 引用至 Next.js 16 实况（docs/ 与 README）

### Added 新增

- 仓库 Topics 标签体系上线（20 个：nextjs / react / ai-agent / github-pages 等）

## [1.0.0] - 2026-09-28

首个正式版本：技术栈全面升级至当前稳定线，建立 CI/CD 自动化部署与完整文档体系。

### Added 新增

- **CI 质量门禁**（[ci.yml](.github/workflows/ci.yml)）：push main / PR 触发，`--frozen-lockfile` 安装 + lint + typecheck + 静态导出构建，产物留存 7 天
- **GitHub Pages 自动化部署**（[deploy-pages.yml](.github/workflows/deploy-pages.yml)）：push main 自动发布至 **<https://ai-landing.yyc3.top**，含> lint/typecheck 部署前置门禁
- **开发者标规系列**（docs/YYC3-AI-LANDING-开发者规范/）：
  - 106 开发环境与工具链（Node/pnpm 版本、依赖策略、allowBuilds 供应链防护）
  - 107 代码规范与 Git 工作流（TypeScript 门禁、命名、组件、分支模型）
  - 108 CI/CD 自动化部署（流水线、Pages 约束、回滚）
- 贡献指南 [CONTRIBUTING.md](CONTRIBUTING.md)、安全政策 [SECURITY.md](SECURITY.md)、行为准则 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- README 徽章体系（CI/部署/站点状态 + 技术栈版本 + 规范徽章）与仓库标签关键词区
- 品牌 SVG 图标组件 `components/ui/social-icons.tsx`（替代 lucide-react v1 移除的品牌图标）
- Favicon 体系（32/16/apple-touch-icon）与 og-image，metadataBase 指向生产域名

### Changed 变更

- 依赖全面审计升级：next ^16.3.6、react ^19.3.0、typescript ^5.9.3、tailwindcss ^4.3.0、eslint ^9.39.5、@tsparticles/* ^3.9.1、lucide-react ^1.48.0、framer-motion ^13.4.4
- 包管理器锁定 pnpm@11.10.0，设置迁至 pnpm-workspace.yaml（`allowBuilds` 供应链白名单）
- ESLint 迁移至原生 flat config（eslint-config-next 16 子路径导出，移除 FlatCompat）
- 静态导出配置对齐：`output: 'export'` + `trailingSlash: true` + `images.unoptimized: true`
- 开发服务器端口规范化为 **3030**
- `use-media-query` 重构为 `useSyncExternalStore` 订阅模式（React 19 lint 合规）
- navbar 菜单状态逻辑内聚化，卸载时清理订阅

### Removed 移除

- 清除 40+ 幽灵依赖（expo、react-native、three、recharts、表单库、22 个未用 Radix 包等）
- 删除无引用的 `styles/globals.css` 与 `components/theme-provider.tsx`
- 移除对已删除 logo 资产的引用（改用 favicon-32.png）

### Security 安全

- pnpm 11 `allowBuilds` 构建脚本白名单：仅 `@tsparticles/engine` 与 `unrs-resolver` 获准执行安装脚本
- 依赖版本显式化，消除 `latest` 浮动引用
- Dependabot 自动依赖安全更新

[Unreleased]: https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/YYC-Cube/YYC3-AI-Agent-Landing-Page/releases/tag/v1.0.0
