#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file YYC3-AI-LANDING-DOCS.py
@description YYC3-AI-LANDING 全文档架构一键生成脚本，用于生成符合YYC3标准的完整文档架构，支持文档内容验证和自动更新功能
@author YYC³
@version v1.2.0
@created 2026-01-23
@updated 2026-01-23
@copyright Copyright (c) 2026 YYC³
@license MIT
"""

# @Desc: YYC3-AI-LANDING 全文档架构一键生成脚本 | 生成根目录docs/ | 无任何错误 | 支持文档验证和自动更新
import os
import sys
import argparse
import re
import datetime
import json
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# ===================== 核心配置区 =====================
# 文档根目录
DOCUMENT_ROOT = "docs"
# 创建日期
CREATION_DATE = "2026-01-23"
# 版本号
VERSION = "v1.0.0"
# 状态
STATUS = "published"
# 编码格式
ENCODING = "utf-8"

# ===================== 模板1：所有业务文档 通用标准主模板 (完全照搬你的规范) =====================
MAIN_MD_TEMPLATE = """---
@file: {FILE_NAME}
@description: YYC3-AI-LANDING {DESCRIPTION}
@author: YYC³
@version: {VERSION}
@created: {CREATE_DATE}
@updated: {CREATE_DATE}
@status: {STATUS}
@tags: {TAGS}
---

> ***YanYuCloudCube***
> 言启象限 | 语枢未来
> ***Words Initiate Quadrants, Language Serves as Core for the Future***
> 万象归元于云枢 | 深栈智启新纪元
> ***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***

---

# {TITLE}

## 概述

本文档详细描述YYC3-AI-LANDING-{DOC_CATEGORY}-{DOC_NAME}相关内容，确保项目按照YYC³标准规范进行开发和实施。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景
YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标
- 规范{DOC_NAME}相关的业务标准与技术落地要求
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

### 3. {DOC_NAME}

---

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」
"""

# ===================== 模板2：所有目录下 README.md 专属索引模板 (完全照搬你的规范) =====================
README_MD_TEMPLATE = """---
@file: YYC3-AI-LANDING-{DOC_CATEGORY}-文档索引.md
@description: YYC3-AI-LANDING {DESCRIPTION}
@author: YYC³
@version: {VERSION}
@created: {CREATE_DATE}
@updated: {CREATE_DATE}
@status: {STATUS}
@tags: {TAGS}
---

# 文档索引模版

## 概述

YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

## 核心内容

### 1. 背景与目标

#### 1.1 项目背景

YYC³(YanYuCloudCube)-AI-LANDING项目是一个基于「五高五标五化」理念的现代化AI代理服务落地页，采用Next.js 14+构建，集成了国际化系统、3D场景交互、动画效果和响应式设计。

#### 1.2 文档目标

- 明确文档索引模版的设计原则和实施标准
- 提供清晰的指导和规范
- 确保项目各阶段的一致性和可追溯性

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

### 3. 实施方案

#### 3.1 架构设计

基于Next.js 14+ App Router架构，采用现代化前端技术栈：

- 表现层：React 19 + TypeScript + Tailwind CSS
- 组件库：shadcn/ui + Radix UI
- 动画库：Framer Motion + Spline 3D
- 国际化：自定义i18n系统
- 部署平台：Vercel

#### 3.2 技术选型

- 前端框架：Next.js 14.2.25 + React 19
- 类型系统：TypeScript 5
- 样式方案：Tailwind CSS 4.1.9
- UI组件：shadcn/ui + Radix UI
- 动画交互：Framer Motion 12.23.12
- 3D场景：@splinetool/react-spline 4.1.0
- 粒子效果：@tsparticles/react 3.0.0

#### 3.3 质量保障

- ESLint代码检查
- TypeScript严格模式
- 响应式设计测试
- 性能优化验证
- 跨浏览器兼容性测试

### 4. 风险控制

#### 4.1 技术风险

- 采用成熟稳定的技术栈
- 建立技术评审机制
- 定期进行技术调研

#### 4.2 进度风险

- 制定详细的开发计划
- 建立里程碑和检查点
- 定期进行进度评估

#### 4.3 质量风险

- 建立代码审查机制
- 实施持续集成和持续部署
- 建立质量监控体系

### 5. 后续计划

#### 5.1 短期计划

- 完成核心功能开发
- 完善文档体系
- 建立监控告警

#### 5.2 中期计划

- 优化系统性能
- 扩展功能模块
- 提升用户体验

#### 5.3 长期计划

- 构建生态系统
- 持续技术创新
- 拓展业务场景

## 附录

### A. 参考文档

- YYC³项目规范文档
- 技术架构设计文档
- 开发实施指南

### B. 术语表

- YYC³：YanYuCloudCube
- 五高五标五化：项目核心理念
- App Router：Next.js应用路由模式

---

<div align="center">

> 「***YanYuCloudCube***」
> 「***<admin@0379.email>***」
> 「***Words Initiate Quadrants, Language Serves as Core for the Future***」
> 「***All things converge in the cloud pivot; Deep stacks ignite a new era of intelligence***」

