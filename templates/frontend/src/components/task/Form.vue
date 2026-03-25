<template>
  <el-form :model="form" :rules="rules" ref="formRef" label-width="80px">
    <el-form-item label="标题" prop="title">
      <el-input v-model="form.title" placeholder="请输入任务标题" />
    </el-form-item>
    <el-form-item label="描述" prop="description">
      <el-input
        v-model="form.description"
        type="textarea"
        :rows="4"
        placeholder="任务描述（可选）"
      />
    </el-form-item>
    <el-form-item label="优先级" prop="priority">
      <el-radio-group v-model="form.priority">
        <el-radio :label="1">低</el-radio>
        <el-radio :label="2">中</el-radio>
        <el-radio :label="3">高</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="截止日期" prop="due_date">
      <el-date-picker
        v-model="form.due_date"
        type="datetime"
        placeholder="选择截止日期"
        format="YYYY-MM-DD HH:mm:ss"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submit" :loading="loading">提交</el-button>
      <el-button @click="$emit('cancel')">取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import type { FormRules } from 'element-plus'

interface Task {
  id?: number
  title: string
  description: string
  priority: number
  due_date: string | null
}

const props = defineProps<{ task: Task | null }>()
const emit = defineEmits<{
  submit: [data: Partial<Task>]
  cancel: []
}>()

const formRef = ref()
const loading = ref(false)

const form = reactive<Task>({
  title: '',
  description: '',
  priority: 2,
  due_date: null
})

const rules: FormRules = {
  title: [{ required: true, message: '请输入任务标题', trigger: 'blur' }]
}

const submit = async () => {
  await formRef.value.validate()
  loading.value = true
  try {
    emit('submit', { ...form })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (props.task) {
    form.title = props.task.title
    form.description = props.task.description
    form.priority = props.task.priority
    form.due_date = props.task.due_date
  }
})
</script>
