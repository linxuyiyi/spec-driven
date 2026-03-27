# 快速参考手册 (Quick Reference)

> 一页纸速查。30 秒内找到你要的场景。

---

## 场景选择决策树

```
用户输入测试需求
        │
        ▼
  ┌─────────────┐
  │ 涉及切换吗？ │
  └──────┬──────┘
     ┌───┴───┐
    是       否
     │       │
     ▼       ▼
┌─────────┐  ┌─────────────┐
│同频还是 │  │ 涉及测量吗？ │
│异频？   │  └──────┬──────┘
└────┬────┘      ┌───┴───┐
   ┌─┴─┐        是       否
  同频 异频       │       │
   │   │         ▼       ▼
   ▼   ▼    ┌─────────┐ ┌─────────────┐
  A3   A5   │事件还是 │ │涉及小区吗？ │
           │周期？   │ └──────┬──────┘
           └────┬────┘     ┌───┴───┐
             ┌──┴──┐      是       否
            事件 周期      │       │
             │    │        ▼       ▼
             ▼    ▼   ┌─────────┐ ┌─────────────┐
          RRM   RRM  │建立还是 │ │涉及业务吗？ │
                     │邻区？   │ └──────┬──────┘
                     └────┬────┘     ┌───┴───┐
                       ┌──┴──┐      是       否
                      建立 邻区      │       │
                       │    │        ▼       ▼
                       ▼    ▼   ┌─────────┐ ┌─────────────┐
                   cell-  neigh- │PING 还  │ │负例/约束测试│
                   setup  bor    │是 FTP？ │ └─────────────┘
                                └────┬────┘
                                   ┌─┴─┐
                                  PING FTP
                                   │   │
                                   ▼   ▼
                              service service
```

---

## 一页纸速查表

| 用户说... | 加载场景 | 关键参数 | 验证点 |
|----------|---------|---------|--------|
| "写个切换测试" | handover-a3.md | threshold=-95dBm, offset=3dB | MR 上报、HO Command、切换完成 |
| "A5 异频切换" | handover-a5.md | thres1=-100, thres2=-90 | A5 触发、异频切换 |
| "配置个测量" | measurement-rrm.md | event=A2, thres=-105 | MR 上报 |
| "CQI 上报测试" | csi-measurement.md | ports=8, interval=20ms | CQI/PMI/RI |
| "建个小区" | cell-setup.md | BW=100, SCS=30, PCI=1 | 小区激活、SIB 广播 |
| "加个邻区" | neighbor-config.md | neighbor_cell_id=2, freq=同频 | 邻区添加成功 |
| "RACH 接入" | rach-access.md | preamble 格式=Format 0 | Msg1-Msg4 |
| "PING 测试" | service-test.md | dst_ip=8.8.8.8, count=10 | 时延<10ms, 成功率 100% |
| "FTP 吞吐量" | service-test.md | file_size=100MB | throughput>1Gbps |
| "VoNR 呼叫" | vonr-call.md | 被叫=13800138000 | IMS 注册、呼叫建立、MOS>4.0 |
| "配不上参数" | ocl-constraint-test.md | 参数越界/组合非法 | 错误码验证 |
| "写个负例" | negative-test.md | 非法参数/状态不符 | 配置失败、错误码 |
| "切换中打电话" | composite-scenarios.md | VoNR + A3 HO | 中断<50ms |
| "切换中 PING" | composite-scenarios.md | PING + A3 HO | 丢包<2 个 |
| "弱场接入" | composite-scenarios.md | pathloss=130dB | 接入成功率>95% |

---

## 参数默认值速查

| 参数 | 默认值 | 常见场景 |
|------|--------|---------|
| cell_id | 1 | 所有小区相关 |
| neighbor_cell_id | 2 | 邻区相关 |
| bandwidth | 100 MHz | 小区建立 |
| scs | 30 kHz | 小区建立 |
| arfcn (n78) | 629166 | 小区建立 |
| pci | 1 (同 cell_id) | 小区建立 |
| power | 46 dBm | 小区建立 |
| threshold (A3) | -95 dBm | A3 测量 |
| threshold (A2) | -105 dBm | A2 测量 |
| hysteresis | 3 dB | 所有事件 |
| ttt | 240 ms | 所有事件 |
| offset (A3) | 3 dB | A3 测量 |
| thres1 (A5) | -100 dBm | A5 测量 |
| thres2 (A5) | -90 dBm | A5 测量 |
| timeout | 5 s | 所有验证 |
| imsi | 460001234567890 | UE 附着 |

---

## 常见测试场景组合

| 需求 | 推荐组合 |
|------|---------|
| 完整的切换测试 | handover-a3.md + composite-scenarios.md(CS-01/02) |
| 完整的测量测试 | measurement-rrm.md + csi-measurement.md |
| 完整的小区测试 | cell-setup.md + neighbor-config.md |
| 完整的接入测试 | rach-access.md + composite-scenarios.md(CS-03) |
| 完整的业务测试 | service-test.md + vonr-call.md + composite-scenarios.md(CS-04) |
| 压力/稳定性测试 | rach-access.md(压力) + service-test.md(长稳) + composite-scenarios.md(CS-05) |
| 配置健壮性测试 | ocl-constraint-test.md + negative-test.md |

---

## 3GPP 协议映射速查

| 测试层 | 协议 | 覆盖场景 |
|--------|------|---------|
| RRC | TS 38.331 | handover-a3/a5, measurement-rrm, cell-setup, rach-access |
| 物理层 | TS 38.215 | measurement-rrm, csi-measurement |
| MAC | TS 38.321 | rach-access |
| NG-RAN | TS 38.401 | cell-setup, neighbor-config |
| XnAP | TS 38.423 | neighbor-config, handover-a3/a5 |
| 5G MM | TS 24.501 | vonr-call |
| IMS | TS 26.114 | vonr-call |
| 配置管理 | TS 32.500 | ocl-constraint-test |

---

## 变体场景速查

### 负例测试
| 场景 | 文件 | 变体 |
|------|------|------|
| 参数越界 | ocl-constraint-test.md | PCI 超限、带宽非法、门限超限 |
| 状态不符 | negative-test.md | 未建立删除、已附着再附着 |
| 资源不足 | negative-test.md | 邻区数超限 |
| 配置冲突 | negative-test.md | 同 PCI 冲突 |

### 边界测试
| 场景 | 文件 | 边界 |
|------|------|------|
| 门限边缘 | handover-a5.md | thres1=-98, thres2=-92 |
| CQI 全范围 | csi-measurement.md | pathloss 60→140dB, CQI 15→1 |
| TTT 验证 | handover-a3.md | ttt=240/480/1020ms |

### 压力测试
| 场景 | 文件 | 压力 |
|------|------|------|
| 多 UE 并发 | rach-access.md | 50 UE 同时接入 |
| 多 UE 切换 | composite-scenarios.md | 5 UE 同时切换 |
| 多邻区 | neighbor-config.md | 32 个邻区 |
| 长稳 | service-test.md | 30min 持续传输 |

---

## 版本信息

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 1.0.0 | 2026-03-27 | 初始版本 |
