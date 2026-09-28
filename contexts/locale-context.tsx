"use client"

/**
 * 语言上下文提供者
 * 管理全局语言状态和切换逻辑
 */

import { createContext, useContext, useState, useEffect, type ReactNode } from "react"
import { type Locale, defaultLocale, locales, getTranslations, type Translations } from "@/lib/i18n"

interface LocaleContextType {
  locale: Locale
  setLocale: (locale: Locale) => void
  t: Translations
}

const LocaleContext = createContext<LocaleContextType | undefined>(undefined)

interface LocaleProviderProps {
  children: ReactNode
  initialLocale?: Locale
}

export function LocaleProvider({ children, initialLocale = defaultLocale }: LocaleProviderProps) {
  const [locale, setLocaleState] = useState<Locale>(initialLocale)
  const [t, setT] = useState<Translations>(getTranslations(initialLocale))

  // 从 localStorage 读取保存的语言设置
  useEffect(() => {
    const savedLocale = localStorage.getItem("locale") as Locale | null
    if (savedLocale && locales.includes(savedLocale)) {
      /* eslint-disable react-hooks/set-state-in-effect -- localStorage 水合恢复须在挂载后同步执行，SSR 无法预知 */
      setLocaleState(savedLocale)
      setT(getTranslations(savedLocale))
      /* eslint-enable react-hooks/set-state-in-effect */
    }
  }, [])

  // 切换语言并保存到 localStorage
  const setLocale = (newLocale: Locale) => {
    if (locales.includes(newLocale)) {
      setLocaleState(newLocale)
      setT(getTranslations(newLocale))
      localStorage.setItem("locale", newLocale)
      // 更新 HTML lang 属性
      document.documentElement.lang = newLocale
    }
  }

  return <LocaleContext.Provider value={{ locale, setLocale, t }}>{children}</LocaleContext.Provider>
}

/**
 * 使用语言上下文的 Hook
 */
export function useLocale() {
  const context = useContext(LocaleContext)
  if (context === undefined) {
    throw new Error("useLocale must be used within a LocaleProvider")
  }
  return context
}
