# DRF + Vue3 Multi-Agent System

基于 **Spec-Kit** (规范驱动)、**Superpower** (测试驱动)、**UI-UX-Pro-Max** (设计智能) 的多 Agent 全栈开发系统。

## 架构

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR AGENT                       │
│  职责：系统架构师 & 项目经理 | 技能：Spec-Kit, Project-Context │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   BACKEND     │     │   FRONTEND    │     │     QA        │
│   AGENT       │     │   AGENT       │     │   AGENT       │
│ DRF + TDD     │     │ Vue3 + UI/UX  │     │ Lint + Test   │
└───────────────┘     └───────────────┘     └───────────────┘
```

## 快速开始

### 后端设置

```bash
cd backend

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或 .venv\Scripts\activate  # Windows

# 安装依赖
pip install django djangorestframework django-cors-headers django-filter pytest pytest-django

# 运行迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 运行测试
pytest -v

# 启动开发服务器
python manage.py runserver
```

### 前端设置

```bash
cd frontend

# 安装依赖
npm install

# 开发模式
npm run dev

# 类型检查
npm run type-check

# 代码检查
npm run lint

# 构建生产版本
npm run build
```

## 目录结构

```
project/
├── .opencode/                # OpenCode 配置
│   ├── instructions.md       # 项目宪法
│   └── agents/               # Agent 提示词
│       ├── orchestrator.md
│       ├── backend.md
│       ├── frontend.md
│       └── qa.md
├── .specify/                 # Spec-Kit 工作目录
│   ├── constitution.md       # 项目原则
│   ├── specs/                # 功能规格文档
│   └── memory/               # 长期记忆
├── backend/                  # DRF 后端
│   ├── app/                  # Django 应用
│   ├── tests/                # Pytest 测试
│   ├── conftest.py           # Pytest 配置
│   └── pytest.ini            # Pytest 设置
├── frontend/                 # Vue3 前端
│   ├── src/
│   │   ├── api/              # API 客户端
│   │   ├── components/       # Vue 组件
│   │   ├── stores/           # Pinia 状态
│   │   ├── styles/           # 全局样式
│   │   ├── types/            # TypeScript 类型
│   │   └── views/            # 页面视图
│   └── tests/                # 前端测试
├── AGENTS.md                 # 多 Agent 配置
└── README.md                 # 本文件
```

## 核心原则

### 1. Spec-First (规范优先)
- 所有功能必须在 `.specify/specs/` 中有对应的规格文档
- 规格定义：API 合同、UI 要求、测试用例
- 无规格不编码

### 2. TDD Mandate (测试驱动)
- 后端：测试必须先于实现编写
- 遵循 Red -> Green -> Refactor 循环
- 测试覆盖率 >80%

### 3. Design Excellence (设计卓越)
- 使用 UI-UX-Pro-Max 原则
- 专业配色、间距、排版
- 无障碍访问 (WCAG AA)
- 响应式设计

### 4. Type Safety (类型安全)
- 后端：Pydantic + DRF 序列化器
- 前端：TypeScript 严格模式

## 质量门禁

| 检查项 | 命令 | 要求 |
|--------|------|------|
| 后端测试 | `pytest backend/ -v` | 全部通过 |
| 覆盖率 | `pytest --cov=app` | >80% |
| 前端 Lint | `npm run lint` | 0 错误 |
| 类型检查 | `npm run type-check` | 0 错误 |
| API 合同 | 规格对比 | 完全匹配 |

## 工作流示例

### 开发新功能

1. **用户请求**: "添加用户个人资料编辑功能"

2. **Orchestrator**:
   - 检查 `.specify/specs/` 是否存在相关规格
   - 如无，创建规格文档
   - 分解任务并分配给 Backend/Frontend Agent

3. **Backend Agent**:
   - 阅读规格
   - 编写失败的 pytest 测试
   - 实现代码使测试通过
   - 提交测试通过的报告

4. **Frontend Agent**:
   - 阅读规格
   - 创建 TypeScript 类型
   - 创建 Vue 组件 + Pinia Store
   - 应用 UI-UX-Pro-Max 设计原则

5. **QA Agent**:
   - 运行所有测试
   - 运行 Lint/Type Check
   - 验证 API 合同
   - 生成 QA 报告

## Agent 说明

### Orchestrator Agent
- **角色**: 系统架构师
- **职责**: 任务分解、规格管理、质量验证
- **永不**: 编写实现代码

### Backend Agent
- **角色**: DRF 专家
- **技能**: Superpower (TDD)
- **规则**: 测试先行

### Frontend Agent
- **角色**: Vue3 + UI/UX 专家
- **技能**: UI-UX-Pro-Max
- **规则**: 专业设计，无丑陋默认样式

### QA Agent
- **角色**: 质量检查员
- **技能**: Verification-Before-Completion
- **职责**: 所有质量门禁通过前阻止合并

## 许可证

MIT
