# 参数约束专项测试脚本框架规范

本规范用于指导参数约束类测试用例的脚本实现。

## 约束规则分析

参数约束测试的核心是验证 OCL 约束规则的三要素：
- **Trigger（触发条件）**: 什么操作触发了约束检查
- **Target（目标对象）**: 约束规则作用的对象
- **Check Point（检查点）**: 在什么时机进行检查

### 常见约束模式

| 约束模式 | 描述 | 示例 |
|----------|------|------|
| 联动约束 | A 开启时 B 必须开启 | sw1=ON → sw2=ON |
| 互斥约束 | A 开启时 B 必须关闭 | 工作模式 A/B 互斥 |
| 范围约束 | 参数值必须在有效范围内 | 功率 0-100 |
| 依赖约束 | B 的取值依赖 A 的值 | 频段依赖区域配置 |

## 脚本结构

```
scripts/{特性}/
├── conftest.py                  # pytest 配置
├── framework/
│   ├── __init__.py
│   ├── base_test.py             # 基类
│   ├── constraint_helper.py     # 约束检查辅助类
│   └── param_helper.py          # 参数操作辅助类
├── test_cases/
│   ├── __init__.py
│   ├── test_xxx_constraint_001.py
│   └── test_xxx_constraint_002.py
└── run.py                       # 主入口
```

## 核心组件

### 1. OAM 客户端 Fixture

```python
import pytest

@pytest.fixture(scope="session")
def oam_client():
    """OAM 客户端 fixture。

    提供与基站 OAM 系统的连接。
    """
    client = OAMClient(
        host="192.168.1.1",
        port=8080,
        username="admin",
        password="admin"
    )
    client.connect()
    yield client
    client.disconnect()
```

### 2. 参数约束辅助类

```python
class ConstraintHelper:
    """参数约束辅助类。"""

    def __init__(self, client):
        self.client = client

    def verify_constraint(
        self,
        trigger_params: dict,
        target_param: str,
        expected_behavior: str,
        error_msg: str = None
    ) -> tuple[bool, str]:
        """验证约束规则。

        Args:
            trigger_params: 触发条件参数 {param_name: value}
            target_param: 目标参数名
            expected_behavior: "success" 或 "fail"
            error_msg: 预期错误信息（fail 时使用）

        Returns:
            (is_pass, error_detail)
        """
        # 设置触发条件
        for name, value in trigger_params.items():
            self.client.set_param(name, value)

        # 设置目标参数
        result = self.client.commit()

        if expected_behavior == "success":
            if result.success:
                return True, ""
            return False, f"预期成功但失败: {result.error_msg}"
        else:
            if not result.success:
                if error_msg and error_msg in result.error_msg:
                    return True, ""
                return False, f"错误信息不匹配: {result.error_msg}"
            return False, "预期失败但实际成功"
```

### 3. 参数操作辅助类

```python
class ParamHelper:
    """参数操作辅助类。"""

    def __init__(self, client):
        self.client = client

    def set_param(self, param_path: str, value: str) -> bool:
        """设置单个参数。"""
        self.client.set_param(param_path, value)
        return True

    def set_params(self, params: dict[str, str]) -> bool:
        """批量设置参数。"""
        for name, value in params.items():
            self.client.set_param(name, value)
        return True

    def commit(self) -> CommitResult:
        """提交配置。"""
        return self.client.commit()

    def get_param(self, param_path: str) -> str:
        """查询参数值。"""
        return self.client.get_param(param_path)

    def reset_to_default(self, param_path: str) -> bool:
        """重置参数为默认值。"""
        default_value = self.client.get_default(param_path)
        self.client.set_param(param_path, default_value)
        return self.client.commit().success
```

## 测试用例实现模式

### 模式一：正向测试（配置成功）

