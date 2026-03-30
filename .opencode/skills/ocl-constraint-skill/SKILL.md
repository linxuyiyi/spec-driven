---
name: ocl-constraint-skill
description: 参数约束（OCL）测试设计技能，验证参数间逻辑约束、依赖关系与非法组合
license: MIT
metadata:
  domain: 配置约束
  version: 1.0
  trigger_keywords: ["约束", "OCL", "implies", "约束关系", "依赖", "互斥", "规则校验"]
---

# OCL 参数约束测试技能

本技能用于验证"参数之间的逻辑约束"，典型来源：
- OCL 表达式
- 配置规则
- 网管约束校验逻辑

---

## 测试目标

验证：
1. 满足约束时 → 配置成功
2. 违反约束时 → 配置失败
3. 边界情况下 → 行为正确

---

## 支持的约束类型

- implies（条件约束）
- and / or（组合约束）
- not（取反）
- 数值比较（>, <, ≤, ≥）
- 枚举依赖
- 互斥约束

---

## 核心原则

每条约束必须生成：

- ✅ 至少 1 个满足约束的用例（正例）
- ❌ 至少 1 个违反约束的用例（反例）

---

## 示例

```ocl
context Cell
inv:
  bandwidth = 100 implies prb <= 273
```

生成：
- 正例：bandwidth=100, prb=200
- 反例：bandwidth=100, prb=300
