| 测试用例编号 | 用例名称 | 前置条件 | 测试步骤 | 预期结果 | 后置条件 |
|--------------|----------|----------|----------|----------|----------|
| PARAM-NEG-001 | 辅小区最大发射功率参数越界校验 (Min-1) | 1. 基站正常运行，网管连接正常<br>2. 目标 MO `SCell` 处于可配置状态，原发射功率为 30dBm | 1. 下发配置命令修改 `SCell` 的 `MaxTxPower` 参数<br>2. 设置值为 -1（有效范围 0~50）<br>3. 提交下发 | 网管拒绝下发，提示值超出范围 [0, 50]；基站侧查询该参数仍为 30dBm | 无需特殊恢复 |
| PARAM-NEG-002 | 辅小区最大发射功率参数越界校验 (Max+1) | 1. 基站正常运行，网管连接正常<br>2. 目标 MO `SCell` 处于可配置状态，原发射功率为 30dBm | 1. 下发配置命令修改 `SCell` 的 `MaxTxPower` 参数<br>2. 设置值为 51（有效范围 0~50）<br>3. 提交下发 | 网管拒绝下发，提示值超出范围 [0, 50]；基站侧查询该参数仍为 30dBm | 无需特殊恢复 |
| PARAM-NEG-003 | 高频 DSS 与载波聚合 (CA) 特性互斥校验 | 1. 基站正常运行<br>2. MO `NRCell` 包含互斥参数 `DssSwitch` 和 `CaSwitch`<br>3. 当前两开关均为 OFF | 1. 下发命令开启 `DssSwitch`<br>2. 再次下发命令尝试开启 `CaSwitch` | 第一条命令成功；第二条命令失败并报错"DSS 与 CA 特性互斥"；系统仅生效 DSS | 关闭 `DssSwitch` 恢复环境初始状态 |
| PARAM-NEG-004 | 载波聚合 CA 与 CA 特性互斥反向校验 | 1. 基站正常运行<br>2. MO `NRCell` 包含互斥参数 `DssSwitch` 和 `CaSwitch`<br>3. 当前两开关均为 OFF | 1. 下发命令开启 `CaSwitch`<br>2. 再次下发命令尝试开启 `DssSwitch` | 第一条命令成功；第二条命令失败并报错"CA 与 DSS 特性互斥"；系统仅生效 CA | 关闭 `CaSwitch` 恢复环境初始状态 |
| PARAM-NEG-005 | 频段指示器枚举值非法字符校验 | 1. 基站正常运行<br>2. MO `NRCellDUFunction` 的 `BandIndicator` 参数有效枚举值为 [n1, n28, n78] | 1. 下发命令配置 `BandIndicator` 参数<br>2. 设置值为 "n999!@#"<br>3. 提交下发 | 网管拒绝下发，提示"非法枚举值"；基站侧参数保持原值 | 无需特殊恢复 |
| PARAM-NEG-006 | 小区建立必填参数缺失校验 | 1. 基站正常运行<br>2. MO `NRCellDUFunction` 包含必填参数 `CellLocalId` | 1. 下发命令创建 `NRCellDUFunction` 对象<br>2. 不提供 `CellLocalId` 参数值<br>3. 提交下发 | 配置被拒绝，返回"缺失必填参数 CellLocalId"错误；对象创建失败 | 无需特殊恢复 |
| PARAM-FUNC-001 | 小区发射功率最小边界值校验 | 1. 基站正常运行<br>2. MO `NRCellDUFunction` 的 `CellTxPower` 有效范围为 [0, 50] | 1. 下发命令配置 `CellTxPower` 参数<br>2. 设置值为 0<br>3. 提交下发<br>4. 查询配置结果 | 配置成功；查询确认参数值为 0；无告警产生 | 恢复参数为原值 |
| PARAM-FUNC-002 | 小区发射功率最大边界值校验 | 1. 基站正常运行<br>2. MO `NRCellDUFunction` 的 `CellTxPower` 有效范围为 [0, 50] | 1. 下发命令配置 `CellTxPower` 参数<br>2. 设置值为 50<br>3. 提交下发<br>4. 查询配置结果 | 配置成功；查询确认参数值为 50；无告警产生 | 恢复参数为原值 |
