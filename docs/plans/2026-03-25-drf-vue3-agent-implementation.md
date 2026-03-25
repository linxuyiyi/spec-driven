# DRF-Vue3 全栈开发 Agent 实施计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 构建一个在 OpenCode 中运行的全栈开发 Agent，集成 Spec 解析、TDD 开发、E2E 测试、经验沉淀能力

**Architecture:** 组合方案 = Skills(工作流) + Config(系统提示词) + Templates(项目模板) + Knowledge(经验库)

**Tech Stack:** OpenCode Skills + DRF + Vue3 + Vite + TypeScript + MySQL + Playwright

---

## 阶段 1: 项目骨架

### Task 1: 创建项目目录结构

**Files:**
- Create: `skills/drf-vue3-developer/`
- Create: `skills/spec-analyzer/`
- Create: `agent-config/`
- Create: `templates/backend/`
- Create: `templates/frontend/`
- Create: `templates/specs/`
- Create: `templates/errors/`
- Create: `templates/decisions/`
- Create: `templates/best-practices/`
- Create: `knowledge/decisions/`
- Create: `knowledge/errors/`
- Create: `knowledge/best-practices/`
- Create: `scripts/`

**Step 1: 创建所有目录**

```bash
mkdir -p skills/drf-vue3-developer skills/spec-analyzer agent-config
mkdir -p templates/backend templates/frontend templates/specs
mkdir -p templates/errors templates/decisions templates/best-practices
mkdir -p knowledge/decisions knowledge/errors knowledge/best-practices
mkdir -p scripts
```

Expected: 所有目录创建成功

**Step 2: 验证目录结构**

```bash
tree -L 2 /Users/niuniu/程序/myagent
```

Expected: 显示完整的目录树

**Step 3: 创建 .gitignore**

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.pyo
.env
.venv/
venv/

