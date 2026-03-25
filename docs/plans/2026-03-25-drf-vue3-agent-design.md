# DRF-Vue3 全栈开发 Agent 设计文档

> **For Claude:** 本文档定义 Agent 架构，后续使用 writing-plans skill 创建实施计划。

**Goal:** 构建一个在 OpenCode 中运行的全栈开发 Agent，集成 Spec 解析、TDD 开发、E2E 测试、经验沉淀能力

**Architecture:** 采用组合方案 = Skills(工作流) + Config(系统提示词) + Templates(项目模板) + Knowledge(经验库)

**Tech Stack:** OpenCode Skills + DRF + Vue3 + Vite + TypeScript + MySQL + Playwright

---

## 1. Agent 架构

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenCode Agent                           │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   Skills    │  │   Config    │  │  Templates  │         │
│  │             │  │             │  │             │         │
│  │ - drf-dev   │  │ - system    │  │ - backend   │         │
│  │ - spec      │  │ - prompts   │  │ - frontend  │         │
│  │ - ui-ux     │  │ - tools     │  │ - specs     │         │
│  │ - tdd       │  │             │  │             │         │
│  │ - e2e       │  │             │  │             │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Knowledge Base (Markdown)              │   │
│  │  - decisions/  - errors/  - best-practices/         │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Skills 设计

### 2.1 核心 Skill: drf-vue3-developer

**位置:** `skills/drf-vue3-developer/SKILL.md`

**工作流:**
```
1. 需求接收 → 2. Spec 解析 → 3. 架构设计 → 4. TDD 开发 → 5. 测试验证 → 6. 经验沉淀
```

**触发方式:**
- 命令行：`/drf-dev create feature <spec-file>`
- 对话式：用户描述需求，Agent 自动识别
- 项目式：检测项目配置文件自动激活

### 2.2 子 Skill 清单

| Skill | 用途 | 调用时机 |
|-------|------|----------|
| `spec-analyzer` | 解析 Spec 模板 | 需求分析阶段 |
| `ui-ux-pro-max` | 前端设计 | 架构设计阶段 |
| `test-driven-development` | TDD 开发 | 代码实现阶段 |
| `playwright-e2e-testing` | E2E 测试 | 测试验证阶段 |
| `subagent-driven-development` | 并行执行 | 多任务执行 |
| `verification-before-completion` | 验证完成 | 每个任务完成后 |

---

## 3. Agent 配置

### 3.1 系统提示词

**位置:** `agent-config/system-prompt.md`

```markdown
你是 DRF-Vue3 全栈开发专家，专精于：
- Django REST Framework 后端开发
- Vue3 + TypeScript + Vite 前端开发
- MySQL 数据库设计
- Playwright E2E 测试
- TDD 测试驱动开发

工作原则：
1. 先读 Spec 文档，确认需求
2. 设计先行，输出架构方案
3. TDD 开发：测试→实现→重构
4. E2E 验证：确保端到端功能正常
5. 经验沉淀：记录决策和错误

可用工具：
- spec-analyzer: 解析需求规格
- ui-ux-pro-max: 前端设计
- tdd: 测试驱动开发
- playwright: E2E 测试
```

### 3.2 工具配置

**位置:** `agent-config/tools-config.yaml`

```yaml
tools:
  spec-analyzer:
    type: internal
    template_path: templates/specs/
    
  ui-ux-pro-max:
    type: skill
    skill_name: ui-ux-pro-max
    
  tdd:
    type: skill
    skill_name: test-driven-development
    
  playwright:
    type: skill
    skill_name: playwright-e2e-testing
    
  knowledge-base:
    type: internal
    storage: markdown
    paths:
      - knowledge/decisions/
      - knowledge/errors/
      - knowledge/best-practices/
```

---

## 4. 项目模板

### 4.1 后端模板 (DRF)

**位置:** `templates/backend/`

```
backend/
├── config/                 # Django 配置
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── <app_name>/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── tests/
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
└── pytest.ini
```

### 4.2 前端模板 (Vue3)

**位置:** `templates/frontend/`

```
frontend/
├── src/
│   ├── components/
│   ├── views/
│   ├── stores/            # Pinia
│   ├── api/               # API 调用
│   ├── router/
│   ├── types/             # TypeScript 类型
│   └── styles/
├── package.json
├── vite.config.ts
├── tsconfig.json
└── playwright.config.ts
```

### 4.3 Spec 模板

**位置:** `templates/specs/feature-spec-template.md`

```markdown
# 功能规格说明书

## 1. 功能概述
- 功能名称：
- 用户故事：
- 业务目标：

## 2. 数据模型
### 2.1 实体定义
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|

### 2.2 关系图
```

## 3. API 设计
### 3.1 端点列表
- `GET /api/resource/` - 列表
- `POST /api/resource/` - 创建
- `GET /api/resource/{id}/` - 详情
- `PUT /api/resource/{id}/` - 更新
- `DELETE /api/resource/{id}/` - 删除

### 3.2 请求/响应示例

