# DRF-Vue3 全栈开发 Agent

一个在 OpenCode 中运行的全栈开发 Agent，专精于 Django REST Framework + Vue3 + MySQL 技术栈。

## 特性

- ✅ **规范化** - 基于 Spec 模板的需求分析和架构设计
- ✅ **自动化** - TDD 模式下全自动代码生成
- ✅ **可进化** - Self-Improving 机制持续沉淀经验
- ✅ **可测试** - Playwright E2E 测试验证

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Django 4.x, DRF, MySQL 8.x |
| 前端 | Vue3, Vite, TypeScript, Pinia, Element Plus |
| 测试 | pytest, Playwright |
| Agent | OpenCode Skills |

## 快速开始

### 1. 创建 Spec 文档

```bash
cp templates/specs/feature-spec-template.md specs/my-feature.md
# 编辑 specs/my-feature.md 填写需求
```

### 2. 使用 Agent

在 OpenCode 中：

```bash
# 命令行式
/drf-dev create feature specs/my-feature.md

# 对话式
"帮我创建一个用户认证功能"

# 检索知识
/drf-dev knowledge search "authentication"
```

### 3. 查看生成的代码

```bash
# 后端代码在 backend/ 目录
# 前端代码在 frontend/ 目录
```

## 目录结构

```
myagent/
├── skills/                    # OpenCode Skills
│   ├── drf-vue3-developer/   # 核心开发 Skill
│   └── spec-analyzer/        # 需求分析 Skill
├── agent-config/              # Agent 配置
│   ├── system-prompt.md      # 系统提示词
│   └── tools-config.yaml     # 工具配置
├── templates/                 # 项目模板
│   ├── backend/              # DRF 模板
│   ├── frontend/             # Vue3 模板
│   └── specs/                # Spec 模板
├── knowledge/                 # 经验知识库
│   ├── decisions/            # 决策记录
│   ├── errors/               # 错误模式
│   └── best-practices/       # 最佳实践
├── scripts/                   # 工具脚本
│   ├── record-decision.py
│   ├── record-error.py
│   └── search-knowledge.py
└── tests/                     # 测试
    └── e2e/
```

## 命令参考

### 开发命令

| 命令 | 说明 |
|------|------|
| `/drf-dev create feature <spec>` | 根据 Spec 创建功能 |
| `/drf-dev parse <spec>` | 解析 Spec 文档 |
| `/drf-dev design ui` | 前端 UI 设计 |
| `/drf-dev tdd <feature>` | TDD 开发 |

### 测试命令

| 命令 | 说明 |
|------|------|
| `/drf-dev test unit` | 运行单元测试 |
| `/drf-dev test e2e` | 运行 E2E 测试 |

### 知识管理

| 命令 | 说明 |
|------|------|
| `/drf-dev knowledge search <query>` | 检索知识库 |
| `python3 scripts/record-decision.py` | 记录决策 |
| `python3 scripts/record-error.py` | 记录错误 |
| `python3 scripts/search-knowledge.py` | 搜索知识 |

## 工作流

```
1. 需求接收 → 2. Spec 解析 → 3. 架构设计 → 4. TDD 开发 → 5. 测试验证 → 6. 经验沉淀
```

### TDD 循环

```
生成测试 → 运行 (失败) → 生成实现 → 运行 (通过) → 重构
```

## 经验知识库

### 决策记录 (ADRs)

记录架构决策的背景、方案对比、最终决策和理由。

```bash
python3 scripts/record-decision.py "JWT 认证方案" \
  --background "需要实现用户认证" \
  --decision "使用 SimpleJWT" \
  --reason "无状态、跨域友好"
```

### 错误模式

记录错误现象、根因分析、解决方案和预防措施。

```bash
python3 scripts/record-error.py "Model 验证错误" \
  --error "ValidationError: field cannot be blank" \
  --scenario "创建实例时传入空字符串" \
  --cause "blank=False 默认值" \
  --solution "设置 blank=True 或清理输入"
```

### 最佳实践

记录代码规范、设计模式和推荐做法。

## 测试

运行端到端测试：

```bash
python3 tests/e2e/test-agent-flow.py
```

## 贡献

1. Fork 项目
2. 创建特性分支
3. 提交变更
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License