# Node
node_modules/
dist/
*.log

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Test
.pytest_cache/
.coverage
htmlcov/
EOF
```

**Step 4: 提交**

```bash
git init
git add .
git commit -m "feat: 初始化项目骨架"
```

---

## 阶段 2: 核心 Skill 开发

### Task 2: 创建核心 Skill: drf-vue3-developer

**Files:**
- Create: `skills/drf-vue3-developer/SKILL.md`

**Step 1: 创建核心 Skill 文件**

内容包含：
- 工作流定义 (Spec 解析→架构设计→TDD 开发→测试验证→经验沉淀)
- 触发方式 (命令行/对话式/项目式)
- 子 Skill 调用规则
- 上下文管理规则

**Step 2: 验证 Skill 语法**

检查 Markdown 格式是否正确

**Step 3: 提交**

```bash
git add skills/drf-vue3-developer/SKILL.md
git commit -m "feat: 创建核心开发 Skill"
```

---

### Task 3: 创建 Spec Analyzer Skill

**Files:**
- Create: `skills/spec-analyzer/SKILL.md`
- Create: `templates/specs/feature-spec-template.md`

**Step 1: 创建 Spec 解析 Skill**

内容包含：
- Spec 模板解析逻辑
- 需求提取规则
- 数据模型识别
- API 端点识别

**Step 2: 创建 Spec 模板**

内容包含：
- 功能概述
- 数据模型
- API 设计
- 前端设计
- 测试用例
- 验收标准

**Step 3: 提交**

```bash
git add skills/spec-analyzer/SKILL.md templates/specs/feature-spec-template.md
git commit -m "feat: 创建 Spec 解析 Skill 和模板"
```

---

## 阶段 3: Agent 配置

### Task 4: 创建系统提示词

**Files:**
- Create: `agent-config/system-prompt.md`

**Step 1: 创建系统提示词**

内容包含：
- 角色定义 (DRF-Vue3 全栈专家)
- 工作原则 (Spec→设计→TDD→测试→沉淀)
- 可用工具列表
- 输出格式规范

**Step 2: 提交**

```bash
git add agent-config/system-prompt.md
git commit -m "feat: 创建系统提示词"
```

---

### Task 5: 创建工具配置

**Files:**
- Create: `agent-config/tools-config.yaml`

**Step 1: 创建工具配置文件**

内容包含：
- 工具列表 (spec-analyzer, ui-ux-pro-max, tdd, playwright)
- 工具类型 (internal/skill)
- 工具参数配置
- 工具调用顺序

**Step 2: 验证 YAML 语法**

```bash
python -c "import yaml; yaml.safe_load(open('agent-config/tools-config.yaml'))"
```

Expected: 无错误输出

**Step 3: 提交**

```bash
git add agent-config/tools-config.yaml
git commit -m "feat: 创建工具配置"
```

---

## 阶段 4: 项目模板开发

### Task 6: 创建后端 DRF 模板

**Files:**
- Create: `templates/backend/config/settings/base.py`
- Create: `templates/backend/config/settings/dev.py`
- Create: `templates/backend/config/settings/prod.py`
- Create: `templates/backend/config/urls.py`
- Create: `templates/backend/apps/__init__.py`
- Create: `templates/backend/requirements/base.txt`
- Create: `templates/backend/requirements/dev.txt`
- Create: `templates/backend/pytest.ini`
- Create: `templates/backend/manage.py`

**Step 1: 创建 Django 配置文件**

包含 settings/base.py, dev.py, prod.py

**Step 2: 创建 requirements 文件**

包含 Django, DRF, pytest 等依赖

**Step 3: 创建 pytest 配置**

**Step 4: 提交**

```bash
git add templates/backend/
git commit -m "feat: 创建 DRF 后端模板"
```

---

### Task 7: 创建前端 Vue3 模板

**Files:**
- Create: `templates/frontend/package.json`
- Create: `templates/frontend/vite.config.ts`
- Create: `templates/frontend/tsconfig.json`
- Create: `templates/frontend/src/main.ts`
- Create: `templates/frontend/src/App.vue`
- Create: `templates/frontend/playwright.config.ts`

**Step 1: 创建 package.json**

包含 Vue3, Vite, TypeScript, Pinia, Element Plus 依赖

**Step 2: 创建 Vite 配置**

**Step 3: 创建 TypeScript 配置**

**Step 4: 创建 Playwright 配置**

**Step 5: 提交**

```bash
git add templates/frontend/
git commit -m "feat: 创建 Vue3 前端模板"
```

---

## 阶段 5: 经验知识库

### Task 8: 创建知识库模板

**Files:**
- Create: `templates/errors/error-pattern-template.md`
- Create: `templates/decisions/adr-template.md`
- Create: `templates/best-practices/practice-template.md`

**Step 1: 创建错误模式模板**

包含：错误现象、触发场景、根因分析、解决方案、预防措施

**Step 2: 创建决策记录模板**

包含：背景、可选方案、最终决策、决策理由、影响

**Step 3: 创建最佳实践模板**

包含：场景描述、实践内容、代码示例、参考链接

**Step 4: 创建示例条目**

创建至少一个示例错误模式、决策记录、最佳实践

**Step 5: 提交**

```bash
git add templates/errors/ templates/decisions/ templates/best-practices/
git commit -m "feat: 创建知识库模板"
```

---

## 阶段 6: Self-Improving 机制

### Task 9: 创建经验记录脚本

**Files:**
- Create: `scripts/record-decision.py`
- Create: `scripts/record-error.py`
- Create: `scripts/search-knowledge.py`

**Step 1: 创建决策记录脚本**

命令行工具，接收决策信息，生成 Markdown 文件到 knowledge/decisions/

**Step 2: 创建错误记录脚本**

命令行工具，接收错误信息，生成 Markdown 文件到 knowledge/errors/

**Step 3: 创建知识检索脚本**

命令行工具，支持关键词搜索、标签过滤

**Step 4: 测试脚本**

```bash
python scripts/record-decision.py --help
python scripts/record-error.py --help
python scripts/search-knowledge.py --help
```

**Step 5: 提交**

```bash
git add scripts/
git commit -m "feat: 创建知识管理脚本"
```

---

## 阶段 7: 集成测试

### Task 10: 端到端流程测试

**Files:**
- Create: `tests/e2e/test-agent-flow.py`

**Step 1: 创建测试 Spec**

创建一个示例功能 Spec 文档

**Step 2: 执行完整流程**

Spec 解析 → 架构设计 → TDD 开发 → E2E 测试 → 经验沉淀

**Step 3: 验证输出**

检查生成的代码、测试、知识库条目

**Step 4: 提交**

```bash
git add tests/
git commit -m "feat: 添加端到端测试"
```

---

## 阶段 8: 文档

### Task 11: 创建使用文档

**Files:**
- Create: `README.md`
- Create: `docs/usage-guide.md`

**Step 1: 创建 README**

包含：项目介绍、快速开始、使用示例

**Step 2: 创建使用指南**

包含：详细说明、命令参考、最佳实践

**Step 3: 提交**

```bash
git add README.md docs/usage-guide.md
git commit -m "docs: 创建使用文档"
```

---

## 验收标准

| 标准 | 验证方式 |
|------|----------|
| 所有目录创建 | `tree` 命令验证 |
| Skill 文件有效 | OpenCode 加载测试 |
| 模板完整 | 人工审查 |
| 脚本可运行 | 执行 `--help` 测试 |
| E2E 测试通过 | 运行集成测试 |
| 文档完整 | 人工审查 |

---

## 预计工作量

| 阶段 | 任务数 | 预计时间 |
|------|--------|----------|
| 1. 项目骨架 | 1 | 10 分钟 |
| 2. 核心 Skill | 2 | 60 分钟 |
| 3. Agent 配置 | 2 | 30 分钟 |
| 4. 项目模板 | 2 | 90 分钟 |
| 5. 知识库 | 1 | 30 分钟 |
| 6. Self-Improving | 1 | 30 分钟 |
| 7. 集成测试 | 1 | 60 分钟 |
| 8. 文档 | 1 | 30 分钟 |
| **总计** | **11** | **340 分钟** |

---

**执行方式选择：**

1. **Subagent-Driven (当前会话)** -  dispatch 新鲜 subagent 逐任务执行，任务间 code review
2. **Parallel Session (新会话)** - 新开会话使用 executing-plans

**选择哪种方式执行本计划？**
