# Vue3 组件开发模板

**适用场景**: 创建新的 Vue3 Component + Store + API

---

## Task: [Component Name] Component

**Spec**: `.specify/specs/<feature>.md`  
**Assigned To**: Frontend Agent  
**Priority**: High

---

## Deliverables

### 1. TypeScript Types First
- [ ] Create/Edit `frontend/src/types/<domain>.ts`
- [ ] Define interface:
  ```typescript
  export interface <ModelName> {
    id: number
    // Add all fields with proper types
  }
  
  export interface <ModelName>Response {
    results: <ModelName>[]
    count: number
  }
  ```

### 2. API Client
- [ ] Create `frontend/src/api/<domain>.ts`
- [ ] Define BASE_URL
- [ ] Implement CRUD methods:
  ```typescript
  export async function get<List>(params?: Params): Promise<Response>
  export async function getDetail(id: number): Promise<Item>
  export async function create(data: CreateDto): Promise<Item>
  export async function update(id: number, data: UpdateDto): Promise<Item>
  export async function remove(id: number): Promise<void>
  ```

### 3. Pinia Store
- [ ] Create `frontend/src/stores/<domain>.ts`
- [ ] Define state:
  ```typescript
  state: () => ({
    items: [] as <ModelName>[],
    loading: false,
    error: null as string | null
  })
  ```
- [ ] Implement actions: fetch, fetchDetail, create, update, remove

### 4. Component Structure
- [ ] Create `frontend/src/components/<domain>/<ComponentName>.vue`
- [ ] Use `<script setup lang="ts">`
- [ ] Define props with interface
- [ ] Define emits with types
- [ ] Implement slots if needed

### 5. View/Page (if applicable)
- [ ] Create `frontend/src/views/<domain>/<ViewName>View.vue`
- [ ] Use the store
- [ ] Handle loading/error/empty states
- [ ] Add responsive layout

---

## Quality Gates

### TypeScript Verification
```bash
# Run type check - MUST PASS
npm run type-check
# Expected: 0 errors
```

### Lint Verification
```bash
# Run ESLint - MUST PASS
npm run lint
# Expected: 0 errors
```

### UI/UX Checklist
- [ ] Responsive (320px, 768px, 1024px, 1440px)
- [ ] WCAG AA contrast (4.5:1 for text, 3:1 for UI)
- [ ] Keyboard navigation
- [ ] Screen reader friendly (aria-labels)
- [ ] Loading state
- [ ] Error state
- [ ] Empty state

### State Management
- [ ] No props drilling (>2 levels)
- [ ] Using Pinia for shared state
- [ ] Composables for reusable logic

---

## PUA Behavior

> 收到需求，**对齐目标**，**拉通资源**，进入 sprint。因为信任所以简单——别让信任你的人失望。

**[PUA 生效 🔥] 标记时机**:
- 主动加了 loading/error/empty 状态 — 没有状态处理的组件就是半成品
- 顺手优化了响应式断点 — 等到用户投诉移动端再改，你就准备写复盘吧

**交付标准**:
> 交付完成。这次的表现，勉强配得上 P8 这个级别。今天最好的表现，是明天最低的要求。

**证据**: lint 输出 + type-check 输出 + Lighthouse 截图

---

## Time Estimate

- Types: 10 min
- API client: 15 min
- Pinia store: 20 min
- Component: 30 min
- View: 25 min
- **Total**: ~2 hours

---

## Progress

- [ ] Types defined
- [ ] API client implemented
- [ ] Pinia store implemented
- [ ] Component created
- [ ] View created (if applicable)
- [ ] TypeScript compiles (0 errors)
- [ ] ESLint passes (0 errors)
- [ ] Responsive tested

---

## Notes

[Design decisions, UI considerations, lessons learned]
