<template>
  <span class="priority-badge" :class="priorityClass">
    {{ priorityText }}
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { BulletinPriority } from '../../types/bulletin'

interface Props {
  priority: BulletinPriority
}

const props = defineProps<Props>()

const priorityClass = computed(() => {
  const map: Record<string, string> = {
    'URGENT': 'priority-urgent',
    'HIGH': 'priority-high',
    'NORMAL': 'priority-normal',
    'LOW': 'priority-low'
  }
  return map[props.priority] || ''
})

const priorityText = computed(() => {
  const map: Record<BulletinPriority, string> = {
    'URGENT': '🔥 紧急',
    'HIGH': '⚠️ 高',
    'NORMAL': '📌 普通',
    'LOW': '📝 低'
  }
  return map[props.priority] || props.priority
}
</script>

<style scoped>
.priority-badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.priority-urgent {
  background: #E74C3C;
  color: white;
}

.priority-high {
  background: #F39C12;
  color: white;
}

.priority-normal {
  background: #3498DB;
  color: white;
}

.priority-low {
  background: #95A5A6;
  color: white;
}
</style>