## 4. 前端设计
### 4.1 页面结构
### 4.2 组件列表
### 4.3 交互流程

## 5. 测试用例
### 5.1 单元测试
### 5.2 E2E 测试

## 6. 验收标准
```

---

## 5. 经验知识库

### 5.1 目录结构

```
knowledge/
├── decisions/           # 架构决策记录 (ADRs)
│   └── YYYY-MM-DD-<topic>.md
├── errors/              # 错误模式库
│   └── <error-type>/
│       └── <error-name>.md
└── best-practices/      # 最佳实践
    └── <domain>/
        └── <practice>.md
```

### 5.2 错误模式模板

**位置:** `templates/errors/error-pattern-template.md`

```markdown
# [错误名称]

## 错误现象
[错误信息/堆栈/表现]

## 触发场景
[什么情况下会发生]

## 根因分析
[根本原因]

## 解决方案
[修复步骤]

## 预防措施
[如何避免]

## 相关代码
[文件路径和行号]

## 首次出现时间
[日期]
```

### 5.3 决策记录模板

**位置:** `templates/decisions/adr-template.md`

```markdown
# [决策标题]

## 背景
[问题描述]

## 可选方案
1. [方案 A] - 优缺点
2. [方案 B] - 优缺点
3. [方案 C] - 优缺点

## 最终决策
[选择的方案]

## 决策理由
[为什么选择这个方案]

## 影响
[对其他部分的影响]

## 时间
[决策日期]
```

---

## 6. TDD 工作流

```
┌─────────────────────────────────────────────────────────┐
│                    TDD Cycle                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Read Spec → 2. Generate Tests → 3. Run (Fail)      │
│                      ↑                    ↓            │
│  6. Document ← 5. Refactor ← 4. Implement (Pass)       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**详细步骤:**

| 步骤 | 动作 | 工具 | 输出 |
|------|------|------|------|
| 1 | 解析 Spec | spec-analyzer | 结构化需求 |
| 2 | 生成测试 | tdd | 测试文件 |
| 3 | 运行测试 (预期失败) | pytest/playwright | 失败报告 |
| 4 | 生成实现代码 | tdd | 业务代码 |
| 5 | 运行测试 (预期通过) | pytest/playwright | 通过报告 |
| 6 | 重构 + 文档 | verification | 优化代码 + 知识库 |

---

## 7. Self-Improving 机制

### 7.1 经验记录时机

| 时机 | 记录内容 | 存储位置 |
|------|----------|----------|
| 架构决策后 | 决策理由、可选方案 | knowledge/decisions/ |
| 测试失败时 | 错误模式、根因、解决方案 | knowledge/errors/ |
| 功能完成后 | 最佳实践、代码示例 | knowledge/best-practices/ |

### 7.2 经验检索机制

**检索策略:**
1. 新项目启动时，扫描 `knowledge/` 目录
2. 根据技术栈 (DRF/Vue3) 过滤相关经验
3. 在关键决策点主动推荐历史经验

**检索命令:**
```bash
# 搜索相关错误模式
grep -r "Django" knowledge/errors/

# 搜索相关最佳实践
grep -r "Vue3" knowledge/best-practices/
```

---

## 8. 使用方式

### 8.1 混合式使用

**命令行式:**
```
/drf-dev create feature specs/user-auth.md
/drf-dev test e2e
/drf-dev knowledge search "authentication error"
```

**对话式:**
```
用户：帮我创建一个用户认证功能
Agent: 好的，我来分析需求...[自动执行 Spec 解析→架构设计→TDD 开发]
```

**项目式:**
```
# 项目根目录放置 .drf-dev-config.yaml
# Agent 检测文件后自动激活
```

### 8.2 典型使用流程

```
1. 用户创建 Spec 文档：specs/user-auth.md
2. 用户执行命令：/drf-dev create feature specs/user-auth.md
3. Agent 执行:
   - 解析 Spec
   - 输出架构设计
   - TDD 开发后端 (DRF)
   - TDD 开发前端 (Vue3)
   - Playwright E2E 测试
   - 记录经验到知识库
4. 用户验收
```

---

## 9. 实施计划摘要

**阶段 1: 基础框架**
- 创建项目目录结构
- 创建核心 Skill 框架
- 创建系统提示词

**阶段 2: 模板开发**
- 后端 DRF 模板
- 前端 Vue3 模板
- Spec 模板

**阶段 3: 知识库**
- 错误模式模板
- 决策记录模板
- 最佳实践模板

**阶段 4: 集成测试**
- 端到端流程测试
- 验证 Self-Improving 机制

---

## 10. 成功标准

| 标准 | 说明 |
|------|------|
| 规范化 | 所有输出符合定义的模板和格式 |
| 自动化 | TDD 循环全自动执行，无需人工干预 |
| 可进化 | 经验知识库持续增长，支持检索和推荐 |
| 可测试 | Playwright E2E 测试覆盖率 > 80% |

---

**下一步：** 使用 `writing-plans` skill 创建详细实施计划，拆解为 bite-sized 任务。
