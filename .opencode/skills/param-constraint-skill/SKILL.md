---
name: param-constraint-skill
description: OAM 参数约束与配置校验专题测试设计技能，包含单参数边界、非法枚举、多参数联动互斥与依赖校验。
license: MIT
metadata:
  domain: OAM
  version: 1.0
  trigger_keywords: ["参数约束", "配置校验", "边界值", "互斥", "非法值", "配置有效性", "MML", "数据配置"]
---

# 参数约束与配置校验技能

本技能提供基站配置参数（MO/Parameter）约束的测试设计知识，重点覆盖单参数有效性验证及多参数业务逻辑校验。详细设计知识请参考 `references/design_knowledge.md`，用例模板参考 `assets/templates.yaml`。

## 快速指引
- 测试维度：单参数有效性、单参数边界与越界、多参数互斥、多参数依赖。
- 关键测试点：极值测试（Max/Min）、类型越界校验（如负数、超长字符串）、业务互斥拒绝配置、缺失必填项。
- 适用对象：OMC 网管、LMT 本地维护终端、Netconf 客户端。