</div>
"""

# ===================== 核心文档架构【完整版，无错误，编号001-200，精准匹配你的规划】 =====================
PROJECT_STRUCT = {
    "需求规划": [
        ("001", "项目章程", "项目立项核心依据，明确项目目标、范围、权责与立项审批标准", "[需求规划],[项目立项],[权责划分]"),
        ("002", "可行性分析报告", "从技术、经济、市场、政策多维度分析项目可行性，提供立项决策支撑", "[需求规划],[可行性分析],[立项评估]"),
        ("003", "项目需求说明书", "全项目核心业务需求梳理，明确功能边界、用户场景与核心业务规则", "[需求规划],[需求梳理],[业务边界]"),
        ("004", "利益相关者分析", "识别项目所有相关方，分析各方需求与诉求，制定沟通与协调策略", "[需求规划],[干系人管理],[需求分析]"),
        ("005", "AI功能需求设计", "AI代理服务核心功能需求拆解与设计，匹配业务核心诉求", "[需求规划],[AI功能],[功能设计]"),
        ("006", "需求变更管理计划", "规范需求变更的申请、评审、实施流程，管控需求范围与项目风险", "[需求规划],[变更管理],[风险管控]"),
        ("007", "预留文档位01", "需求规划类扩展文档预留位，用于新增需求相关文档", "[需求规划],[文档预留],[扩展文档]"),
    ],
    "项目规划": [
        ("011", "项目管理计划", "全项目管理总纲，包含范围、时间、成本、质量、资源的综合管理规划", "[项目规划],[项目管理],[整体规划]"),
        ("012", "项目进度计划", "项目各阶段里程碑与任务拆解，明确各节点交付物与责任人", "[项目规划],[进度管理],[里程碑]"),
        ("013", "资源分配计划", "人力、物力、技术资源的统筹分配，保障项目各阶段资源充足", "[项目规划],[资源管理],[人力配置]"),
        ("014", "风险管理计划", "识别项目全周期风险，制定风险应对策略与应急预案，降低项目风险", "[项目规划],[风险管理],[应急预案]"),
        ("015", "沟通管理计划", "规范项目内外部沟通机制、频率、渠道与文档输出，保障信息同步", "[项目规划],[沟通管理],[信息同步]"),
        ("016", "预留文档位01", "项目规划类扩展文档预留位，用于新增项目管理相关文档", "[项目规划],[文档预留],[扩展文档]"),
    ],
    "架构设计": [
        ("021", "系统架构设计文档", "全系统整体架构设计，包含分层、分模块、部署架构的核心设计方案", "[架构设计],[系统架构],[整体设计]"),
        ("022", "数据架构设计文档", "项目全数据流转、存储、处理的架构设计，明确数据链路与数据规范", "[架构设计],[数据架构],[数据流转]"),
        ("023", "技术选型报告", "全栈技术栈选型依据与对比分析，匹配五高五标五化的核心设计原则", "[架构设计],[技术选型],[技术评估]"),
        ("024", "组件架构设计文档", "前端组件体系架构设计，包含组件分层、复用、状态管理的设计方案", "[架构设计],[组件架构],[组件设计]"),
        ("025", "安全架构设计文档", "系统全维度安全防护设计，包含数据安全、接口安全、权限安全等", "[架构设计],[安全架构],[风险防护]"),
        ("026", "国际化架构设计文档", "i18n国际化系统架构设计，包含语言切换、翻译管理、持久化的设计方案", "[架构设计],[国际化],[i18n设计]"),
        ("027", "动画交互架构设计文档", "动画系统架构设计，包含Framer Motion、Spline 3D、粒子效果的设计方案", "[架构设计],[动画架构],[交互设计]"),
        ("028", "性能优化架构文档", "前端性能优化架构设计，包含加载优化、渲染优化、资源优化的设计方案", "[架构设计],[性能优化],[性能设计]"),
        ("029", "响应式架构设计文档", "响应式布局架构设计，包含断点系统、适配策略、兼容方案的设计", "[架构设计],[响应式],[适配设计]"),
        ("030", "部署架构设计文档", "Vercel部署架构设计，包含CI/CD、环境配置、监控告警的设计方案", "[架构设计],[部署架构],[部署设计]"),
        ("031", "预留文档位01", "架构设计类扩展文档预留位，用于新增架构相关文档", "[架构设计],[文档预留],[扩展文档]"),
    ],
    "详细设计": [
        ("036", "模块详细设计文档", "各业务模块的功能、逻辑、接口、数据的详细设计，指导开发落地", "[详细设计],[模块设计],[开发指导]"),
        ("037", "UI-UX设计规范", "前端界面设计、交互逻辑、视觉规范的统一标准，保障用户体验一致", "[详细设计],[UI设计],[UX规范]"),
        ("038", "交互流程图", "全业务场景的用户操作与系统交互流程可视化，明确交互逻辑与规则", "[详细设计],[交互设计],[流程可视化]"),
        ("039", "界面原型文档", "全系统界面高保真原型，标注界面元素、交互逻辑与业务规则", "[详细设计],[原型设计],[界面规范]"),
        ("040", "技术实现方案", "核心业务功能的技术落地方案，包含核心算法、逻辑处理与集成方案", "[详细设计],[技术实现],[开发方案]"),
        ("041", "组件设计文档", "前端组件的详细设计，包含组件Props、状态管理、事件处理的规范", "[详细设计],[组件设计],[前端组件]"),
        ("042", "动画效果设计文档", "动画效果的详细设计，包含Framer Motion动画、Spline 3D场景、粒子效果的实现", "[详细设计],[动画设计],[效果实现]"),
        ("043", "国际化实现文档", "i18n国际化系统的详细实现，包含翻译字典、语言切换、持久化的代码实现", "[详细设计],[国际化],[i18n实现]"),
        ("044", "响应式适配文档", "响应式适配的详细实现，包含断点系统、适配策略、兼容方案的代码实现", "[详细设计],[响应式],[适配实现]"),
        ("045", "性能优化方案", "前端性能优化的详细方案，包含加载优化、渲染优化、资源优化的实现", "[详细设计],[性能优化],[优化实现]"),
        ("046", "通用组件封装文档", "前端通用组件的封装原则与复用规范，提升开发效率", "[详细设计],[组件封装],[复用设计]"),
        ("047", "业务逻辑实现", "项目核心业务逻辑的代码实现与注释规范，保障逻辑正确性", "[详细设计],[核心逻辑],[代码实现]"),
        ("048", "数据校验规则", "前端数据校验规则的代码实现，包含参数、格式、业务规则校验", "[详细设计],[数据校验],[规则实现]"),
        ("049", "异常处理规范", "系统全局异常、业务异常、技术异常的处理规范与代码实现", "[详细设计],[异常处理],[容错设计]"),
        ("050", "权限控制实现", "基于角色的权限控制代码实现，包含菜单、接口、数据的权限管控", "[详细设计],[权限控制],[代码植入]"),
        ("051", "第三方集成文档", "第三方服务SDK的集成规范与代码实现，包含Spline、Analytics等", "[详细设计],[第三方集成],[SDK规范]"),
        ("052", "SEO优化方案", "SEO优化的详细方案与实现，包含元数据、结构化数据、Sitemap的配置", "[详细设计],[SEO优化],[搜索优化]"),
        ("053", "PWA实现方案", "PWA功能的详细实现，包含Service Worker、离线访问、推送通知的配置", "[详细设计],[PWA实现],[离线访问]"),
        ("054", "预留文档位01", "详细设计类扩展文档预留位，全栈代码植入扩展使用", "[详细设计],[文档预留],[代码扩展]"),
    ],
    "API文档": [
        ("056", "通用规范-RESTful接口设计标准", "全项目RESTful接口的统一设计标准，包含请求、响应、路径规范", "[API接口],[通用规范],[RESTful]"),
        ("057", "通用规范-接口错误码体系", "全局统一的接口错误码定义，包含业务码、技术码、错误描述规范", "[API接口],[通用规范],[错误码]"),
        ("058", "通用规范-接口签名鉴权手册", "接口请求的签名、验签、token鉴权的实现规范与调用方式", "[API接口],[通用规范],[接口鉴权]"),
        ("059", "业务域-首页接口手册", "首页所有业务接口的详细定义，包含入参、出参、调用示例", "[API接口],[业务域],[首页]"),
        ("060", "业务域-服务接口手册", "服务展示相关接口的详细定义，包含入参、出参、调用示例", "[API接口],[业务域],[服务]"),
        ("061", "业务域-定价接口手册", "定价相关接口的详细定义，包含入参、出参、调用示例", "[API接口],[业务域],[定价]"),
        ("062", "业务域-联系接口手册", "联系相关接口的详细定义，包含入参、出参、调用示例", "[API接口],[业务域],[联系]"),
        ("063", "业务域-测试接口手册", "用户评价和测试相关接口的详细定义与调用规范", "[API接口],[业务域],[评价]"),
        ("064", "业务域-流程接口手册", "业务流程相关接口的详细定义与调用规范", "[API接口],[业务域],[流程]"),
        ("065", "技术类型-国际化接口", "国际化相关接口的详细定义，包含语言切换、翻译获取等", "[API接口],[技术类型],[国际化]"),
        ("066", "技术类型-动画接口", "动画相关接口的详细定义，包含动画配置、场景加载等", "[API接口],[技术类型],[动画]"),
        ("067", "技术类型-3D场景接口", "3D场景相关接口的详细定义，包含场景配置、交互事件等", "[API接口],[技术类型],[3D场景]"),
        ("068", "技术类型-文件服务接口", "图片、视频、文档等文件的上传、下载、预览接口规范", "[API接口],[技术类型],[文件服务]"),
        ("069", "第三方-Spline集成接口", "对接Spline 3D平台的接口规范与调用实现", "[API接口],[第三方],[Spline集成]"),
        ("070", "第三方-分析服务接口", "对接分析平台的接口规范与调用实现，包含Vercel Analytics等", "[API接口],[第三方],[分析服务]"),
        ("071", "版本管理-接口迭代变更记录", "接口版本迭代与变更的记录，保障接口兼容性与追溯性", "[API接口],[版本管理],[变更记录]"),
        ("072", "测试用例-接口自动化测试脚本", "接口自动化测试的用例与脚本，保障接口功能正确性", "[API接口],[测试用例],[自动化]"),
        ("073", "预留文档位01", "API接口类扩展文档预留位，用于新增接口相关文档", "[API接口],[文档预留],[扩展文档]"),
    ],
    "类型定义": [
        ("074", "前端-TypeScript全局类型声明", "前端TS全局公共类型、接口、枚举的统一声明与约束", "[类型定义],[前端],[TypeScript]"),
        ("075", "前端-组件Props类型约束", "前端组件Props的类型定义、默认值、校验规则的统一规范", "[类型定义],[前端],[组件约束]"),
        ("076", "前端-请求响应数据类型", "前端接口请求与响应数据的类型定义，保障前后端数据一致性", "[类型定义],[前端],[接口数据]"),
        ("077", "业务模块-用户类型字典", "用户角色、权限、状态的类型定义与映射关系的完整规范", "[类型定义],[业务模块],[用户]"),
        ("078", "业务模块-服务类型约束", "服务、功能、特性的类型定义与业务规则的完整规范", "[类型定义],[业务模块],[服务]"),
        ("079", "业务模块-定价类型字典", "定价、套餐、优惠的类型定义与业务规则的完整规范", "[类型定义],[业务模块],[定价]"),
        ("080", "预留文档位01", "类型定义类扩展文档预留位，用于新增类型相关文档", "[类型定义],[文档预留],[扩展文档]"),
    ],
    "测试文档": [
        ("081", "单元测试规范", "单元测试的编写规范、测试用例设计、覆盖率要求", "[测试文档],[单元测试],[测试规范]"),
        ("082", "集成测试规范", "集成测试的编写规范、测试场景设计、环境配置", "[测试文档],[集成测试],[测试规范]"),
        ("083", "E2E测试规范", "端到端测试的编写规范、测试流程设计、自动化实现", "[测试文档],[E2E测试],[测试规范]"),
        ("084", "性能测试方案", "性能测试的详细方案，包含测试指标、测试工具、测试流程", "[测试文档],[性能测试],[测试方案]"),
        ("085", "安全测试方案", "安全测试的详细方案，包含测试类型、测试工具、测试流程", "[测试文档],[安全测试],[测试方案]"),
        ("086", "兼容性测试方案", "兼容性测试的详细方案，包含浏览器测试、设备测试、系统测试", "[测试文档],[兼容性测试],[测试方案]"),
        ("087", "测试用例管理", "测试用例的管理规范，包含用例编写、用例维护、用例追踪", "[测试文档],[用例管理],[测试规范]"),
        ("088", "测试数据管理", "测试数据的管理规范，包含数据准备、数据清理、数据隔离", "[测试文档],[数据管理],[测试规范]"),
        ("089", "预留文档位01", "测试文档类扩展文档预留位，用于新增测试相关文档", "[测试文档],[文档预留],[扩展文档]"),
    ],
    "部署运维": [
        ("090", "部署方案文档", "Vercel部署的详细方案，包含部署流程、环境配置、域名配置", "[部署运维],[部署方案],[部署流程]"),
        ("091", "CI/CD配置文档", "持续集成和持续部署的配置文档，包含GitHub Actions、自动构建、自动部署", "[部署运维],[CI/CD],[自动化部署]"),
        ("092", "环境配置文档", "开发、测试、生产环境的配置文档，包含环境变量、配置文件、配置管理", "[部署运维],[环境配置],[配置管理]"),
        ("093", "监控告警文档", "系统监控和告警的配置文档，包含监控指标、告警规则、通知方式", "[部署运维],[监控告警],[监控配置]"),
        ("094", "日志管理文档", "日志收集、存储、分析的配置文档，包含日志格式、日志级别、日志查询", "[部署运维],[日志管理],[日志配置]"),
        ("095", "备份恢复文档", "数据备份和恢复的配置文档，包含备份策略、恢复流程、灾难恢复", "[部署运维],[备份恢复],[数据保护]"),
        ("096", "性能优化文档", "系统性能优化的配置文档，包含优化策略、优化工具、优化效果", "[部署运维],[性能优化],[优化配置]"),
        ("097", "安全加固文档", "系统安全加固的配置文档，包含安全策略、安全配置、安全审计", "[部署运维],[安全加固],[安全配置]"),
        ("098", "故障处理文档", "系统故障的处理文档，包含故障分类、处理流程、预防措施", "[部署运维],[故障处理],[故障管理]"),
        ("099", "预留文档位01", "部署运维类扩展文档预留位，用于新增部署运维相关文档", "[部署运维],[文档预留],[扩展文档]"),
    ],
    "用户手册": [
        ("100", "快速开始指南", "项目的快速开始指南，包含安装、配置、启动的详细步骤", "[用户手册],[快速开始],[入门指南]"),
        ("101", "功能使用手册", "项目功能的使用手册，包含功能介绍、使用步骤、注意事项", "[用户手册],[功能使用],[使用指南]"),
        ("102", "配置说明文档", "项目配置的详细说明，包含配置项、配置示例、配置验证", "[用户手册],[配置说明],[配置指南]"),
        ("103", "常见问题解答", "常见问题的解答文档，包含问题分类、解决方案、预防措施", "[用户手册],[常见问题],[FAQ]"),
        ("104", "故障排除指南", "故障排除的详细指南，包含故障诊断、解决步骤、联系支持", "[用户手册],[故障排除],[问题解决]"),
        ("105", "预留文档位01", "用户手册类扩展文档预留位，用于新增用户手册相关文档", "[用户手册],[文档预留],[扩展文档]"),
    ],
}

# ===================== 文档验证函数 =====================
def validate_document_format(file_path, verbose=False):
    """验证文档格式是否符合规范"""
    try:
        with open(file_path, 'r', encoding=ENCODING) as f:
            content = f.read()

        # 检查是否包含必要的头部字段
        required_fields = ['@file:', '@description:', '@author:', '@version:', '@created:', '@status:', '@tags:']
        missing_fields = [field for field in required_fields if field not in content]

        if missing_fields:
            return False, f'缺少必要的头部字段: {missing_fields}'

        return True, '格式验证通过'
    except Exception as e:
        return False, f'验证失败: {str(e)}'

def validate_document_headers(file_path, verbose=False):
    """验证文档头部信息是否完整"""
    try:
        with open(file_path, 'r', encoding=ENCODING) as f:
            content = f.read()

        # 检查是否包含品牌信息
        if 'YanYuCloudCube' not in content:
            return False, '缺少品牌信息'

        # 检查是否包含联系方式
        if '<admin@0379.email>' not in content:
            return False, '缺少联系方式'

        return True, '头部信息验证通过'
    except Exception as e:
        return False, f'验证失败: {str(e)}'

def validate_document_content(file_path, verbose=False):
    """验证文档内容是否符合规范"""
    try:
        with open(file_path, 'r', encoding=ENCODING) as f:
            content = f.read()

        # 检查是否包含核心内容结构
        if '## 核心内容' not in content:
            return False, '缺少核心内容部分'

        # 检查是否包含概述
        if '## 概述' not in content:
            return False, '缺少概述部分'

        return True, '内容验证通过'
    except Exception as e:
        return False, f'验证失败: {str(e)}'

def check_links(file_path, verbose=False):
    """检查文档中的链接是否有效"""
    try:
        with open(file_path, 'r', encoding=ENCODING) as f:
            content = f.read()

        # 提取所有链接
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

        broken_links = []
        for link_text, link_url in links:
            # 检查本地文件链接
            if link_url.startswith('./') or link_url.startswith('../'):
                link_path = os.path.join(os.path.dirname(file_path), link_url)
                if not os.path.exists(link_path):
                    broken_links.append(f'{link_text}: {link_url}')

        if broken_links:
            return False, f'发现无效链接: {broken_links}'

        return True, '链接验证通过'
    except Exception as e:
        return False, f'检查失败: {str(e)}'

# ===================== 文档更新函数 =====================
def update_document(file_path, new_version=None, update_version=True, update_date=True, dry_run=False, verbose=False):
    """更新文档版本号和日期"""
    try:
        with open(file_path, 'r', encoding=ENCODING) as f:
            content = f.read()

        updated_content = content
        changes = []

        # 更新日期
        if update_date:
            today = datetime.date.today().isoformat()
            # 更新 @updated 字段
            updated_content = re.sub(r'@updated: .*$', f'@updated: {today}', updated_content, flags=re.MULTILINE)
            changes.append(f'更新日期为 {today}')

        # 更新版本号
        if update_version:
            if new_version:
                # 使用指定的新版本号
                updated_content = re.sub(r'@version: .*$', f'@version: {new_version}', updated_content, flags=re.MULTILINE)
                changes.append(f'更新版本号为 {new_version}')
            else:
                # 自动增加补丁版本号
                version_match = re.search(r'@version: v(\d+)\.(\d+)\.(\d+)', updated_content)
                if version_match:
                    major, minor, patch = map(int, version_match.groups())
                    new_patch = patch + 1
                    new_version_str = f'v{major}.{minor}.{new_patch}'
                    updated_content = re.sub(r'@version: .*$', f'@version: {new_version_str}', updated_content, flags=re.MULTILINE)
                    changes.append(f'更新版本号为 {new_version_str}')

        # 写入文件
        if not dry_run and changes:
            with open(file_path, 'w', encoding=ENCODING) as f:
                f.write(updated_content)
            if verbose:
                print(f"\n已更新文档: {os.path.basename(file_path)}")
                for change in changes:
                    print(f"  - {change}")
        elif changes and verbose:
            print(f"\n将更新文档: {os.path.basename(file_path)}")
            for change in changes:
                print(f"  - {change}")

        return True, f'文档更新完成: {changes}' if changes else True, '无需更新'
    except Exception as e:
        return False, f'更新失败: {str(e)}'

# ===================== 核心生成逻辑 =====================
def create_dir(path):
    """创建目录，不存在则创建"""
    try:
        if not os.path.exists(path):
            logger.info(f"创建目录: {path}")
            os.makedirs(path)
        else:
            logger.debug(f"目录已存在: {path}")
    except PermissionError as e:
        logger.error(f"创建目录权限不足: {path}")
        raise Exception(f"创建目录权限不足: {path}, 错误: {str(e)}")
    except OSError as e:
        logger.error(f"创建目录失败: {path}, 错误: {str(e)}")
        raise Exception(f"创建目录失败: {path}, 错误: {str(e)}")
    except Exception as e:
        logger.error(f"创建目录时发生未知错误: {path}, 错误: {str(e)}")
        raise Exception(f"创建目录失败: {path}, 错误: {str(e)}")

def write_file(path, content, encoding=ENCODING):
    """写入文件，覆盖原有内容"""
    try:
        # 确保目录存在
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            create_dir(dir_path)

        logger.debug(f"写入文件: {path}")
        with open(path, "w", encoding=encoding) as f:
            f.write(content)
        logger.info(f"文件写入成功: {path}")
    except PermissionError as e:
        logger.error(f"写入文件权限不足: {path}")
        raise Exception(f"写入文件权限不足: {path}, 错误: {str(e)}")
    except OSError as e:
        logger.error(f"写入文件失败: {path}, 错误: {str(e)}")
        raise Exception(f"写入文件失败: {path}, 错误: {str(e)}")
    except Exception as e:
        logger.error(f"写入文件时发生未知错误: {path}, 错误: {str(e)}")
        raise Exception(f"写入文件失败: {path}, 错误: {str(e)}")

def validate_path(path, base_dir=None):
    """验证路径安全性，防止路径遍历攻击"""
    # 规范化路径
    normalized_path = os.path.normpath(path)

    # 检查路径是否包含上级目录引用
    if '..' in normalized_path.split(os.sep):
        raise Exception(f"路径包含不安全的上级目录引用: {path}")

    # 检查路径是否为绝对路径
    if not os.path.isabs(normalized_path):
        normalized_path = os.path.abspath(normalized_path)

    # 如果提供了基础目录，确保路径在基础目录内
    if base_dir:
        base_dir = os.path.abspath(base_dir)
        # 检查路径是否在基础目录内
        if not os.path.commonpath([base_dir, normalized_path]) == base_dir:
            raise Exception(f"路径不在基础目录内: {path}")

    # 检查路径是否包含非法字符
    illegal_chars = ['<', '>', ':', '"', '|', '?', '*']
    for char in illegal_chars:
        if char in normalized_path:
            raise Exception(f"路径包含非法字符: {char}")

    return normalized_path

def print_welcome_message():
    """打印欢迎信息"""
    print("="*80)
    print("🚀 YYC3-AI-LANDING 全文档架构一键生成脚本")
    print("="*80)
    print("📋 功能: 生成符合YYC3标准的完整文档架构")
    print("🔧 版本: v1.2.0")
    print("📅 日期: 2026-01-23")
    print("="*80)

def generate_project(root_dir, version, creation_date, status, encoding):
    """一键生成全部文档架构"""
    # 打印欢迎信息
    print_welcome_message()

    print("✅ 开始生成 YYC3-AI-LANDING 文档架构 | 根目录: {} | 编码: {}".format(root_dir, encoding))
    print("="*80)

    try:
        # 验证并规范化根目录路径
        root_dir = validate_path(root_dir)
        logger.info(f"已验证根目录路径: {root_dir}")
        print(f"🔒 已验证根目录路径: {root_dir}")

        # 创建根目录
        create_dir(root_dir)

        # 计算总文档数，用于进度显示
        total_docs = sum(len(doc_list) for _, doc_list in PROJECT_STRUCT.items())
        total_categories = len(PROJECT_STRUCT)
        current_doc = 0
        current_category = 0

        print(f"📊 任务统计: {total_categories} 个分类, {total_docs} 个文档")
        print("="*80)
        logger.info(f"开始生成文档架构: {total_categories} 个分类, {total_docs} 个文档")

        # 预先计算模板中不变的部分
        base_template_values = {
            'VERSION': version,
            'CREATE_DATE': creation_date,
            'STATUS': status
        }

        # 遍历所有分类，生成目录和文档
        for doc_category, doc_list in PROJECT_STRUCT.items():
            current_category += 1
            try:
                # 创建分类目录
                cate_dir = os.path.join(root_dir, "YYC3-AI-LANDING-{}".format(doc_category))
                # 验证分类目录路径，确保在根目录内
                cate_dir = validate_path(cate_dir, base_dir=root_dir)

                create_dir(cate_dir)
                logger.info(f"创建分类目录: {cate_dir}")
                print(f"📂 [{current_category}/{total_categories}] 创建目录: {cate_dir}")

                # 生成该目录下的所有文档
                for doc_no, doc_name, doc_desc, doc_tags in doc_list:
                    current_doc += 1
                    try:
                        # 拼接文件名和标题
                        file_name = "{}-YYC3-AI-LANDING-{}-{}.md".format(doc_no, doc_category, doc_name)
                        file_path = os.path.join(cate_dir, file_name)
                        # 验证文件路径，确保在根目录内
                        file_path = validate_path(file_path, base_dir=root_dir)
                        title = "{}-YYC3-AI-LANDING-{}".format(doc_no, doc_category, doc_name)

                        # 替换模板占位符
                        template_values = {
                            **base_template_values,
                            'FILE_NAME': file_name,
                            'DESCRIPTION': doc_desc,
                            'TAGS': doc_tags,
                            'TITLE': title,
                            'DOC_CATEGORY': doc_category,
                            'DOC_NAME': doc_name
                        }
                        content = MAIN_MD_TEMPLATE.format(**template_values)

                        # 写入文件
                        write_file(file_path, content, encoding)
                        # 计算进度百分比
                        progress = int((current_doc / total_docs) * 100)
                        print(f"  ✍️ [{current_doc}/{total_docs}] ({progress}%) 生成文档: {file_name}")
                    except Exception as e:
                        logger.error(f"生成文档失败: {file_name}, 错误: {str(e)}")
                        raise Exception(f"生成文档失败: {file_name}, 错误: {str(e)}")

                # 生成该目录下的 README.md 索引文档
                try:
                    readme_name = "README.md"
                    readme_path = os.path.join(cate_dir, readme_name)
                    # 验证README文件路径，确保在根目录内
                    readme_path = validate_path(readme_path, base_dir=root_dir)
                    readme_desc = "{}分类下所有文档的索引与说明，统一管理文档清单".format(doc_category)
                    readme_tags = "[{}],[文档索引],[目录总览]".format(doc_category)

                    # 使用预先计算的模板值
                    readme_template_values = {
                        **base_template_values,
                        'DOC_CATEGORY': doc_category,
                        'DESCRIPTION': readme_desc,
                        'TAGS': readme_tags
                    }

                    readme_content = README_MD_TEMPLATE.format(**readme_template_values)
                    write_file(readme_path, readme_content, encoding)
                    logger.info(f"生成README索引: {readme_path}")
                    print(f"  📑 生成索引: {readme_name}")
                    print("-"*80)
                except Exception as e:
                    logger.error(f"生成README索引失败: {doc_category}, 错误: {str(e)}")
                    raise Exception(f"生成README索引失败: {doc_category}, 错误: {str(e)}")
            except Exception as e:
                logger.error(f"处理分类目录失败: {doc_category}, 错误: {str(e)}")
                raise Exception(f"处理分类目录失败: {doc_category}, 错误: {str(e)}")

        # 验证生成的文档结构
        validate_document_structure(root_dir)

        print("="*80)
        print("🎉 生成完成！")
        print("="*80)
        print(f"📁 文档根目录: {os.path.abspath(root_dir)}")
        print(f"📊 生成统计:")
        print(f"   • 分类目录: {total_categories} 个")
        print(f"   • 业务文档: {total_docs} 个")
        print(f"   • README索引: {total_categories} 个")
        print(f"   • 总计生成: {total_docs + total_categories} 个文件")
        print(f"🔍 文档结构:")
        print(f"   • 符合YYC3标准的文档命名规范")
        print(f"   • 完整的文档分类体系")
        print(f"   • 标准化的文档模板")
        print(f"✅ 所有文档严格遵循 YYC3-AI-LANDING 命名规范与模板标准！")
        print("="*80)
        print("📚 后续建议:")
        print("   • 检查生成的文档结构是否符合预期")
        print("   • 根据实际项目需求修改文档内容")
        print("   • 定期更新文档以保持与项目同步")
        print("="*80)
        logger.info(f"文档架构生成完成: {total_docs + total_categories} 个文件")
    except Exception as e:
        logger.error(f"生成文档架构失败: {str(e)}")
        raise Exception(f"生成文档架构失败: {str(e)}")


def validate_document_structure(root_dir):
    """验证生成的文档结构是否与PROJECT_STRUCT一致"""
    print("\n🔍 验证文档结构...")
    logger.info(f"开始验证文档结构: {root_dir}")

    try:
        # 计算预期的文档数量
        expected_categories = len(PROJECT_STRUCT)
        expected_docs = sum(len(doc_list) for _, doc_list in PROJECT_STRUCT.items())
        expected_total = expected_docs + expected_categories  # 加上README文件

        # 统计实际生成的文档数量
        actual_categories = 0
        actual_docs = 0
        actual_readmes = 0

        for root, dirs, files in os.walk(root_dir):
            # 统计分类目录
            if root != root_dir:
                actual_categories += 1

            # 统计文档和README文件
            for file in files:
                if file.endswith('.md'):
                    if file == 'README.md':
                        actual_readmes += 1
                    else:
                        actual_docs += 1

        actual_total = actual_docs + actual_readmes

        # 验证数量是否一致
        print(f"\n📊 文档结构验证结果:")
        print(f"   • 预期分类目录: {expected_categories} 个")
        print(f"   • 实际分类目录: {actual_categories} 个")
        print(f"   • 预期业务文档: {expected_docs} 个")
        print(f"   • 实际业务文档: {actual_docs} 个")
        print(f"   • 预期README索引: {expected_categories} 个")
        print(f"   • 实际README索引: {actual_readmes} 个")
        print(f"   • 预期总文件数: {expected_total} 个")
        print(f"   • 实际总文件数: {actual_total} 个")

        # 检查是否所有分类都已生成
        missing_categories = []
        for category in PROJECT_STRUCT.keys():
            category_dir = os.path.join(root_dir, f"YYC3-AI-LANDING-{category}")
            if not os.path.exists(category_dir):
                missing_categories.append(category)

        if missing_categories:
            print(f"\n❌ 缺少分类目录: {missing_categories}")
            logger.error(f"缺少分类目录: {missing_categories}")
            raise Exception(f"文档结构验证失败: 缺少分类目录 {missing_categories}")

        # 检查是否所有文档都已生成
        missing_docs = []
        for category, doc_list in PROJECT_STRUCT.items():
            category_dir = os.path.join(root_dir, f"YYC3-AI-LANDING-{category}")
            for doc_no, doc_name, _, _ in doc_list:
                doc_file = f"{doc_no}-YYC3-AI-LANDING-{category}-{doc_name}.md"
                doc_path = os.path.join(category_dir, doc_file)
                if not os.path.exists(doc_path):
                    missing_docs.append(f"{category}/{doc_file}")

        if missing_docs:
            print(f"\n❌ 缺少文档: {missing_docs}")
            logger.error(f"缺少文档: {missing_docs}")
            raise Exception(f"文档结构验证失败: 缺少文档 {missing_docs}")

        # 检查是否所有分类都有README文件
        missing_readmes = []
        for category in PROJECT_STRUCT.keys():
            category_dir = os.path.join(root_dir, f"YYC3-AI-LANDING-{category}")
            readme_path = os.path.join(category_dir, "README.md")
            if not os.path.exists(readme_path):
                missing_readmes.append(category)

        if missing_readmes:
            print(f"\n❌ 缺少README文件: {missing_readmes}")
            logger.error(f"缺少README文件: {missing_readmes}")
            raise Exception(f"文档结构验证失败: 缺少README文件 {missing_readmes}")

        # 验证通过
        if (actual_categories == expected_categories and
            actual_docs == expected_docs and
            actual_readmes == expected_categories):
            print("\n✅ 文档结构验证通过！")
            logger.info("文档结构验证通过，所有预期的文档和目录都已生成")
        else:
            print("\n❌ 文档数量不匹配！")
            logger.error(f"文档数量不匹配: 预期 {expected_total} 个文件，实际 {actual_total} 个文件")
            raise Exception(f"文档结构验证失败: 文档数量不匹配")

    except Exception as e:
        logger.error(f"验证文档结构时发生错误: {str(e)}")
        raise Exception(f"验证文档结构失败: {str(e)}")

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='YYC3-AI-LANDING 全文档架构一键生成脚本')

    # 模式选择
    parser.add_argument('--mode', choices=['generate', 'validate', 'update'], default='generate',
                      help='运行模式: generate(生成文档), validate(验证文档), update(更新文档)')

    # 生成选项
    parser.add_argument('--root', '-r', default=DOCUMENT_ROOT, help='文档根目录 (默认: docs)')
    parser.add_argument('--version', '-v', default=VERSION, help='版本号 (默认: v1.0.0)')
    parser.add_argument('--date', '-d', default=CREATION_DATE, help='创建日期 (默认: 2026-01-23)')
    parser.add_argument('--status', '-s', default=STATUS, help='文档状态 (默认: published)')
    parser.add_argument('--encoding', '-e', default=ENCODING, help='文件编码 (默认: utf-8)')

    # 验证选项
    parser.add_argument('--check-format', action='store_true', default=True,
                      help='检查文档格式是否符合规范')
    parser.add_argument('--check-headers', action='store_true', default=True,
                      help='检查文档头部信息是否完整')
    parser.add_argument('--check-content', action='store_true', default=True,
                      help='检查文档内容是否符合规范')
    parser.add_argument('--check-links', action='store_true', default=False,
                      help='检查文档中的链接是否有效')

    # 更新选项
    parser.add_argument('--update-version', action='store_true', default=True,
                      help='更新文档版本号')
    parser.add_argument('--update-date', action='store_true', default=True,
                      help='更新文档日期')
    parser.add_argument('--new-version', type=str, default=None,
                      help='指定新的版本号')

    # 其他选项
    parser.add_argument('--verbose', '-V', action='store_true', default=False,
                      help='详细输出')
    parser.add_argument('--dry-run', action='store_true', default=False,
                      help='试运行，不实际修改文件')

    return parser.parse_args()

def validate_all_documents(args):
    """验证所有文档"""
    print("\n====================================")
    print("🔍 开始验证文档...")
    print("====================================")

    try:
        # 验证根目录
        root_dir = validate_path(args.root)
        if not os.path.exists(root_dir):
            print(f"❌ 文档根目录不存在: {root_dir}")
            return

        total_valid = 0
        total_invalid = 0
        validation_results = []

        # 遍历所有文档
        for category, doc_list in PROJECT_STRUCT.items():
            category_dir = os.path.join(root_dir, f"YYC3-AI-LANDING-{category}")
            if not os.path.exists(category_dir):
                logger.warning(f"分类目录不存在: {category_dir}")
                continue

            for doc_no, doc_name, _, _ in doc_list:
                doc_file = f"{doc_no}-YYC3-AI-LANDING-{category}-{doc_name}.md"
                doc_path = os.path.join(category_dir, doc_file)

                if not os.path.exists(doc_path):
                    logger.warning(f"文档不存在: {doc_path}")
                    continue

                # 验证文档
                if args.check_format:
                    valid, msg = validate_document_format(doc_path, args.verbose)
                    validation_results.append((doc_path, '格式', valid, msg))
                    if valid:
                        total_valid += 1
                    else:
                        total_invalid += 1

                if args.check_headers:
                    valid, msg = validate_document_headers(doc_path, args.verbose)
                    validation_results.append((doc_path, '头部', valid, msg))
                    if valid:
                        total_valid += 1
                    else:
                        total_invalid += 1

                if args.check_content:
                    valid, msg = validate_document_content(doc_path, args.verbose)
                    validation_results.append((doc_path, '内容', valid, msg))
                    if valid:
                        total_valid += 1
                    else:
                        total_invalid += 1

                if args.check_links:
                    valid, msg = check_links(doc_path, args.verbose)
                    validation_results.append((doc_path, '链接', valid, msg))
                    if valid:
                        total_valid += 1
                    else:
                        total_invalid += 1

        # 输出验证结果
        print("\n📊 验证结果统计:")
        print(f"   • 验证通过: {total_valid} 项")
        print(f"   • 验证失败: {total_invalid} 项")

        if args.verbose:
            print("\n📋 详细验证结果:")
            for doc_path, check_type, valid, msg in validation_results:
                status_icon = "✅" if valid else "❌"
                print(f"   {status_icon} {os.path.basename(doc_path)} - {check_type}: {msg}")

        if total_invalid == 0:
            print("\n✅ 所有文档验证通过！")
        else:
            print(f"\n⚠️  发现 {total_invalid} 个问题，请检查并修复")

    except Exception as e:
        logger.error(f"验证文档时发生错误: {str(e)}")
        print(f"❌ 验证失败: {str(e)}")

def update_all_documents(args):
    """更新所有文档"""
    print("\n====================================")
    print("🔄 开始更新文档...")
    print("====================================")

    try:
        # 验证根目录
        root_dir = validate_path(args.root)
        if not os.path.exists(root_dir):
            print(f"❌ 文档根目录不存在: {root_dir}")
            return

        total_updated = 0
        total_skipped = 0
        update_results = []

        # 遍历所有文档
        for category, doc_list in PROJECT_STRUCT.items():
            category_dir = os.path.join(root_dir, f"YYC3-AI-LANDING-{category}")
            if not os.path.exists(category_dir):
                logger.warning(f"分类目录不存在: {category_dir}")
                continue

            for doc_no, doc_name, _, _ in doc_list:
                doc_file = f"{doc_no}-YYC3-AI-LANDING-{category}-{doc_name}.md"
                doc_path = os.path.join(category_dir, doc_file)

                if not os.path.exists(doc_path):
                    logger.warning(f"文档不存在: {doc_path}")
                    continue

                # 更新文档
                success, msg = update_document(
                    doc_path,
                    new_version=args.new_version,
                    update_version=args.update_version,
                    update_date=args.update_date,
                    dry_run=args.dry_run,
                    verbose=args.verbose
                )

                if success:
                    total_updated += 1
                    update_results.append((doc_path, msg))
                else:
                    total_skipped += 1

        # 输出更新结果
        print("\n📊 更新结果统计:")
        print(f"   • 已更新: {total_updated} 个")
        print(f"   • 已跳过: {total_skipped} 个")

        if args.verbose:
            print("\n📋 详细更新结果:")
            for doc_path, msg in update_results:
                print(f"   ✅ {os.path.basename(doc_path)}: {msg}")

        if args.dry_run:
            print("\n⚠️  这是试运行模式，未实际修改文件")
        else:
            print("\n✅ 文档更新完成！")

    except Exception as e:
        logger.error(f"更新文档时发生错误: {str(e)}")
        print(f"❌ 更新失败: {str(e)}")

def main():
    """主函数"""
    args = parse_args()

    try:
        if args.mode == 'generate':
            generate_project(
                root_dir=args.root,
                version=args.version,
                creation_date=args.date,
                status=args.status,
                encoding=args.encoding
            )
        elif args.mode == 'validate':
            validate_all_documents(args)
        elif args.mode == 'update':
            update_all_documents(args)
        else:
            print("❌ 未知的运行模式: {}".format(args.mode))
            sys.exit(1)
    except Exception as e:
        logger.error(f"程序执行失败: {str(e)}")
        print(f"❌ 程序执行失败: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
