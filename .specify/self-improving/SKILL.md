# Self-Improving Agent 多 Agent 系统


## Overview

这是一个**通用自我改进系统**，可以从所有 Agent 的经验中学习，实现持续进化。

## 核心架构

### Multi-Memory System

```
┌─────────────────────────────────────────────────────────────┐
│              MULTI-MEMORY ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Semantic Memory     Episodic Memory      Working Memory    │
│  (模式/规则)         (经验记录)           (当前会话)        │
│  memory/semantic/    memory/episodic/     memory/working/   │
│                                                             │
│  - 可重用模式         - 具体事件            - 会话上下文     │
│  - 抽象规则           - 成功/失败案例       - 错误上下文     │
│  - 最佳实践           - 用户反馈            - 临时数据       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Self-Improvement Loop

```
┌──────────────────────────────────────────────────────────────┐
│                  SELF-IMPROVEMENT LOOP                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Agent Event → Extract Experience → Abstract Pattern       │
│        │              │                   │                  │
│        ▼              ▼                   ▼                  │
│   ┌────────────────────────────────────────────────┐         │
│   │           MULTI-MEMORY SYSTEM                   │         │
│   └────────────────────────────────────────────────┘         │
│        │                   │                   │              │
│        ▼                   ▼                   ▼              │
│   Update Skills    Update Confidence   Self-Correction        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 触发机制

### 自动触发 (Hooks)

| 事件 | 触发条件 | 动作 |
|------|---------|------|
| `before_start` | 任何 Agent 开始任务 | 记录会话开始 |
| `after_complete` | Agent 完成任务 | 提取模式，更新技能 |
| `on_error` | 命令返回非零退出码 | 捕获错误，自我修正 |

### 手动触发

用户可以说：
- "自我进化"、"self-improve"、"从经验中学习"
- "分析今天的经验"、"总结教训"
- "改进某个 Agent 的能力"

## 进化优先级矩阵

| 触发进化 | 目标 Agent | 优先级 | 动作 |
|---------|-----------|--------|------|
| 新 PRD 模式发现 | prd-planner | 高 | 添加到质量清单 |
| 架构权衡澄清 | architecting-solutions | 高 | 添加到决策模式 |
| API 设计规则学习 | api-designer | 高 | 更新模板 |
| Debug 技巧发现 | debugger | 高 | 添加到反模式 |
| Review 清单补充 | code-reviewer | 高 | 添加检查项 |
| 性能/安全洞察 | performance-engineer | 高 | 更新模式 |
| UI/UX 规范问题 | prd-planner | 高 | 添加视觉规范 |
| React 状态模式 | debugger | 中 | 更新模式 |
| 测试策略改进 | test-automator | 中 | 更新方法 |

## Memory 结构

### 1. Semantic Memory (`memory/semantic-patterns.json`)

存储**抽象模式和规则**，可在不同上下文中重用：

```json
{
  "patterns": {
    "pat-2026-03-22-001": {
      "id": "pat-2026-03-22-001",
      "name": "TDD Implementation Pattern",
      "source": "implementation_review",
      "confidence": 0.95,
      "applications": 5,
      "created": "2026-03-22",
      "category": "backend_tdd",
      "pattern": "Tests must be written before implementation code",
      "problem": "Developers often write implementation first, leading to poor test coverage",
      "solution": {
        "steps": [
          "Write failing test first",
          "Implement minimal code to pass",
          "Refactor while keeping tests green"
        ],
        "quality_rules": [
          "Test coverage must be >80%",
          "All edge cases must be covered"
        ]
      },
      "target_skills": ["backend", "qa"]
    }
  }
}
```

### 2. Episodic Memory (`memory/episodic/`)

存储**具体经验和发生的事件**：

```
memory/episodic/
├── 2026/
│   ├── 2026-03-22-backend-tdd.json
│   ├── 2026-03-22-frontend-ui.json
│   └── 2026-03-23-qa-verification.json
```

```json
{
  "id": "ep-2026-03-22-001",
  "timestamp": "2026-03-22T10:30:00Z",
  "agent": "backend",
  "task": "Implement DefenseConfig model",
  "outcome": "success",
  "situation": "User requested defense configuration management feature",
  "approach": "Followed TDD: wrote 21 tests first, then implemented models",
  "result": "All tests passed, 85% coverage achieved",
  "lesson": "TDD approach ensures high code quality from the start",
  "related_pattern": "tdd_implementation_pattern",
  "user_feedback": {
    "rating": 9,
    "comments": "Excellent test coverage and clean code"
  }
}
```

### 3. Working Memory (`memory/working/`)

存储**当前会话上下文**：

```
memory/working/
├── current_session.json   # 当前会话数据
├── last_error.json        # 错误上下文（用于自我修正）
└── session_end.json       # 会话结束标记
```

## 自我改进流程

### Phase 1: 经验提取

任何 Agent 完成任务后，提取：

