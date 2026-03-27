# 随机接入测试 Pattern

## 触发关键词

- 中文：随机接入、RACH、前导、preamble、接入
- 英文：random access、RACH、preamble、access

## 测试目的

验证 UE 能够正确执行随机接入流程，包括基于竞争的随机接入 (CBRA) 和无竞争随机接入 (CFRA)。

## 协议参考

- 3GPP TS 38.321: MAC 协议
- 3GPP TS 38.213: 物理层控制
- 3GPP TS 38.331: RRC 协议 - RACH 配置

## 随机接入类型

| 类型 | 说明 | 使用场景 |
|------|------|---------|
| CBRA | 基于竞争的随机接入 | 初始接入、RRC 重建 |
| CFRA | 无竞争随机接入 | 切换、波束失败恢复 |

## 随机接入流程 (4 步 RACH)

| 步骤 | 消息 | 方向 | 内容 |
|------|------|------|------|
| 1 | Msg1 | UE→gNB | Preamble 发送 |
| 2 | Msg2 | gNB→UE | RAR (Random Access Response) |
| 3 | Msg3 | UE→gNB | RRC Setup Request |
| 4 | Msg4 | gNB→UE | Contention Resolution |

## 标准步骤序列 (初始接入 - CBRA)

| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1 | 环境重置 | 清空残留配置，重置测试环境 | - | 环境干净 |
| 2 | 小区建立 | 建立 NR 服务小区 | cell_id=1, BW=100MHz, SCS=30kHz | 小区状态 ACTIVE |
| 3 | RACH 配置验证 | 验证 SIB1 中 RACH 配置广播 | - | RACH 配置正确 |
| 4 | UE 上电 | UE 上电并搜索小区 | - | UE 搜索到小区 |
| 5 | 同步 | UE 执行 PSS/SSS 同步 | - | 同步成功 |
| 6 | MIB 获取 | UE 读取 MIB | - | MIB 获取成功 |
| 7 | SIB1 获取 | UE 读取 SIB1 | - | SIB1 获取成功，含 RACH 配置 |
| 8 | Msg1 发送 | UE 发送 Preamble | preamble_index=随机选择 | Preamble 发送成功 |
| 9 | Msg2 接收 | UE 接收 RAR | timeout=10ms | 收到 RAR，含 TA 和 UL grant |
| 10 | Msg3 发送 | UE 发送 RRC Setup Request | - | Msg3 发送成功 |
| 11 | Msg4 接收 | UE 接收 RRC Setup | timeout=20ms | 收到 RRC Setup |
| 12 | 接入完成验证 | UE 进入 RRC CONNECTED 态 | - | 状态=CONNECTED |

## 关键参数推荐值

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| preamble 格式 | Format 0 | 常用格式 |
| RACH SCS | 1.25kHz 或 5kHz | 前导子载波间隔 |
| RACH 时频资源 | SIB1 指示 | 由网络配置 |
| 功率爬坡步长 | 2dB | 每次重传增加 |
| 最大重传次数 | 10 | preambleTransMax |

## 通过标准

### CBRA 测试
1. ✅ UE 正确获取 RACH 配置
2. ✅ UE 正确选择 preamble 并发送
3. ✅ UE 在 10ms 内收到 RAR
4. ✅ RAR 中包含正确的 TA 和 UL grant
5. ✅ Msg3 发送成功
6. ✅ 竞争解决成功，UE 进入 CONNECTED 态

### CFRA 测试
1. ✅ 网络正确分配专用 preamble
2. ✅ UE 使用专用 preamble 发送
3. ✅ UE 收到 RAR
4. ✅ 接入成功

## 常见失败原因

| 现象 | 可能原因 | 排查方法 |
|------|---------|---------|
| 未收到 RAR | preamble 检测失败 | 检查接收功率、前导格式 |
| RAR 解析失败 | RNTI 错误 | 检查 RA-RNTI 计算 |
| Msg3 发送失败 | UL grant 解析错误 | 检查 DCI 格式 |
| 竞争解决失败 | 多 UE 同 preamble | 检查 preamble 资源 |
| 接入超时 | 重传次数超限 | 检查功率爬坡配置 |

## 变体场景

### CFRA 切换场景测试
| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1-2 | 环境重置、小区建立 | 同上 | - | - |
| 3 | 服务小区建立 | 建立服务小区 | cell_id=1 | ACTIVE |
| 4 | 邻区建立 | 建立邻区 | cell_id=2 | ACTIVE |
| 5 | UE 附着服务小区 | UE 附着到服务小区 | - | CONNECTED |
| 6 | 切换准备 | 网络准备切换，分配专用 preamble | preamble=专用 | preamble 分配成功 |
| 7 | 切换命令 | 下发 RRC Reconfiguration | - | 命令发送成功 |
| 8 | CFRA 执行 | UE 在邻区执行 CFRA | 使用专用 preamble | Msg1 发送成功 |
| 9 | RAR 接收 | UE 接收 RAR | timeout=10ms | 收到 RAR |
| 10 | 切换完成 | UE 接入邻区 | - | 切换完成 |

### 波束失败恢复测试
| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1-5 | 环境重置到接入完成 | 同上 | - | UE 已接入 |
| 6 | 波束失败触发 | 阻塞当前波束 | - | 波束失败检测 |
| 7 | BFR 请求 | UE 发送 BFR preamble | - | BFR 请求发送 |
| 8 | gNB 响应 | gNB 发送新的波束指示 | - | 新波束激活 |
| 9 | 恢复验证 | 验证链路恢复 | - | 通信恢复 |

### RACH 压力测试
| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1-2 | 环境重置、小区建立 | 同上 | - | - |
| 3 | UE1 接入 | UE1 执行随机接入 | - | 接入成功 |
| 4 | UE2 接入 | UE2 执行随机接入 | - | 接入成功 |
| 5 | UE3 接入 | UE3 执行随机接入 | - | 接入成功 |
| ... | ... | ... | ... | ... |
| N | UE50 接入 | UE50 执行随机接入 | - | 接入成功 |
| N+1 | 统计结果 | 统计 50 个 UE 接入成功率 | - | 成功率 > 95% |

### 弱场接入测试
| 步骤 | 步骤名 | 操作描述 | 参数 | 预期结果 |
|------|--------|---------|------|---------|
| 1-2 | 环境重置、小区建立 | 同上 | - | - |
| 3 | 弱场配置 | 配置高 pathloss | pathloss=130dB | 信号弱 |
| 4-7 | 同步、MIB、SIB1 获取 | 同上 | - | 获取成功 |
| 8 | Msg1 发送 | UE 发送 Preamble (可能多次重传) | - | Preamble 发送 |
| 9 | Msg2 接收 | UE 接收 RAR | timeout=50ms | 收到 RAR |
| 10-12 | Msg3、Msg4、接入完成 | 同上 | - | 接入成功 |
