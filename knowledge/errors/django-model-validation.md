# Django Model 字段验证错误

## 错误现象

```
django.core.exceptions.ValidationError: {'field': ['This field cannot be blank.']}
```

## 触发场景

- 创建或更新 Model 实例时
- 字段值为空字符串但 `blank=False`
- 调用了 `full_clean()` 或 `save()` 之前未验证

## 根因分析

Django Model 的字段默认 `blank=False`，如果传入空字符串会触发验证错误。

## 解决方案

### 方案 1：设置字段允许 blank

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
```

### 方案 2：序列化器中处理

```python
class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
        extra_kwargs = {
            'name': {'allow_blank': True}
        }
```

### 方案 3：清理输入数据

```python
data = {k: v for k, v in data.items() if v != ''}
serializer = MySerializer(data=data)
```

## 预防措施

- [ ] 在 Model 定义时明确 `blank=True/False`
- [ ] 在 Serializer 中设置 `allow_blank`
- [ ] 添加单元测试验证边界情况

## 相关代码

- `templates/backend/apps/__init__.py`

## 时间线

- **首次出现**: 2026-03-25
- **修复时间**: 2026-03-25

## 标签

#django #validation #model #serializer