```python
class TestSwConstraint:
    """sw1/sw2 参数约束测试。"""

    def test_sw1_on_sw2_on_success(
        self,
        oam_client: OAMClient,
        initial_state
    ):
        """【sw1/sw2 约束】sw1 开且 sw2 开配置成功。

        用例编号: gNB-FUNC-001
        测试步骤:
            1. 配置 p1.sw1=ON
            2. 配置 p1.sw2=ON
            3. 提交配置
        预期结果: 配置成功，查询返回 sw1=ON, sw2=ON
        """
        # 前置条件
        oam_client.set_param("p1.sw1", "OFF")
        oam_client.set_param("p1.sw2", "OFF")
        oam_client.commit()

        # 测试步骤
        oam_client.set_param("p1.sw1", "ON")
        oam_client.set_param("p1.sw2", "ON")
        result = oam_client.commit()

        # 断言
        assert result.success, f"配置应该成功: {result.error_msg}"
        assert oam_client.get_param("p1.sw1") == "ON"
        assert oam_client.get_param("p1.sw2") == "ON"
```

### 模式二：负向测试（配置失败）

```python
    def test_sw1_on_sw2_off_fail(
        self,
        oam_client: OAMClient,
        initial_state
    ):
        """【sw1/sw2 约束】sw1 开但 sw2 关被拒绝。

        用例编号: gNB-NEG-001
        测试步骤:
            1. 配置 p1.sw1=ON
            2. 配置 p1.sw2=OFF
            3. 提交配置
        预期结果: 配置失败，提示"sw1 为开时 sw2 必须为开"
        """
        # 前置条件
        oam_client.set_param("p1.sw1", "OFF")
        oam_client.set_param("p1.sw2", "OFF")
        oam_client.commit()

        # 测试步骤
        oam_client.set_param("p1.sw1", "ON")
        oam_client.set_param("p1.sw2", "OFF")
        result = oam_client.commit()

        # 断言
        assert not result.success, "配置应该失败"
        assert "sw1 为开时 sw2 必须为开" in result.error_msg, \
            f"错误信息不匹配: {result.error_msg}"
```

### 模式三：顺序测试

```python
    def test_seq_sw2_first_then_sw1(
        self,
        oam_client: OAMClient,
        initial_state
    ):
        """【sw1/sw2 约束】先开 sw2 再开 sw1 成功。

        用例编号: gNB-FUNC-002
        测试步骤:
            1. 配置 p1.sw2=ON
            2. 提交
            3. 配置 p1.sw1=ON
            4. 提交
        预期结果: 配置成功，查询返回 sw1=ON, sw2=ON
        """
        # 前置条件
        oam_client.set_param("p1.sw1", "OFF")
        oam_client.set_param("p1.sw2", "OFF")
        oam_client.commit()

        # 测试步骤
        oam_client.set_param("p1.sw2", "ON")
        result1 = oam_client.commit()
        assert result1.success, f"步骤2应该成功: {result1.error_msg}"

        oam_client.set_param("p1.sw1", "ON")
        result2 = oam_client.commit()
        assert result2.success, f"步骤4应该成功: {result2.error_msg}"

        # 验证最终状态
        assert oam_client.get_param("p1.sw1") == "ON"
        assert oam_client.get_param("p1.sw2") == "ON"
```

### 模式四：同时下发测试

```python
    def test_batch_sw1_on_sw2_off_fail(
        self,
        oam_client: OAMClient,
        initial_state
    ):
        """【sw1/sw2 约束】同时下发 sw1=ON 和 sw2=OFF 被拒绝。

        用例编号: gNB-NEG-003
        测试步骤:
            1. 同时下发配置 p1.sw1=ON, p1.sw2=OFF
            2. 提交配置
        预期结果: 配置失败，提示"sw1 为开时 sw2 必须为开"
        """
        # 前置条件
        oam_client.set_param("p1.sw1", "OFF")
        oam_client.set_param("p1.sw2", "OFF")
        oam_client.commit()

        # 测试步骤：同时下发
        oam_client.set_param("p1.sw1", "ON")
        oam_client.set_param("p1.sw2", "OFF")
        result = oam_client.commit()

        # 断言
        assert not result.success, "同时下发约束违反的配置应该失败"
        assert "sw1 为开时 sw2 必须为开" in result.error_msg
```

