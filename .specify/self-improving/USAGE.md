# Self-Improving Agent 使用指南

## 快速开始

### 1. 自动触发

自我进化机制会在以下情况自动触发：

- **任务完成后**: 自动提取经验并更新模式
- **发生错误时**: 自动记录错误并自我修正
- **会话结束时**: 自动分析并生成报告

### 2. 手动触发

用户可以通过以下方式手动触发自我进化：

```
自我进化
self-improve
从经验中学习
分析今天的经验
总结教训
```

### 3. 查看记忆

**Semantic Memory** (抽象模式):
```bash
cat .specify/self-improving/memory/semantic-patterns.json
```

**Episodic Memory** (具体经验):
```bash
ls -la .specify/self-improving/memory/episodic/$(date +%Y)/
cat .specify/self-improving/memory/episodic/$(date +%Y)/ep-*.json
```

**Working Memory** (当前会话):
```bash
cat .specify/self-improving/memory/working/current_session.json
```

## 脚本使用

### extract-experience.sh

提取经验并存储到记忆中：

```bash
.specify/self-improving/scripts/extract-experience.sh \
  "backend" \
  "Implement DefenseConfig model" \
  "success" \
  "9" \
  "Excellent test coverage"
```

参数：
1. `agent`: 使用的 Agent (backend/frontend/qa/orchestrator)
2. `task`: 任务描述
3. `outcome`: 结果 (success/partial/failure)
4. `rating`: 用户评分 (1-10，可选)
5. `comments`: 用户反馈 (可选)

### session-complete.sh

会话完成时分析和报告：

```bash
.specify/self-improving/scripts/session-complete.sh
```

## 记忆结构

### Semantic Memory (`semantic-patterns.json`)

存储可重用的抽象模式和规则：

```json
{
  "patterns": {
    "pat-2026-03-22-001": {
      "id": "pat-2026-03-22-001",
      "name": "TDD Implementation Pattern",
      "confidence": 0.95,
      "applications": 5,
      "pattern": "Tests must be written before implementation",
      "solution": { ... },
      "target_agents": ["backend", "qa"]
    }
  }
}
```

### Episodic Memory (`episodic/YYYY-MM-DD-agent.json`)

存储具体的经验事件：

```json
{
  "id": "ep-2026-03-22-001",
  "timestamp": "2026-03-22T10:30:00Z",
  "agent": "backend",
  "task": "Implement DefenseConfig model",
  "outcome": "success",
  "lesson": "TDD approach ensures high code quality",
  "user_feedback": {
    "rating": 9,
    "comments": "Excellent test coverage"
  }
}
```

### Working Memory (`working/`)

当前会话上下文：

- `current_session.json`: 活跃会话数据
- `last_error.json`: 错误上下文（用于自我修正）
- `session_end.json`: 会话结束标记

## 进化流程

### 1. 经验提取

```
Agent 完成任务 → 记录到 Episodic Memory
```

### 2. 模式抽象

```
经验重复 3+ 次 → 提升为 Critical Pattern
解决方案有效 → 添加为 Best Practice
用户评分 >= 7 → 强化此方法
用户评分 <= 4 → 添加到 "What to Avoid"
```

### 3. 更新 Agent

使用进化标记更新 Agent 文件：

```markdown
<!-- Evolution: 2026-03-22 | source: ep-2026-03-22-001 | agent: backend -->

## Pattern Added (2026-03-22)

**Pattern**: Always verify callbacks are not empty functions
**Source**: Episode ep-2026-03-22-001
**Confidence**: 0.95
```

### 4. 记忆整合

- 更新 semantic memory
- 存储 episodic memory
- 更新模式置信度
- 剪枝过时模式

## 自我修正流程

当发生错误时：

1. **检测错误**: 捕获错误上下文
2. **验证根因**: 分析是否 Agent 指导有误
3. **应用修正**: 更新 Agent 文件并添加修正标记
4. **验证修复**: 测试修正后的指导

## 最佳实践

### ✅ DO

- 从每个 Agent 交互中学习
- 在适当的抽象级别提取模式
- 更新多个相关 Agent
- 跟踪置信度和应用次数
- 请求用户反馈
- 使用进化/修正标记

### ❌ DON'T

- 从单一经验过度概括
- 在没有置信度跟踪的情况下更新
- 忽略负面反馈
- 破坏现有功能
- 创建矛盾的模式

## 示例工作流

```bash
# 1. Agent 完成任务
# (Backend Agent implements DefenseConfig model with TDD)

# 2. 提取经验
.specify/self-improving/scripts/extract-experience.sh \
  "backend" \
  "Implement DefenseConfig model with TDD" \
  "success" \
  "9" \
  "All 21 tests passed, 85% coverage"

# 3. 会话完成分析
.specify/self-improving/scripts/session-complete.sh

# 4. 查看更新
cat .specify/self-improving/memory/semantic-patterns.json
cat .specify/self-improving/memory/episodic/2026/ep-2026-03-22-*.json
```

## 参考资料

- [SimpleMem: Efficient Lifelong Memory](https://arxiv.org/html/2601.02553v1)
- [Memory Mechanism Survey](https://dl.acm.org/doi/10.1145/3748302)
- [Lifelong Learning of LLM Agents](https://arxiv.org/html/2501.07278v1)
