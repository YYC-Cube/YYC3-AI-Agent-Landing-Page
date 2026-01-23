/**
 * @fileoverview Next.js 配置文件
 * @description YYC³ AI Agent Landing Page 项目配置
 * @author YYC³
 * @version 1.0.0
 * @created 2026-01-23
 * @copyright Copyright (c) 2026 YYC³
 * @license MIT
 */

/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    ignoreBuildErrors: false,
  },
  images: {
    unoptimized: false,
    domains: ['prod.spline.design'],
  },
  eslint: {
    ignoreDuringBuilds: false,
  },
  experimental: {
    optimizePackageImports: ['lucide-react'],
  },
}

export default nextConfig
