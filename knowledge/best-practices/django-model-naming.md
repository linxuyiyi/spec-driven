# Django Model 命名规范

## 场景描述

创建 Django Model 时的命名和结构规范。

## 问题

不规范的命名导致代码可读性差、维护困难。

## 解决方案

### 做法

1. Model 名使用单数，驼峰命名
2. 表名自动生成（app_name_model_name）
3. 字段使用下划线命名
4. 必须包含 `created_at` 和 `updated_at`

### 代码示例

```python
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
    
    def __str__(self):
        return self.user.username
```

### 反模式

```python
# 错误做法 - 避免
class user_profiles(models.Model):  # 小写 + 复数
    userName = models.CharField()   # 驼峰字段
    ...
```

## 原理

统一的命名规范提高代码可读性和团队协作效率。

## 适用范围

- ✅ 所有 Django Model 定义
- ❌ 中间表（ManyToMany through）可以使用复数

## 相关资源

- [Django Model 文档](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Style Guide](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/)

## 标签

#best-practice #django #model #naming #code-quality
