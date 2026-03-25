# Skill: drf-vue3-developer

## 全栈开发专家 Agent

专精于 Django REST Framework + Vue3 + MySQL 的全栈开发。

---

## 工作流

```
1. 需求接收 → 2. Spec 解析 → 3. 架构设计 → 4. TDD 开发 → 5. 测试验证 → 6. 经验沉淀
```

---

## 触发方式

### 命令行式
```
/drf-dev create feature <spec-file>
/drf-dev test e2e
/drf-dev knowledge search <query>
```

### 对话式
用户用自然语言描述需求，Agent 自动识别意图并执行。

### 项目式
检测项目根目录的 `.drf-dev-config.yaml` 文件，自动激活。

---

## 子 Skill 调用

| 阶段 | 子 Skill | 用途 |
|------|----------|------|
| Spec 解析 | spec-analyzer | 解析模板化 Spec 文档 |
| 架构设计 | writing-plans | 创建架构设计方案 |
| 前端设计 | ui-ux-pro-max | Vue3 组件设计 |
| TDD 开发 | test-driven-development | 测试驱动实现 |
| 测试验证 | playwright-e2e-testing | E2E 自动化测试 |
| 经验沉淀 | self-improving | 记录决策和错误 |

---

## 上下文管理

### 项目状态
- 当前 Spec 文件路径
- 已完成的阶段
- 生成的文件列表
- 测试状态

### 知识检索
在执行新任务前，检索 `knowledge/` 目录：
```bash
grep -r "<tech>" knowledge/best-practices/
grep -r "<error-type>" knowledge/errors/
```

---

## 输出规范

### 架构设计输出
```markdown
## 架构方案

### 数据模型
- Model A: fields...
- Model B: fields...

### API 端点
- GET/POST/PUT/DELETE /api/resource/

### 前端组件
- ComponentA.vue
- ComponentB.vue
```

### TDD 输出
```
1. 生成测试文件
2. 运行测试 (预期失败)
3. 生成实现代码
4. 运行测试 (预期通过)
5. 重构
```

### 经验记录输出
```markdown
## 决策记录
- 问题：
- 方案：
- 决策：
- 理由：
```

---

## 错误处理

| 错误 | 处理方式 |
|------|----------|
| Spec 解析失败 | 请求用户澄清 |
| 测试失败 | 记录到 knowledge/errors/ |
| 代码生成错误 | 回滚并重试 |

---

## 验收标准

- 所有测试通过
- E2E 测试覆盖主要用户流程
- 经验知识库更新
- 代码符合规范

---

## 使用示例

```bash
# 创建新功能
/drf-dev create feature specs/user-auth.md

# 运行测试
/drf-dev test unit
/drf-dev test e2e

# 检索知识
/drf-dev knowledge search "authentication"
```
