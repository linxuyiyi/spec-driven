# Skill: spec-analyzer

## 需求规格解析器

解析模板化的 Spec 文档，提取结构化需求。

---

## 输入

Spec Markdown 文件，遵循 `templates/specs/feature-spec-template.md` 格式。

---

## 输出

```json
{
  "feature_name": "功能名称",
  "user_stories": ["用户故事 1", "用户故事 2"],
  "data_models": [
    {
      "name": "Model 名",
      "fields": [
        {"name": "字段名", "type": "类型", "required": true, "description": "说明"}
      ]
    }
  ],
  "api_endpoints": [
    {"method": "GET", "path": "/api/resource/", "description": "列表"}
  ],
  "frontend_components": ["ComponentA", "ComponentB"],
  "test_cases": {
    "unit": ["测试用例 1"],
    "e2e": ["E2E 测试 1"]
  },
  "acceptance_criteria": ["验收标准 1"]
}
```

---

## 解析规则

### 数据模型识别
- 查找 `## 数据模型` 章节
- 解析 Markdown 表格提取字段定义
- 识别实体关系（一对多、多对多）

### API 端点识别
- 查找 `### API 端点` 或 `### 端点列表`
- 解析 `METHOD /path/` 格式
- 提取请求/响应示例

### 前端组件识别
- 查找 `### 前端设计` 章节
- 解析组件列表
- 识别交互流程

### 测试用例识别
- 查找 `### 测试用例` 章节
- 分离单元测试和 E2E 测试

---

## 验证规则

| 规则 | 说明 |
|------|------|
| 必须包含功能名称 | 否则无法继续 |
| 必须包含至少一个用户故事 | 否则需求不明确 |
| 必须包含数据模型或 API 端点 | 否则无法生成代码 |

---

## 错误处理

| 错误 | 处理 |
|------|------|
| Spec 文件不存在 | 报错并请求正确路径 |
| 格式不符合模板 | 提示用户修正 |
| 缺少必填字段 | 列出缺失项 |

---

## 使用示例

```bash
# 解析 Spec 文件
/drf-dev parse specs/user-auth.md

# 验证 Spec
/drf-dev validate specs/user-auth.md

# 从 Spec 生成任务
/drf-dev plan specs/user-auth.md
```