```yaml
What happened:
  agent_used: {which agent}
  task: {what was being done}
  outcome: {success|partial|failure}

Key Insights:
  what_went_well: [what worked]
  what_went_wrong: [what didn't work]
  root_cause: {underlying issue if applicable}

User Feedback:
  rating: {1-10 if provided}
  comments: {specific feedback}
```

### Phase 2: 模式抽象

将经验转换为可重用模式：

| 具体经验 | 抽象模式 | 目标 Agent |
|---------|---------|-----------|
| "用户忘记保存 PRD 笔记" | "始终将思考持久化到文件" | orchestrator |
| "代码审查漏掉 SQL 注入" | "添加安全检查项" | backend |
| "Callback 为空导致失败" | "验证 callback 实现" | backend, frontend |
| "UI 规范位置描述模糊" | "UI 规范需要精确相对位置" | frontend |

**抽象规则**:
```yaml
If experience_repeats 3+ times:
  pattern_level: critical
  action: Add to Agent's "Critical Mistakes" section

If solution_was_effective:
  pattern_level: best_practice
  action: Add to Agent's "Best Practices" section

If user_rating >= 7:
  pattern_level: strength
  action: Reinforce this approach

If user_rating <= 4:
  pattern_level: weakness
  action: Add to "What to Avoid" section
```

### Phase 3: Agent 更新

使用**进化标记**更新 Agent 文件：

```markdown
<!-- Evolution: 2026-03-22 | source: ep-2026-03-22-001 | agent: backend -->

## Pattern Added (2026-03-22)

**Pattern**: Always verify callbacks are not empty functions

**Source**: Episode ep-2026-03-22-001

**Confidence**: 0.95

### Updated Checklist
- [ ] Verify all callbacks have implementations
- [ ] Test callback execution paths
```

**修正标记** (修复错误指导时):

```markdown
<!-- Correction: 2026-03-22 | was: "Use callback chain" | reason: caused stale refresh -->

## Corrected Guidance

Use direct state monitoring instead of callback chains:
```typescript
// ✅ Do: Direct state monitoring
const prevPendingCount = usePrevious(pendingCount);
```
```

### Phase 4: Memory Consolidation

1. **更新 semantic memory** (`memory/semantic-patterns.json`)
2. **存储 episodic memory** (`memory/episodic/YYYY-MM-DD-{agent}.json`)
3. **更新模式置信度** 基于应用次数/反馈
4. **剪枝过时模式** (低置信度、近期未应用)

## 自我修正 (on_error hook)

触发条件：
- Bash 命令返回非零退出码
- 测试在遵循 Agent 指导后失败
- 用户报告指导产生错误结果

**流程**:

```markdown
## Self-Correction Workflow

1. Detect Error
   - Capture error context from working/last_error.json
   - Identify which Agent guidance was followed

2. Verify Root Cause
   - Was the Agent guidance incorrect?
   - Was the guidance misinterpreted?
   - Was the guidance incomplete?

3. Apply Correction
   - Update Agent file with corrected guidance
   - Add correction marker with reason
   - Update related patterns in semantic memory

4. Validate Fix
   - Test the corrected guidance
   - Ask user to verify
```

## 钩子集成

### Claude Code Settings 配置

在 `~/.claude/settings.json` 中添加：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILLS_DIR}/self-improving-agent/hooks/pre-tool.sh \"$TOOL_NAME\" \"$TOOL_INPUT\""
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILLS_DIR}/self-improving-agent/hooks/post-bash.sh \"$TOOL_OUTPUT\" \"$EXIT_CODE\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILLS_DIR}/self-improving-agent/hooks/session-end.sh"
          }
        ]
      }
    ]
  }
}
```

## 最佳实践

### DO (应该做的)

- ✅ 从 EVERY Agent 交互中学习
- ✅ 在适当的抽象级别提取模式
- ✅ 更新多个相关 Agent
- ✅ 跟踪置信度和应用次数
- ✅ 请求用户对改进的反馈
- ✅ 使用进化/修正标记进行可追溯性
- ✅ 在广泛应用前验证指导

### DON'T (不应该做的)

- ❌ 从单一经验过度概括
- ❌ 在没有置信度跟踪的情况下更新 Agent
- ❌ 忽略负面反馈
- ❌ 做出破坏现有功能的更改
- ❌ 创建矛盾的模式
- ❌ 在不理解上下文的情况下更新 Agent

## 快速开始

在任何 Agent 完成任务后，此系统自动：

1. **分析** 发生了什么
2. **提取** 模式和见解
3. **更新** 相关 Agent 文件
4. **记录** 到 memory 供将来参考
5. **报告** 摘要给用户

## References

- [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/html/2601.02553v1)
- [A Survey on the Memory Mechanism of Large Language Model Agents](https://dl.acm.org/doi/10.1145/3748302)
- [Lifelong Learning of LLM based Agents](https://arxiv.org/html/2501.07278v1)
- [Evo-Memory: DeepMind's Benchmark](https://shothota.medium.com/evo-memory-deepminds-new-benchmark)
