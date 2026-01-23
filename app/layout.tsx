import type React from "react"
import type { Metadata } from "next"
import { GeistSans } from "geist/font/sans"
import { GeistMono } from "geist/font/mono"
import { Analytics } from "@vercel/analytics/next"
import { LocaleProvider } from "@/contexts/locale-context"
import "./globals.css"

export const metadata: Metadata = {
  title: "YYC³ AI Agent Landing Page",
  description: "YYC³ AI Agent Landing Page - 专业的AI代理服务展示平台",
  generator: "YYC³",
  icons: {
    icon: "/yyc3-pwa-icon.png",
    shortcut: "/yyc3-pwa-icon.png",
    apple: "/yyc3-pwa-icon.png",
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="zh">
      <body className={`font-sans antialiased ${GeistSans.variable} ${GeistMono.variable}`}>
        <LocaleProvider>{children}</LocaleProvider>
        <Analytics />
      </body>
    </html>
  )
}
