# 项目宪法：DRF + Vue3 多 Agent 开发系统

**单一事实来源**: 本文件是所有 Agent 的权威参考。

## 核心原则

1. **Spec-First (规范优先)**: 任何代码编写前必须在 `.specify/specs/` 中有对应的规格文档。如果规格缺失，Orchestrator 必须先创建规格。

2. **TDD Mandate (测试驱动)**: 所有后端逻辑必须先写测试 (`pytest`)，后写实现。遵循 Red -> Green -> Refactor 循环。

3. **Design Excellence (设计卓越)**: 所有前端组件必须遵循专业 UI/UX 标准 (颜色、间距、排版、无障碍)。禁止使用内联样式或丑陋默认值；使用 Tailwind/SCSS 配合设计令牌。

4. **Type Safety (类型安全)**: 后端 (Pydantic/DRF Serializers) 和前端 (TypeScript) 必须严格类型化。

5. **单一事实来源**: `.specify/` 目录是 API 合同、UI 需求和测试用例的权威参考。

## 工作流

| 角色 | 职责 |
|------|------|
| **Orchestrator** | 分解任务、管理 `.specify/` 更新、分配子 Agent |
| **Backend Agent** | 负责模型、序列化器、视图集、测试 (TDD 优先) |
| **Frontend Agent** | 负责组件、Pinia Store、API 集成、UI 优化 |
| **QA Agent** | 验证测试通过且代码检查无误后才会并 |

## 技术栈

### 后端
- Python 3.11+
- Django 5.x
- Django Rest Framework (DRF)
- Pytest + Pytest-Django
- Celery (异步任务)
- Pydantic (验证)

### 前端
- Vue 3.4+
- TypeScript
- Vite
- Pinia (状态管理)
- TailwindCSS
- Vue Router

## 代码质量门禁

- **后端**: `pytest --cov=app --cov-report=term-missing`
- **前端**: `npm run lint && npm run type-check`
- **API 合同**: 对照 `.specify/specs/*.md` 验证

## 文件命名规范

- 后端测试：`tests/test_<模块>.py`
- Vue 组件：`<组件名>.vue`
- Pinia Store：`src/stores/<store>.ts`
- 规格文档：`.specify/specs/<功能名>.md`

## 错误处理与恢复

### QA 失败处理
1. QA 报告失败 → 通知责任 Agent
2. 责任 Agent 修复 → 重新运行测试
3. 连续 3 次失败 → 升级至 Orchestrator
4. Orchestrator 介入 → 重新分解任务或调整 Spec

### Spec 评审不通过
1. User/Agent 提出修改意见
2. Orchestrator 更新 Spec
3. 版本号 +1 (v1.0.0 → v1.1.0)
4. 通知所有相关 Agent

### Agent 多次失败
1. 记录失败原因到 `.specify/memory/blockers.md`
2. 分析是否为同类问题
3. 如是同类问题 → 更新 Agent prompt
4. 如是新问题 → 调用 Self-Improving 提取经验
