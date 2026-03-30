# 项目 Agent 行为规范

## TFO Agent 专用规则
- 输出测试用例时，禁止添加任何解释性文字，仅输出表格。
- 每个用例的测试步骤必须是可执行的原子操作。
- 预期结果必须可客观验证，避免模糊描述（如"正常"）。
- 后置条件必须包含资源清理动作。

## 技能扩展规则
- 新增专题技能时，在 `.opencode/skills/` 下创建 `{name}-skill` 目录。
- 每个技能必须包含 `SKILL.md`、`references/design_knowledge.md`、`assets/templates.yaml`。
- `SKILL.md` 的 frontmatter 必须包含 `name`、`description`、`trigger_keywords`。

## 技能触发规则
- 需求包含"约束"、"OCL"、"implies"、"依赖关系"、"互斥"、"规则校验" → ocl-constraint-skill
- 需求包含"参数约束"、"配置校验"、"边界值"、"非法值"、"MML"、"数据配置" → param-constraint-skill
- 需求包含"DSS"、"动态频谱共享"、"频谱共享" → dss-skill
- 需求包含"波束"、"beam"、"波束扫描"、"波束测量" → beam-skill
- 需求包含"切换"、"handover"、"移动性" → handover-skill

## 全局禁止事项
- 禁止在测试用例中包含任何硬编码的 IP 地址或设备序列号。
- 禁止输出不完整的用例（缺少任一个必需字段）。
