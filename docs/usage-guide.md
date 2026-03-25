# 使用指南

## 详细使用流程

### 场景 1: 创建新功能

#### 步骤 1: 编写 Spec

```bash
cp templates/specs/feature-spec-template.md specs/user-auth.md
```

编辑 `specs/user-auth.md`：

```markdown
## 1. 功能概述
- 功能名称：用户认证
- 用户故事：作为用户，我希望登录系统，以便访问个人数据

## 2. 数据模型
### Model: User
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | CharField | 是 | 用户名 |
| email | EmailField | 是 | 邮箱 |
| password | CharField | 是 | 密码 |

## 3. API 设计
- POST /api/token/ - 获取 token
- DELETE /api/token/ - 注销
- GET /api/users/me/ - 获取当前用户

## 4. 前端设计
- LoginForm 组件
- UserProfile 组件
```

#### 步骤 2: 运行 Agent

```bash
/drf-dev create feature specs/user-auth.md
```

#### 步骤 3: 验收代码

检查生成的文件：
- `backend/apps/user_auth/` - 后端应用
- `frontend/src/components/auth/` - 前端组件

### 场景 2: 记录经验

#### 记录架构决策

```bash
python3 scripts/record-decision.py "数据库选型" \
  -b "需要支持事务和外键" \
  -d "使用 MySQL 8.0" \
  -r "团队熟悉，性能满足需求" \
  -o MySQL PostgreSQL SQLite \
  -a "张三"
```

#### 记录错误模式

```bash
python3 scripts/record-error.py "CORS 配置错误" \
  -e "Access-Control-Allow-Origin header missing" \
  -s "前端调用后端 API 时" \
  -c "CORS_ALLOWED_ORIGINS 未配置前端地址" \
  -S "添加前端地址到 CORS_ALLOWED_ORIGINS" \
  -p "在新项目中检查 CORS 配置" \
  -f "backend/config/settings/base.py"
```

### 场景 3: 检索知识

#### 搜索相关经验

```bash
# 搜索 JWT 相关决策
python3 scripts/search-knowledge.py "JWT"

# 搜索认证相关最佳实践
python3 scripts/search-knowledge.py "authentication" \
  --paths knowledge/best-practices/

# 限制结果数量
python3 scripts/search-knowledge.py "validation" --limit 10
```

## 最佳实践

### 1. Spec 编写

- ✅ 明确用户故事和业务目标
- ✅ 详细定义数据模型和字段
- ✅ 列出所有 API 端点
- ✅ 描述前端组件和交互流程
- ❌ 避免模糊的需求描述

### 2. 代码审查

- 检查生成的测试覆盖率
- 验证 API 端点符合设计
- 确认前端组件可正常工作
- 运行 E2E 测试验证流程

### 3. 经验沉淀

- 每次架构决策后记录 ADR
- 每个错误修复后更新错误库
- 完成功能后总结最佳实践
- 定期回顾和更新知识库

## 常见问题

### Q: 如何修改生成的代码？

A: 直接编辑生成的文件，然后运行测试验证。重要修改建议记录到知识库。

### Q: 如何处理 Spec 变更？

A: 更新 Spec 文件，然后重新运行 Agent。Agent 会对比现有代码并生成差异。

### Q: 知识库如何团队共享？

A: 知识库是 Markdown 文件，通过 Git 版本控制。团队成员可以：
- Pull 最新知识
- 添加新条目
- 提交 PR 审核

## 故障排查

### 测试失败

1. 检查依赖是否安装：`pip install -r requirements/dev.txt`
2. 检查数据库配置：确认 MySQL 运行
3. 查看详细错误：`pytest -v --tb=long`

### 代码生成错误

1. 检查 Spec 格式是否正确
2. 查看 Agent 日志输出
3. 检索知识库是否有类似错误

### 前端构建失败

1. 检查 Node.js 版本：`node --version` (需要 18+)
2. 安装依赖：`npm install`
3. 查看详细错误：`npm run build`
