# AW 函数目录

> 本文档是 AW 测试函数的检索目录，详细实现见各模块源代码。
> 
> **使用位置索引**：每个函数下方标注了在哪些 Pattern 中被使用。

---

## 环境控制

| 函数 | 功能 | 参数 | 使用位置 |
|------|------|------|---------|
| `aw_reset_test_env()` | 重置测试环境 | - | **全部 Pattern** |
| `aw_log(msg)` | 记录测试日志 | msg: 日志内容 | 所有需要日志的步骤 |
| `aw_sleep(seconds)` | 等待指定时间 | seconds: 秒数 | cell-setup.md, handover-a3/a5.md |

---

## 小区管理 (aw_cell.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_cell_setup()` | 建立 NR 小区 | cell_id, bandwidth, scs, arfcn, pci, power | **全部 Pattern** |
| `aw_cell_delete()` | 删除小区 | cell_id | cell-setup.md(删除重建变体) |
| `aw_cell_modify()` | 修改小区参数 | cell_id, **kwargs | cell-setup.md(参数修改变体) |
| `aw_get_cell_state()` | 获取小区状态 | cell_id | cell-setup.md |

### aw_cell_setup 参数详解
```python
aw_cell_setup(
    cell_id: int,           # 小区 ID (0-255)
    bandwidth: int,         # 带宽 MHz (50/100/200)
    scs: int,               # 子载波间隔 kHz (15/30/60)
    arfcn: int,             # 频点号
    pci: int,               # 物理小区 ID (0-1007)
    power: int = 46,        # 发射功率 dBm
    cell_name: str = None   # 小区名称 (可选)
)
```

---

## 邻区配置 (aw_neighbor.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_neighbor_add()` | 添加邻区关系 | cell_id, neighbor_cell_id, nci, pci, freq | handover-a3/a5.md, neighbor-config.md, composite-scenarios.md |
| `aw_neighbor_remove()` | 删除邻区关系 | cell_id, neighbor_cell_id | neighbor-config.md(删除变体) |
| `aw_neighbor_modify()` | 修改邻区参数 | cell_id, neighbor_cell_id, **kwargs | neighbor-config.md(修改变体) |
| `aw_get_neighbor_list()` | 获取邻区列表 | cell_id | neighbor-config.md |

### aw_neighbor_add 参数详解
```python
aw_neighbor_add(
    cell_id: int,           # 服务小区 ID
    neighbor_cell_id: int,  # 邻区 ID
    nci: int,               # NR Cell Identity
    pci: int,               # 邻区 PCI
    freq: int,              # 邻区频点
    qoffset: int = 0        # 小区偏移 (可选)
)
```

---

## UE 操作 (aw_ue.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_ue_attach()` | UE 附着 | ue_id, imsi, pdu_type, dnn | **全部 Pattern** |
| `aw_ue_detach()` | UE 去附着 | ue_id | - |
| `aw_ue_move()` | 移动 UE 位置 | ue_id, x, y, z | handover-a3/a5.md, composite-scenarios.md |
| `aw_ue_set_pathloss()` | 设置路径损耗 | ue_id, pathloss_db | handover-a5.md, measurement-rrm.md, csi-measurement.md |
| `aw_ue_power_control()` | 设置 UE 发射功率 | ue_id, tx_power_dbm | - |
| `aw_ue_get_state()` | 获取 UE 状态 | ue_id | cell-setup.md |
| `aw_ue_set_speed()` | 设置 UE 移动速度 | ue_id, speed_kmh | - |

### aw_ue_attach 参数详解
```python
aw_ue_attach(
    ue_id: int,                     # UE 标识
    imsi: str,                      # IMSI 号
    pdu_type: str = "IPv4",         # PDU Session 类型
    dnn: str = "internet",          # DNN
    s_nssai: str = None             # 切片标识 (可选)
)
```

### aw_ue_move 参数详解
```python
aw_ue_move(
    ue_id: int,         # UE 标识
    x: float,           # X 坐标 (米)
    y: float = 0,       # Y 坐标 (米)
    z: float = 0        # Z 坐标 (米)
)
```

