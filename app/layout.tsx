import type React from "react"
import type { Metadata } from "next"
import { GeistSans } from "geist/font/sans"
import { GeistMono } from "geist/font/mono"
import { Analytics } from "@vercel/analytics/next"
import { LocaleProvider } from "@/contexts/locale-context"
import "./globals.css"

export const metadata: Metadata = {
  metadataBase: new URL("https://ai-landing.yyc3.top"),
  title: {
    default: "YYC³ AI Agent Landing Page",
    template: "%s | YYC³ AI Agent Landing Page",
  },
  description: "YYC³ AI Agent Landing Page - 专业的AI代理服务展示平台",
  generator: "YYC³",
  keywords: ["YYC³", "AI Agent", "AI 代理", "Landing Page", "智能体"],
  icons: {
    icon: [
      { url: "/favicon-32.png", sizes: "32x32", type: "image/png" },
      { url: "/favicon-16.png", sizes: "16x16", type: "image/png" },
    ],
    shortcut: "/favicon-32.png",
    apple: "/apple-touch-icon.png",
  },
  openGraph: {
    type: "website",
    siteName: "YYC³ AI Agent Landing Page",
    url: "https://ai-landing.yyc3.top",
    images: [{ url: "/og-image.png", width: 512, height: 512 }],
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
