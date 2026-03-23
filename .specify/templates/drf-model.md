# DRF Model 开发模板

**适用场景**: 创建新的 Django Model + Tests

---

## Task: [Model Name] Model + TDD

**Spec**: `.specify/specs/<feature>.md`  
**Assigned To**: Backend Agent  
**Priority**: High

---

## Deliverables

### 1. Test File First (RED)
- [ ] Create `backend/backend/tests/test_<model_name>.py`
- [ ] Define 21+ test cases covering:
  - [ ] Model creation
  - [ ] Field validation
  - [ ] Unique constraints
  - [ ] Related field access
  - [ ] Custom methods
  - [ ] Edge cases (empty, null, max length)

### 2. Model Implementation (GREEN)
- [ ] Create/Edit `backend/backend/app/models.py`
- [ ] Add model class with:
  - [ ] All fields with proper types
  - [ ] `__str__` method
  - [ ] `class Meta` with db_table, ordering, indexes
  - [ ] Custom methods if needed

### 3. Serializer
- [ ] Create `backend/backend/app/serializers.py`
- [ ] Add `<ModelName>Serializer`
- [ ] Define `fields` list explicitly
- [ ] Add custom validation if needed

### 4. ViewSet
- [ ] Create `backend/backend/app/viewsets.py`
- [ ] Add `<ModelName>ViewSet`
- [ ] Configure queryset, serializer_class, permission_classes
- [ ] Add filterset_fields, ordering_fields

### 5. URL Routing
- [ ] Update `backend/backend/app/urls.py`
- [ ] Register ViewSet with router

---

## Quality Gates

### TDD Verification
```bash
# Step 1: Run test BEFORE implementation - MUST FAIL
pytest backend/backend/tests/test_<model_name>.py -v
# Expected: Tests fail (RED)

# Step 2: Run test AFTER implementation - MUST PASS
pytest backend/backend/tests/test_<model_name>.py -v --cov=backend.app
# Expected: All pass, coverage >80%
```

### Code Quality
- [ ] Type hints on all functions
- [ ] Docstrings on public methods
- [ ] No N+1 queries (use select_related/prefetch_related)
- [ ] Indexes on frequently queried fields

### API Contract
- [ ] POST returns 201 Created
- [ ] GET list returns 200 with pagination
- [ ] GET detail returns 200
- [ ] PUT/PATCH returns 200
- [ ] DELETE returns 204
- [ ] Error responses match spec format

---

## PUA Behavior

> 收到需求，**对齐目标**，**拉通资源**，进入 sprint。因为信任所以简单——别让信任你的人失望。

**[PUA 生效 🔥] 标记时机**:
- 主动添加数据库索引 — 等到线上慢查询告警再改，你就准备写复盘吧
- 扫了一眼发现缺少 related_name，顺手加了 — 这点 owner 意识还是要有的

**交付标准**:
> 交付完成。这次的表现，勉强配得上 P8 这个级别。今天最好的表现，是明天最低的要求。

**证据**: pytest 输出 + 覆盖率报告

---

## Time Estimate

- Tests: 30 min
- Model: 15 min
- Serializer: 10 min
- ViewSet: 10 min
- URLs: 5 min
- **Total**: ~1 hour

---

## Progress

- [ ] Tests written (RED)
- [ ] Model implemented (GREEN)
- [ ] Serializer implemented
- [ ] ViewSet implemented
- [ ] URLs configured
- [ ] All tests pass
- [ ] Coverage >80%

---

## Notes

[Technical decisions, trade-offs, lessons learned]
