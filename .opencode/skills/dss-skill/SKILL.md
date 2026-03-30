---
name: dss-skill
description: 动态频谱共享（DSS）专题测试设计技能，包含测试点、边界值、异常场景库
license: MIT
metadata:
  domain: 空口
  version: 1.0
  trigger_keywords: ["DSS", "动态频谱共享", "频谱共享", "LTE-NR 共存"]
---

# DSS 测试设计技能

本技能提供动态频谱共享（DSS）特性的测试设计知识。详细设计知识和用例模板请参考本技能目录下的 `references/design_knowledge.md` 和 `assets/templates.yaml`。

## 快速指引
- 测试维度：功能、性能、异常
- 关键测试点：基础接入、资源抢占、动态调整、测量报告、配置错误
- 边界值：抢占阈值 50%/70%/90%，PRB 范围 1~100
- 协议依据：3GPP TS 38.331, TS 38.214
