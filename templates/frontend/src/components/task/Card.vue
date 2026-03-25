<template>
  <el-card class="task-card" :class="task.status">
    <div class="task-header">
      <h3>{{ task.title }}</h3>
      <el-tag :type="priorityType">{{ priorityLabel }}</el-tag>
    </div>
    <p class="task-description" v-if="task.description">{{ task.description }}</p>
    <div class="task-footer">
      <el-tag :type="task.status === 'completed' ? 'success' : 'warning'">
        {{ task.status === 'completed' ? '已完成' : '待办' }}
      </el-tag>
      <span class="task-due" v-if="task.due_date">{{ formatDate(task.due_date) }}</span>
    </div>
    <div class="task-actions">
      <el-button size="small" @click="$emit('toggle', task)">
        {{ task.status === 'completed' ? '撤销' : '完成' }}
      </el-button>
      <el-button size="small" @click="$emit('edit', task)">编辑</el-button>
      <el-button size="small" type="danger" @click="$emit('delete', task.id)">删除</el-button>
    </div>
  </el-card>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Task {
  id: number
  title: string
  description: string
  status: string
  priority: number
  due_date: string | null
}

const props = defineProps<{ task: Task }>()
const emit = defineEmits<{
  edit: [task: Task]
  toggle: [task: Task]
  delete: [id: number]
}>()

const priorityLabel = computed(() => {
  const labels: Record<number, string> = { 1: '低', 2: '中', 3: '高' }
  return labels[props.task.priority] || '未知'
})

const priorityType = computed(() => {
  const types: Record<number, string> = { 1: 'info', 2: 'warning', 3: 'danger' }
  return types[props.task.priority] || 'info'
})

const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString('zh-CN')
}
</script>

<style scoped>
.task-card {
  transition: all 0.3s;
}

.task-card.completed {
  opacity: 0.7;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.task-header h3 {
  margin: 0;
  font-size: 1.1rem;
}

.task-description {
  color: #666;
  font-size: 0.9rem;
  margin: 10px 0;
}

.task-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
}

.task-due {
  font-size: 0.8rem;
  color: #999;
}

.task-actions {
  display: flex;
  gap: 8px;
  margin-top: 10px;
}
</style>
