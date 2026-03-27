# Pattern 索引目录

> 快速检索所有测试场景、变体、关键词。按业务域组织，端到端拉通。

---

## 场景总览

| 序号 | 场景名称 | 文件 | 变体数 | 核心验证点 |
|------|---------|------|--------|-----------|
| 1 | A3 同频切换 | `handover-a3.md` | 4 | MR 上报、HO Command、切换完成 |
| 2 | A5 异频切换 | `handover-a5.md` | 4 | A5 触发、异频切换、GAP 配置 |
| 3 | RRM 测量 | `measurement-rrm.md` | 6 | A1-A6 事件、周期上报 |
| 4 | CSI 测量 | `csi-measurement.md` | 4 | CQI/PMI/RI 上报、波束切换 |
| 5 | 小区建立 | `cell-setup.md` | 5 | 小区激活、SIB 广播、UE 附着 |
| 6 | 邻区配置 | `neighbor-config.md` | 5 | 邻区添加/删除/修改 |
| 7 | 随机接入 | `rach-access.md` | 5 | Msg1-Msg4、CBRA/CFRA、BFR |
| 8 | 业务测试 | `service-test.md` | 5 | PING 时延、FTP 吞吐量 |
| 9 | VoNR 呼叫 | `vonr-call.md` | 5 | IMS 注册、呼叫建立、MOS 分 |
| 10 | 负例测试 | `negative-test.md` | 多类别 | 参数非法、状态不符、资源不足 |
| 11 | OCL 约束 | `ocl-constraint-test.md` | 8 | 范围/条件/依赖/互斥约束 |

**合计**：11 个主场景，50+ 变体场景

---

## 按业务域索引

### 移动性管理 (Mobility)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| A3 同频切换 | `handover-a3.md` | A3、同频切换、intra-freq | 正常流程、负例、快速移动、乒乓、TTT 验证 |
| A5 异频切换 | `handover-a5.md` | A5、异频切换、inter-freq | 正常流程、门限边缘、迟滞验证、TTT 验证、负例 |

### 测量管理 (Measurement)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| RRM 测量 | `measurement-rrm.md` | RRM、MR、A1/A2/A3/A4/A5、RSRP | A1-A6 事件、周期上报、多事件并发、联合测试 |
| CSI 测量 | `csi-measurement.md` | CSI、CQI、PMI、RI、波束 | 周期上报、非周期上报、多波束、全范围扫描 |

### 接入管理 (Access)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| 随机接入 | `rach-access.md` | RACH、preamble、接入、Msg1 | CBRA、CFRA、BFR、压力测试、弱场接入 |

### 小区管理 (Cell Management)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| 小区建立 | `cell-setup.md` | 小区建立、cell setup | 正常流程、多小区、删除重建、参数修改、负例 |
| 邻区配置 | `neighbor-config.md` | 邻区、neighbor、Xn | 同频邻区、异频邻区、删除、修改、多邻区、负例 |

### 业务测试 (Service)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| PING/FTP | `service-test.md` | PING、吞吐量、FTP | PING、FTP 下载、FTP 上传、多 UE 并发、移动中业务、长稳 |
| VoNR | `vonr-call.md` | VoNR、语音、呼叫 | 主叫、被叫、EPS Fallback、切换中保持、并发业务、连续呼叫 |

### 运维管理 (O&M)

| 场景 | 文件 | 触发关键词 | 变体 |
|------|------|-----------|------|
| OCL 约束 | `ocl-constraint-test.md` | OCL、参数约束、OMC、校验 | 范围约束、条件约束、依赖约束、互斥约束、数量约束、长度约束、批量配置 |
| 负例测试 | `negative-test.md` | 负例、失败、异常、非法 | 参数非法、状态不符、资源不足、配置冲突、超时 |

---

## 关键词速查表

### 切换相关
| 用户说法 | 映射场景 |
|---------|---------|
| "切不过去" | handover-a3.md / handover-a5.md |
| "乒乓切换" | handover-a3.md (乒乓场景变体) |
| "切换掉话" | handover-a3.md + vonr-call.md (切换中保持) |

