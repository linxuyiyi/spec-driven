# 规格：公告管理系统 (Bulletin Board)

## Overview

公告管理系统用于发布、管理和展示系统公告。支持公告的创建、编辑、删除、发布状态管理，以及列表展示和详情查看。

---

## API Contract

### 1. List Bulletins
- **Endpoint**: `GET /api/bulletins/`
- **Query Params**:
  - `status` (optional): Filter by status (`DRAFT`, `PUBLISHED`, `ARCHIVED`)
  - `search` (optional): Search in title and content
  - `page` (optional): Page number (default: 1)
  - `page_size` (optional): Items per page (default: 20, max: 100)
- **Response** (200 OK):
```json
{
  "count": 50,
  "next": "/api/bulletins/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "系统维护通知",
      "content": "系统将于本周末进行维护...",
      "status": "PUBLISHED",
      "priority": "HIGH",
      "author": "admin",
      "published_at": "2026-03-20T10:00:00Z",
      "created_at": "2026-03-19T15:30:00Z",
      "updated_at": "2026-03-20T10:00:00Z"
    }
  ]
}
```

### 2. Get Bulletin Detail
- **Endpoint**: `GET /api/bulletins/{id}/`
- **Response** (200 OK):
```json
{
  "id": 1,
  "title": "系统维护通知",
  "content": "系统将于本周末进行维护...",
  "status": "PUBLISHED",
  "priority": "HIGH",
  "author": "admin",
  "published_at": "2026-03-20T10:00:00Z",
  "created_at": "2026-03-19T15:30:00Z",
  "updated_at": "2026-03-20T10:00:00Z"
}
```

### 3. Create Bulletin
- **Endpoint**: `POST /api/bulletins/`
- **Request**:
```json
{
  "title": "新功能上线通知",
  "content": "我们很高兴地宣布...",
  "status": "DRAFT",
  "priority": "NORMAL"
}
```
- **Response** (201 Created):
```json
{
  "id": 2,
  "title": "新功能上线通知",
  "content": "我们很高兴地宣布...",
  "status": "DRAFT",
  "priority": "NORMAL",
  "author": "current_user",
  "published_at": null,
  "created_at": "2026-03-24T10:00:00Z",
  "updated_at": "2026-03-24T10:00:00Z"
}
```

### 4. Update Bulletin
- **Endpoint**: `PUT /api/bulletins/{id}/` or `PATCH /api/bulletins/{id}/`
- **Request**:
```json
{
  "title": "更新后的标题",
  "status": "PUBLISHED"
}
```
- **Response** (200 OK): Bulletin object

### 5. Delete Bulletin
- **Endpoint**: `DELETE /api/bulletins/{id}/`
- **Response** (204 No Content): Success

### 6. Publish Bulletin
- **Endpoint**: `POST /api/bulletins/{id}/publish/`
- **Request**: Empty body
- **Response** (200 OK):
```json
{
  "id": 1,
  "title": "系统维护通知",
  "status": "PUBLISHED",
  "published_at": "2026-03-24T10:00:00Z",
  ...
}
```

---

## Data Models

### Bulletin Model
```python
class Bulletin(models.Model):
    """系统公告模型。"""
    
    STATUS_CHOICES = [
        ('DRAFT', '草稿'),
        ('PUBLISHED', '已发布'),
        ('ARCHIVED', '已归档'),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW', '低'),
        ('NORMAL', '普通'),
        ('HIGH', '高'),
        ('URGENT', '紧急'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='NORMAL')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'bulletin'
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['status', 'published_at']),
            models.Index(fields=['priority', 'status']),
        ]
```

---

## UI Requirements (UI-UX-Pro-Max)

### 公告列表页

**Layout**:
- 卡片式布局，每个公告一个卡片
- 顶部有搜索框和状态筛选
- 支持分页

**颜色**:
- 紧急公告：`bg-red-50 border-red-500`
- 高优先级：`bg-orange-50 border-orange-500`
- 普通：`bg-white border-gray-200`
- 状态标签：`status-badge` 样式

**状态展示**:
- 草稿：灰色标签
- 已发布：绿色标签
- 已归档：蓝色标签

**空状态**:
- 无公告时显示空状态插图和提示文字
- 提供"发布第一个公告"按钮 (管理员)

