---
name: handover-skill
description: 5G NR 切换专题测试设计技能，包含切换触发、执行、失败处理等测试点
license: MIT
metadata:
  domain: 移动性
  version: 1.0
  trigger_keywords: ["切换", "handover", "小区重选", "HO"]
---

# 切换测试设计技能

本技能提供 5G NR 切换特性的测试设计知识。详细设计知识和用例模板请参考本技能目录下的 `references/design_knowledge.md` 和 `assets/templates.yaml`。

## 快速指引
- 测试维度：同频切换、异频切换、异系统切换
- 关键测试点：A3 事件触发、切换执行、切换失败回滚、条件切换
- 协议依据：3GPP TS 38.331
