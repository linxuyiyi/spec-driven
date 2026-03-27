# A3 事件切换测试 Pattern

## 触发关键词

- 中文：切换、A3、同频切换、intra-frequency
- 英文：handover、HO、A3、intra-freq

## 测试目的

验证当邻区信号质量优于服务小区一定偏移量时，UE 能够正确上报 A3 测量报告并完成切换流程。

## 协议参考

- 3GPP TS 38.331: RRC 协议 - 测量事件 A3 定义
- 3GPP TS 38.133: RRM 测试要求

## A3 事件触发条件

```
Mn + Ofn + Ocn - Hys > Ms + Ofs + Ocs + Off + Hys

其中:
- Mn: 邻区测量结果
- Ms: 服务小区测量结果
- Ofn/Ofs: 频率偏移
- Ocn/Ocs: 小区偏移
- Hys: 迟滞 (hysteresis)
- Off: 偏移量 (a3-Offset)
```

## 标准步骤序列

| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1 | 环境重置 | 清空残留配置，重置测试环境 | - | 环境干净 |
| 2 | 服务小区建立 | 建立 NR 服务小区 | cell_id=1, BW=100MHz, SCS=30kHz, PCI=1, power=46dBm | 小区状态 ACTIVE |
| 3 | 邻区配置 | 添加同频邻区关系 | neighbor_cell_id=2, PCI=2, freq=同频 | 邻区添加成功 |
| 4 | UE 附着 | UE 附着到服务小区 | IMSI=460001234567890, PDU=IPv4 | UE 进入 CONNECTED 态 |
| 5 | A3 测量配置 | 配置 A3 事件测量 | threshold=-95dBm, hysteresis=3dB, ttt=240ms, offset=3dB | 测量配置生效 |
| 6 | 初始位置验证 | 确认 UE 在服务小区中心 | 位置= (0, 0) | RSRP > -80dBm |
| 7 | 初始 MR 验证 | 验证初始状态不上报 A3 | timeout=2s | 无 A3 MR 上报 |
| 8 | 触发切换 | 移动 UE 到小区边缘 | 位置= (500m, 0) | UE 进入切换触发区 |
| 9 | A3 MR 验证 | 验证 UE 上报 A3 测量报告 | timeout=5s | 收到 A3 MR，邻区 RSRP 优于服务小区 3dB+ |
| 10 | 切换命令验证 | 验证基站下发切换命令 | timeout=5s | 收到 RRC Reconfiguration 消息 |
| 11 | 切换完成验证 | 验证 UE 接入目标小区 | timeout=5s | 收到 RRC Reconfiguration Complete |
| 12 | 数据通路验证 | 验证切换后数据通路正常 | timeout=5s | PING 时延<10ms |

## 关键参数推荐值

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| a3-Offset | 3dB | 邻区需优于服务小区 3dB |
| hysteresis | 3dB | 防止乒乓切换 |
| ttt | 240ms | 触发时间，平衡灵敏度和稳定性 |
| 小区间距 | 500-1000m | 根据路径损耗模型调整 |
| UE 移动距离 | 0m → 500m | 从中心到边缘 |

## 通过标准

1. ✅ UE 在满足 A3 条件后 240ms+5s 内上报 MR
2. ✅ MR 中邻区 RSRP 优于服务小区 RSRP 至少 3dB
3. ✅ 基站正确下发 Handover Command (RRC Reconfiguration)
4. ✅ UE 成功接入目标小区并发送 RRC Reconfiguration Complete
5. ✅ 切换后 PING 时延 < 10ms，无丢包

## 常见失败原因

| 现象 | 可能原因 | 排查方法 |
|------|---------|---------|
| 未上报 A3 MR | 门限设置过高 | 降低 threshold 或增加 offset |
| 上报但未切换 | 邻区未配置/状态异常 | 检查邻区配置是否成功 |
| 切换失败 | 目标小区资源不足 | 检查目标小区状态和容量 |
| 切换后数据不通 | PDU Session 未迁移 | 检查核心网侧配置 |

## 变体场景

### A3 切换 - 负例 (不满足条件)
- 步骤 8 改为：UE 保持在服务小区中心
- 步骤 9 改为：验证无 A3 MR 上报 (timeout=5s)

### A3 切换 - 快速移动
- 步骤 8 改为：UE 从 (0,0) 快速移动到 (800, 0)
- 验证切换时延和成功率

### A3 切换 - 乒乓场景
- UE 在小区边缘来回移动
- 验证迟滞参数是否有效防止乒乓

### A3 切换 - 不同 TTT 验证
- 步骤 5 改为：ttt=480ms 或 1020ms
- 验证切换触发时延
