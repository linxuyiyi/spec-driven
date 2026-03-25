<template>
  <div class="task-list">
    <div class="task-header">
      <h2>任务列表</h2>
      <el-button type="primary" @click="showCreateDialog">新建任务</el-button>
    </div>
    
    <div class="task-filters">
      <el-select v-model="filterStatus" placeholder="状态" clearable @change="loadTasks">
        <el-option label="待办" value="pending" />
        <el-option label="已完成" value="completed" />
      </el-select>
      <el-select v-model="filterPriority" placeholder="优先级" clearable @change="loadTasks">
        <el-option label="低" :value="1" />
        <el-option label="中" :value="2" />
        <el-option label="高" :value="3" />
      </el-select>
    </div>
    
    <div class="task-cards">
      <TaskCard
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @edit="showEditDialog"
        @toggle="toggleTaskStatus"
        @delete="deleteTask"
      />
    </div>
    
    <el-dialog v-model="dialogVisible" :title="dialogTitle">
      <TaskForm :task="editingTask" @submit="handleSubmit" @cancel="dialogVisible = false" />
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import TaskCard from './Card.vue'
import TaskForm from './Form.vue'
import apiClient from '@/api/client'

interface Task {
  id: number
  title: string
  description: string
  status: string
  priority: number
  due_date: string | null
}

const tasks = ref<Task[]>([])
const filterStatus = ref<string>('')
const filterPriority = ref<number | null>(null)
const dialogVisible = ref(false)
const editingTask = ref<Task | null>(null)
const dialogTitle = ref('')

const loadTasks = async () => {
  const params: Record<string, string> = {}
  if (filterStatus.value) params.status = filterStatus.value
  if (filterPriority.value) params.priority = String(filterPriority.value)
  
  const { data } = await apiClient.get('/tasks/', { params })
  tasks.value = data.results
}

const showCreateDialog = () => {
  editingTask.value = null
  dialogTitle.value = '新建任务'
  dialogVisible.value = true
}

const showEditDialog = (task: Task) => {
  editingTask.value = { ...task }
  dialogTitle.value = '编辑任务'
  dialogVisible.value = true
}

const handleSubmit = async (taskData: Partial<Task>) => {
  if (editingTask.value?.id) {
    await apiClient.put(`/tasks/${editingTask.value.id}/`, taskData)
  } else {
    await apiClient.post('/tasks/', taskData)
  }
  dialogVisible.value = false
  loadTasks()
}

const toggleTaskStatus = async (task: Task) => {
  const newStatus = task.status === 'pending' ? 'completed' : 'pending'
  await apiClient.patch(`/tasks/${task.id}/`, { status: newStatus })
  loadTasks()
}

const deleteTask = async (id: number) => {
  await apiClient.delete(`/tasks/${id}`)
  loadTasks()
}

onMounted(loadTasks)
</script>

<style scoped>
.task-list {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.task-filters {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.task-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
}
</style>