### 公告详情页

**Layout**:
- 标题大号显示
- 元信息 (作者/发布时间/优先级)
- 内容区域支持富文本展示

**优先级标识**:
- 紧急：红色徽章
- 高：橙色徽章
- 普通：灰色徽章

### 发布/编辑表单页

**表单字段**:
- 标题：必填，最大 200 字符
- 内容：必填，多行文本
- 优先级：下拉选择
- 状态：草稿/发布

**验证**:
- 标题不能为空
- 内容不能为空
- 发布时检查必填字段

---

## Test Cases (Superpower)

### Backend Tests

#### Model Tests
- [ ] **test_bulletin_creation**: 创建公告成功
- [ ] **test_bulletin_str**: `__str__` 返回标题
- [ ] **test_default_status**: 默认状态为 DRAFT
- [ ] **test_default_priority**: 默认优先级为 NORMAL
- [ ] **test_published_at_auto_set**: 发布时自动设置 published_at

#### Serializer Tests
- [ ] **test_serializer_valid**: 有效数据序列化成功
- [ ] **test_serializer_required_fields**: 必填字段验证
- [ ] **test_serializer_status_choices**: 状态选项验证

#### ViewSet Tests
- [ ] **test_list_bulletins**: 列表接口返回分页数据
- [ ] **test_create_bulletin**: 创建公告成功 (201)
- [ ] **test_get_bulletin_detail**: 获取详情成功
- [ ] **test_update_bulletin**: 更新公告成功
- [ ] **test_delete_bulletin**: 删除公告成功 (204)
- [ ] **test_publish_bulletin**: 发布公告成功，设置 published_at
- [ ] **test_filter_by_status**: 按状态筛选
- [ ] **test_search_by_title**: 按标题搜索

### Frontend Tests
- [ ] **test_bulletin_list_page**: 列表页渲染
- [ ] **test_bulletin_detail_page**: 详情页渲染
- [ ] **test_create_bulletin_form**: 创建表单提交
- [ ] **test_status_filter**: 状态筛选功能
- [ ] **test_empty_state**: 空状态显示

---

## Backend Implementation Checklist

- [ ] Create `Bulletin` model with all fields
- [ ] Create `BulletinSerializer`
- [ ] Create `BulletinViewSet` with actions: list, retrieve, create, update, destroy, publish
- [ ] Register ViewSet in urls.py
- [ ] Write all tests in `tests/test_bulletin.py`
- [ ] Add admin interface for Bulletin

---

## Frontend Implementation Checklist

- [ ] Create types: `Bulletin`, `BulletinStatus`, `BulletinPriority`
- [ ] Create API client: `bulletinApi.ts`
- [ ] Create Pinia store: `bulletinStore.ts`
- [ ] Create views:
  - `BulletinList.vue` (列表页)
  - `BulletinDetail.vue` (详情页)
  - `BulletinForm.vue` (表单页)
- [ ] Create components:
  - `BulletinCard.vue` (公告卡片)
  - `BulletinStatusBadge.vue` (状态标签)
  - `BulletinPriorityBadge.vue` (优先级标签)
- [ ] Add routes for bulletin pages
- [ ] Implement empty state
- [ ] Implement loading/error states

---

## Files to Create/Modify

### Backend
- `backend/app/models.py` (add Bulletin model)
- `backend/app/serializers.py` (add BulletinSerializer)
- `backend/app/viewsets.py` (add BulletinViewSet)
- `backend/app/urls.py` (register routes)
- `backend/tests/test_bulletin.py` (all tests)

### Frontend
- `frontend/src/types/bulletin.ts`
- `frontend/src/api/bulletin.ts`
- `frontend/src/stores/bulletin.ts`
- `frontend/src/views/bulletin/BulletinList.vue`
- `frontend/src/views/bulletin/BulletinDetail.vue`
- `frontend/src/views/bulletin/BulletinForm.vue`
- `frontend/src/components/bulletin/BulletinCard.vue`
- `frontend/src/components/bulletin/BulletinStatusBadge.vue`
- `frontend/src/components/bulletin/BulletinPriorityBadge.vue`
- `frontend/src/router/index.ts` (add routes)

---

## Spec Version
- **Version**: 1.0.0
- **Created**: 2026-03-24
- **Status**: Approved