---

## 测量配置 (aw_rrm.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_cfg_meas_a1()` | 配置 A1 事件 | cell_id, threshold, hysteresis, ttt | measurement-rrm.md |
| `aw_cfg_meas_a2()` | 配置 A2 事件 | cell_id, threshold, hysteresis, ttt | measurement-rrm.md |
| `aw_cfg_meas_a3()` | 配置 A3 事件 | cell_id, threshold, hysteresis, ttt, offset | handover-a3.md, composite-scenarios.md |
| `aw_cfg_meas_a4()` | 配置 A4 事件 | cell_id, threshold, hysteresis, ttt | measurement-rrm.md |
| `aw_cfg_meas_a5()` | 配置 A5 事件 | cell_id, thres1, thres2, hysteresis, ttt | handover-a5.md |
| `aw_cfg_meas_a6()` | 配置 A6 事件 | cell_id, threshold, hysteresis, ttt, offset | - |
| `aw_cfg_meas_period()` | 配置周期上报 | cell_id, interval_ms | measurement-rrm.md, csi-measurement.md |
| `aw_cfg_csi_rs()` | 配置 CSI-RS | cell_id, resource_id, ports, density | csi-measurement.md |
| `aw_cfg_meas_gap()` | 配置测量 GAP | ue_id, gap_pattern, gap_offset | handover-a5.md(异频切换) |

### aw_cfg_meas_a3 参数详解
```python
aw_cfg_meas_a3(
    cell_id: int,         # 小区 ID
    threshold: int,       # 门限 dBm
    hysteresis: int,      # 迟滞 dB
    ttt: int,             # 触发时间 ms (240/480/1020)
    offset: int = 3       # A3 偏移 dB
)
```

### aw_cfg_meas_a5 参数详解
```python
aw_cfg_meas_a5(
    cell_id: int,         # 小区 ID
    thres1: int,          # 服务小区门限 dBm
    thres2: int,          # 邻区门限 dBm
    hysteresis: int,      # 迟滞 dB
    ttt: int              # 触发时间 ms
)
```

---

## 验证函数 (aw_verify.py)

| 函数 | 功能 | 返回值 | 关键参数 | 使用位置 |
|------|------|--------|---------|---------|
| `aw_verify_mr()` | 验证测量报告 | (success, mr_content) | ue_id, event_type, timeout, expected | handover-a3/a5.md, measurement-rrm.md |
| `aw_verify_ho_cmd()` | 验证切换命令 | (success, rrc_msg) | source_cell, target_cell, timeout | handover-a3/a5.md, composite-scenarios.md |
| `aw_verify_ho_complete()` | 验证切换完成 | (success, msg) | ue_id, target_cell, timeout | handover-a3/a5.md, composite-scenarios.md |
| `aw_verify_data_path()` | 验证数据通路 | (success, ping_result) | ue_id, timeout | handover-a3/a5.md, service-test.md, vonr-call.md |
| `aw_verify_cell_state()` | 验证小区状态 | (success, state) | cell_id, expected_state, timeout | cell-setup.md, neighbor-config.md |
| `aw_verify_ue_state()` | 验证 UE 状态 | (success, state) | ue_id, expected_state, timeout | cell-setup.md, rach-access.md |
| `aw_verify_no_mr()` | 验证无 MR 上报 | (success, _) | ue_id, timeout | handover-a3/a5.md(负例) |
| `aw_verify_sys_info()` | 验证系统广播 | (success, sib_content) | cell_id, sib_type, timeout | cell-setup.md |

### aw_verify_mr 参数详解
```python
aw_verify_mr(
    ue_id: int,                   # UE 标识
    event_type: str,              # 事件类型 (A1/A2/A3/A4/A5/PERIODIC)
    timeout: int = 5,             # 超时时间 秒
    expected: bool = True         # 是否期望上报
) -> tuple[bool, dict]
```

---

