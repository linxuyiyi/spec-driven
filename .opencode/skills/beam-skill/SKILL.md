---
name: beam-skill
description: 5G NR 波束管理专题测试设计技能，包含波束扫描、测量、切换、失败恢复等测试点
license: MIT
metadata:
  domain: 空口
  version: 1.0
  trigger_keywords: ["波束", "beam", "波束管理", "波束赋形", "SSB"]
---

# 波束管理测试设计技能

本技能提供 5G NR 波束管理特性的测试设计知识。详细设计知识和用例模板请参考本技能目录下的 `references/design_knowledge.md` 和 `assets/templates.yaml`。

## 快速指引
- 测试维度：波束扫描、波束测量、波束切换、波束失败恢复
- 关键测试点：初始波束对准、波束测量上报、波束切换、波束失败恢复
- 边界值：SSB 波束数量 4/8/16/32/64，测量周期 5ms~160ms
- 协议依据：3GPP TS 38.213, TS 38.215