## pytest 配置

### conftest.py

```python
import pytest
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework.oam_client import OAMClient


@pytest.fixture(scope="session")
def oam_client():
    """OAM 客户端 fixture。"""
    client = OAMClient(
        host=os.getenv("OAM_HOST", "192.168.1.1"),
        port=int(os.getenv("OAM_PORT", "8080")),
        username=os.getenv("OAM_USER", "admin"),
        password=os.getenv("OAM_PASS", "admin")
    )
    client.connect()
    yield client
    client.disconnect()


@pytest.fixture
def initial_state(oam_client):
    """初始状态 fixture。

    记录当前状态，测试结束后恢复。
    """
    # 记录初始状态
    initial_params = {
        "p1.sw1": oam_client.get_param("p1.sw1"),
        "p1.sw2": oam_client.get_param("p1.sw2"),
    }
    print(f"\n[initial_state] 记录初始状态: {initial_params}")

    yield initial_params

    # 恢复初始状态
    print(f"[initial_state] 恢复初始状态: {initial_params}")
    for name, value in initial_params.items():
        oam_client.set_param(name, value)
    oam_client.commit()


@pytest.fixture
def cleanup(oam_client):
    """测试后清理 fixture。"""
    yield
    # 清理操作（如需要）
    oam_client.rollback()
```

### pytest.ini

```ini
[pytest]
testpaths = test_cases
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers
markers =
    P0: P0 用例（核心功能）
    P1: P1 用例（重要功能）
    P2: P2 用例（次要功能）
    constraint: 参数约束测试
    counter: Counter 测试
```

## 主入口脚本

### run.py

```python
#!/usr/bin/env python3
"""参数约束测试执行入口。"""

import sys
import os
import argparse

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    parser = argparse.ArgumentParser(description="参数约束测试执行器")
    parser.add_argument(
        "--host",
        default=os.getenv("OAM_HOST", "192.168.1.1"),
        help="OAM 服务器地址"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("OAM_PORT", "8080")),
        help="OAM 端口"
    )
    parser.add_argument(
        "--level",
        choices=["P0", "P1", "P2", "all"],
        default="all",
        help="执行级别"
    )
    parser.add_argument(
        "--case",
        help="指定用例编号（如 gNB-FUNC-001）"
    )

    args = parser.parse_args()

    # 设置环境变量
    os.environ["OAM_HOST"] = args.host
    os.environ["OAM_PORT"] = str(args.port)

    # 构建 pytest 命令
    pytest_args = ["-v", "test_cases/"]

    if args.level != "all":
        pytest_args.extend(["-m", args.level])

    if args.case:
        pytest_args.extend(["-k", args.case])

    # 执行 pytest
    import pytest
    sys.exit(pytest.main(pytest_args))


if __name__ == "__main__":
    main()
```

## 编码规范

1. **命名规范**
   - 测试类：`Test{特性}Constraint`
   - 测试函数：`test_{特性}_{用例名称}_{序号}`
   - Fixture：`{描述性名称}`

2. **文档字符串**
   - 每个测试用例必须包含：用例编号、测试步骤、预期结果
   - 格式参考上述示例

3. **断言消息**
   - 所有断言必须包含清晰的错误消息
   - 消息格式：`"{操作}应该{预期结果}: {实际结果}"`

4. **日志输出**
   - 使用 `print()` 输出关键步骤信息
   - 使用 `[测试阶段]` 前缀标识阶段

5. **错误处理**
   - 捕获异常并给出清晰的错误信息
   - 不要 bare assert，使用 `assert condition, message`

## 执行方式

```bash
# 执行所有用例
python run.py

# 只执行 P0 用例
python run.py --level P0

# 执行指定用例
python run.py --case gNB-FUNC-001

# 指定 OAM 服务器
python run.py --host 192.168.1.100 --port 9090
```
