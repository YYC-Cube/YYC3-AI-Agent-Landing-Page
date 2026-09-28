/**
 * @fileoverview Next.js 配置文件
 * @description YYC³ AI Agent Landing Page 项目配置
 * @author YYC³
 * @version 2.0.0
 * @updated 2026-09-28
 * @copyright Copyright (c) 2026 YYC³
 * @license MIT
 */

/** @type {import('next').NextConfig} */
const nextConfig = {
  // GitHub Pages 静态导出（部署至 https://ai-landing.yyc3.top）
  output: 'export',
  trailingSlash: true,
  typescript: {
    ignoreBuildErrors: false,
  },
  eslint: {
    ignoreDuringBuilds: false,
  },
  // 静态导出不支持 Next Image 优化服务，必须关闭
  images: {
    unoptimized: true,
  },
  experimental: {
    optimizePackageImports: ['lucide-react'],
  },
}

export default nextConfig
