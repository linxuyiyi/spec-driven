# RRM 测量报告测试 Pattern

## 触发关键词

- 中文：测量、测量报告、MR、RRM、RSRP、RSRQ、SINR
- 英文：measurement、MR、RRM、RSRP、RSRQ、SINR、report

## 测试目的

验证 UE 能够根据网络配置正确上报 RRM 测量报告，包括事件触发和周期上报两种模式。

## 协议参考

- 3GPP TS 38.331: RRC 协议 - 测量配置和上报
- 3GPP TS 38.215: 物理层测量
- 3GPP TS 38.133: RRM 测试要求

## 测量事件类型

| 事件 | 用途 | 触发条件 |
|------|------|---------|
| A1 | 服务小区优于门限 | Ms - Hys > Thresh |
| A2 | 服务小区低于门限 | Ms + Hys < Thresh |
| A3 | 邻区优于服务小区 | Mn + Ofn + Ocn - Hys > Ms + Ofs + Ocs + Off + Hys |
| A4 | 邻区优于门限 | Mn + Ofn + Ocn - Hys > Thresh |
| A5 | 服务小区差且邻区好 | Ms + Hys < Thresh1 且 Mn + Ofn + Ocn - Hys > Thresh2 |
| A6 | 邻区优于 SCell | Mn + Ocn - Hys > Ms + Ocs + Off + Hys |

## 标准步骤序列 (以 A2 事件为例)

| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1 | 环境重置 | 清空残留配置，重置测试环境 | - | 环境干净 |
| 2 | 小区建立 | 建立 NR 服务小区 | cell_id=1, BW=100MHz, SCS=30kHz, PCI=1 | 小区状态 ACTIVE |
| 3 | UE 附着 | UE 附着到服务小区 | IMSI=460001234567890, PDU=IPv4 | UE 进入 CONNECTED 态 |
| 4 | A2 测量配置 | 配置 A2 事件测量 | threshold=-105dBm, hysteresis=3dB, ttt=240ms | 测量配置生效 |
| 5 | 初始状态设置 | 设置 UE 低路损 (信号好) | pathloss=80dB | RSRP > -40dBm |
| 6 | 初始 MR 验证 | 验证初始状态不上报 A2 | timeout=2s | 无 A2 MR 上报 |
| 7 | 触发条件 | 增加路损使信号变差 | pathloss=130dB | RSRP < -90dBm |
| 8 | A2 MR 验证 | 验证 UE 上报 A2 测量报告 | timeout=5s | 收到 A2 MR |
| 9 | MR 内容验证 | 验证 MR 中 RSRP 值合理性 | - | RSRP 在合理范围 (-90~-140dBm) |

## 关键参数推荐值

| 事件 | 门限推荐值 | 说明 |
|------|-----------|------|
| A1 | -85dBm | 服务小区较好 |
| A2 | -105dBm | 服务小区较差 |
| A3 | offset=3dB | 邻区优于服务小区 3dB |
| A4 | -95dBm | 邻区较好 |
| A5 | thres1=-100, thres2=-90 | 服务小区差 + 邻区好 |

## 通过标准

### 事件触发上报
1. ✅ 不满足事件条件时不上报 MR
2. ✅ 满足事件条件后 TTT + 5s 内上报 MR
3. ✅ MR 中包含正确的测量对象 (服务小区/邻区)
4. ✅ RSRP/RSRQ/SINR 值在合理范围内

### 周期上报
1. ✅ 按配置周期 (如 200ms/480ms/1020ms) 上报
2. ✅ 周期内 MR 数量符合预期 (如 5s 内上报约 25 条@200ms 周期)
3. ✅ MR 内容准确性

## 常见失败原因

| 现象 | 可能原因 | 排查方法 |
|------|---------|---------|
| 未上报 MR | 门限设置不合理 | 调整 threshold 或路损 |
| MR 内容错误 | 测量对象配置错误 | 检查 MeasObject 配置 |
| 上报不及时 | TTT 设置过长 | 减小 ttt 或检查配置 |
| 周期上报异常 | 周期配置未生效 | 检查 reportConfig |

## 变体场景

### A1 事件 - 服务小区恢复
- 先配置 A2 触发 MR
- 然后减小路损使服务小区恢复
- 验证 A1 事件上报 (服务小区优于门限)

### 周期上报测试
- 配置周期上报 interval=200ms
- 验证 5s 内收到约 25 条 MR
- 统计 MR 间隔的稳定性

### 多事件并发测试
- 同时配置 A2 + A4
- 验证两个事件都能正确上报
- 验证事件上报的优先级

### A1+A2 联合测试
| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1-3 | 环境重置、小区建立、UE 附着 | 同上 | - | - |
| 4 | A1 测量配置 | threshold=-85dBm, hys=3dB, ttt=240ms | - | 配置生效 |
| 5 | A2 测量配置 | threshold=-105dBm, hys=3dB, ttt=240ms | - | 配置生效 |
| 6 | 初始信号好 | pathloss=80dB | - | RSRP > -40dBm |
| 7 | A1 MR 验证 | 验证上报 A1 MR | timeout=5s | 收到 A1 MR |
| 8 | 信号变差 | pathloss=130dB | - | RSRP < -90dBm |
| 9 | A2 MR 验证 | 验证上报 A2 MR | timeout=5s | 收到 A2 MR |
| 10 | 信号恢复 | pathloss=80dB | - | RSRP > -40dBm |
| 11 | A1 MR 验证 | 验证再次上报 A1 MR | timeout=5s | 收到 A1 MR |
