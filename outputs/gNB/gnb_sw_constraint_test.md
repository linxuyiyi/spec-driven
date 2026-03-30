# gNB p1 参数 sw1/sw2 约束测试用例

## 约束规则分析表

| 三要素 | 内容 |
|--------|------|
| Trigger | p1.sw1 = ON |
| Target | p1.sw2 |
| Check Point | 配置修改/提交时检查 |

**约束规则**：当 sw1 为开时，sw2 必须为开

---

## 测试用例

| 用例编号 | 用例名称 | 级别 | 前置条件 | 测试步骤 | 预期结果 | 后置条件 |
|----------|----------|------|----------|----------|----------|----------|
| gNB-FUNC-001 | 【sw1/sw2 约束】sw1 开且 sw2 开配置成功 | P0 | sw1=OFF, sw2=OFF | 1. 配置 p1.sw1=ON<br>2. 配置 p1.sw2=ON<br>3. 提交配置 | 配置成功，查询返回 sw1=ON, sw2=ON | 恢复初始状态 |
| gNB-NEG-001 | 【sw1/sw2 约束】sw1 开但 sw2 关被拒绝 | P0 | sw1=OFF, sw2=OFF | 1. 配置 p1.sw1=ON<br>2. 配置 p1.sw2=OFF<br>3. 提交配置 | 配置失败，提示"sw1 为开时 sw2 必须为开" | 无 |
| gNB-FUNC-002 | 【sw1/sw2 约束】先开 sw2 再开 sw1 成功 | P1 | sw1=OFF, sw2=OFF | 1. 配置 p1.sw2=ON<br>2. 提交<br>3. 配置 p1.sw1=ON<br>4. 提交 | 配置成功，查询返回 sw1=ON, sw2=ON | 恢复初始状态 |
| gNB-FUNC-003 | 【sw1/sw2 约束】sw1 关时 sw2 可关 | P1 | sw1=ON, sw2=ON | 1. 配置 p1.sw1=OFF<br>2. 配置 p1.sw2=OFF<br>3. 提交配置 | 配置成功，查询返回 sw1=OFF, sw2=OFF | 恢复初始状态 |
| gNB-FUNC-004 | 【sw1/sw2 约束】sw1 关时 sw2 可开 | P2 | sw1=OFF, sw2=OFF | 1. 配置 p1.sw1=OFF<br>2. 配置 p1.sw2=ON<br>3. 提交配置 | 配置成功，查询返回 sw1=OFF, sw2=ON | 恢复初始状态 |
| gNB-NEG-002 | 【sw1/sw2 约束】sw1 开状态下修改 sw2 为关被拒绝 | P1 | sw1=ON, sw2=ON | 1. 配置 p1.sw2=OFF<br>2. 提交配置 | 配置失败，提示"sw1 为开时 sw2 必须为开" | 保持 sw2=ON |
| gNB-NEG-003 | 【sw1/sw2 约束】同时下发 sw1=ON 和 sw2=OFF 被拒绝 | P0 | sw1=OFF, sw2=OFF | 1. 同时下发配置 p1.sw1=ON, p1.sw2=OFF<br>2. 提交配置 | 配置失败，提示"sw1 为开时 sw2 必须为开" | 无 |

---

## 评审检查清单

- [x] 约束规则三要素已识别完整
- [x] 分支覆盖完整（正例/反例/修正/无关）
- [x] 测试了顺序下发和同时下发两种场景
- [x] 预期结果明确可验证
- [x] 用例编号唯一