## 业务测试 (aw_service.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_ping()` | 执行 PING 测试 | ue_id, dst_ip, count, timeout | service-test.md, composite-scenarios.md |
| `aw_ftp_upload()` | FTP 上传测试 | ue_id, file_size, server_ip | service-test.md |
| `aw_ftp_download()` | FTP 下载测试 | ue_id, file_size, server_ip | service-test.md, composite-scenarios.md |
| `aw_vonr_call()` | VoNR 呼叫测试 | ue_id, callee_number, duration | vonr-call.md, composite-scenarios.md |
| `aw_http_request()` | HTTP 请求测试 | ue_id, url, method | - |

---

## RACH 相关 (aw_rach.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_rach_config()` | 配置 RACH 参数 | cell_id, preamble_format, prach_config | rach-access.md |
| `aw_rach_trigger()` | 触发 RACH | ue_id | rach-access.md |
| `aw_verify_rar()` | 验证 RAR | ue_id, timeout | rach-access.md |
| `aw_verify_msg4()` | 验证 Msg4 | ue_id, timeout | rach-access.md |

---

## VoNR 相关 (aw_vonr.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_ims_register()` | IMS 注册 | ue_id, p_cscf, dnn | vonr-call.md, composite-scenarios.md |
| `aw_ims_call()` | 发起 IMS 呼叫 | caller_ue_id, callee_number | vonr-call.md, composite-scenarios.md |
| `aw_verify_call_state()` | 验证呼叫状态 | ue_id, expected_state | vonr-call.md |
| `aw_verify_mos()` | 验证 MOS 分 | ue_id, duration | vonr-call.md, composite-scenarios.md |
| `aw_call_release()` | 释放呼叫 | ue_id | vonr-call.md |

---

## OCL 相关 (aw_ocl.py)

| 函数 | 功能 | 关键参数 | 使用位置 |
|------|------|---------|---------|
| `aw_ocl_connect()` | 建立 OCL 连接 | ocl_address, port | ocl-constraint-test.md |
| `aw_ocl_configure()` | OCL 配置参数 | param_name, param_value | ocl-constraint-test.md |
| `aw_ocl_verify()` | OCL 验证配置 | param_name, expected_value | ocl-constraint-test.md |
| `aw_ocl_disconnect()` | 断开 OCL 连接 | - | ocl-constraint-test.md |

---

## 常用参数默认值

| 参数 | 默认值 | 说明 |
|------|--------|------|
| cell_id | 1 | 服务小区 ID |
| neighbor_cell_id | 2 | 邻区 ID |
| bandwidth | 100 | 带宽 MHz |
| scs | 30 | 子载波间隔 kHz |
| pci | 同 cell_id | 物理小区 ID |
| power | 46 | 发射功率 dBm |
| threshold (A3) | -95 | 门限 dBm |
| hysteresis | 3 | 迟滞 dB |
| ttt | 240 | 触发时间 ms |
| imsi | "460001234567890" | 测试 IMSI |
| timeout | 5 | 验证超时秒数 |

---

## 函数查找指南

**按测试场景查找**：

| 场景 | 相关函数 |
|------|---------|
| 小区建立 | aw_cell_setup, aw_verify_cell_state, aw_verify_sys_info |
| 切换测试 | aw_neighbor_add, aw_cfg_meas_a3/a5, aw_verify_ho_*, aw_ue_move |
| 测量测试 | aw_cfg_meas_*, aw_cfg_csi_rs, aw_verify_mr |
| UE 移动 | aw_ue_move, aw_ue_set_pathloss |
| 业务测试 | aw_ping, aw_ftp_*, aw_vonr_call, aw_ims_* |
| RACH 测试 | aw_rach_*, aw_verify_rar, aw_verify_msg4 |
| OCL 测试 | aw_ocl_*, aw_ocl_verify |

---

## 更新记录

| 日期 | 更新内容 | 负责人 |
|------|---------|--------|
| 2026-03-27 | 初始版本 + 使用位置索引 | - |