### 测量相关
| 用户说法 | 映射场景 |
|---------|---------|
| "不上报 MR" | measurement-rrm.md |
| "CQI 不准" | csi-measurement.md |
| "波束失败" | rach-access.md (BFR 变体) |

### 接入相关
| 用户说法 | 映射场景 |
|---------|---------|
| "附着不上" | rach-access.md |
| "RACH 失败" | rach-access.md |
| "弱场接入" | rach-access.md (弱场变体) |

### 业务相关
| 用户说法 | 映射场景 |
|---------|---------|
| "PING 不通" | service-test.md |
| "速率低" | service-test.md (FTP 吞吐量) |
| "语音掉话" | vonr-call.md |

### 配置相关
| 用户说法 | 映射场景 |
|---------|---------|
| "参数配不进去" | ocl-constraint-test.md |
| "配置报错" | ocl-constraint-test.md / negative-test.md |
| "邻区加不上" | neighbor-config.md |

---

## 变体场景清单 (按测试目的)

### 正常流程验证
- `handover-a3.md` - A3 切换正常流程
- `handover-a5.md` - A5 切换正常流程
- `measurement-rrm.md` - A2 事件正常流程
- `cell-setup.md` - 小区建立正常流程
- `service-test.md` - PING/FTP 正常流程
- `vonr-call.md` - VoNR 主叫正常流程
- `rach-access.md` - CBRA 正常流程

### 负例/异常验证
- `handover-a3.md` - 不满足条件不上报
- `handover-a5.md` - 不满足条件不上报
- `cell-setup.md` - 非法 PCI 测试
- `neighbor-config.md` - 重复添加邻区
- `service-test.md` - 数据通路未建立
- `negative-test.md` - 通用负例模板
- `ocl-constraint-test.md` - 参数越界测试

### 边界/压力验证
- `handover-a5.md` - 门限边缘测试
- `csi-measurement.md` - CQI 全范围扫描
- `rach-access.md` - 50 UE 压力测试
- `ocl-constraint-test.md` - 邻区数超限测试
- `service-test.md` - 长稳测试 (30min)

### 组合场景验证
- `vonr-call.md` - 切换中保持通话
- `vonr-call.md` - 通话 + 数据并发
- `service-test.md` - 移动中 PING
- `service-test.md` - 多 UE 并发 PING
- `csi-measurement.md` - 多波束切换

---

## 协议覆盖映射

| 3GPP 协议 | 覆盖场景 |
|----------|---------|
| TS 38.331 (RRC) | handover-a3/a5, measurement-rrm, cell-setup, rach-access |
| TS 38.215 (物理层测量) | measurement-rrm, csi-measurement |
| TS 38.321 (MAC) | rach-access |
| TS 38.401 (NG-RAN 架构) | cell-setup, neighbor-config |
| TS 38.423 (XnAP) | neighbor-config, handover-a3/a5 |
| TS 24.501 (5G MM) | vonr-call |
| TS 26.114 (IMS 语音) | vonr-call |
| TS 32.500 (配置管理) | ocl-constraint-test |

---

## 待补充场景 (Backlog)

| 场景 | 优先级 | 说明 |
|------|--------|------|
| 载波聚合 (CA) | P1 | 主辅小区配置、SCell 激活/去激活 |
| 双连接 (EN-DC) | P1 | LTE+NR 双连接、分流测试 |
| 网络切片 | P2 | DNN 配置、切片选择 |
| 定位测试 | P2 | LTE Positioning、NR Positioning |
| 节能测试 | P3 | 小区休眠、符号关断 |
| PDCP 测试 | P2 | 重排序、重复检测 |
| RLC 测试 | P2 | AM/UM/TM 模式、分段重组 |

---

## 版本信息

| 版本 | 日期 | 更新内容 | 作者 |
|------|------|---------|------|
| 1.0.0 | 2026-03-27 | 初始版本，11 个场景 | - |
