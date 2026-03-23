<template>
  <span class="status-badge" :class="statusClass">
    {{ statusText }}
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { BulletinStatus } from '../../types/bulletin'

interface Props {
  status: BulletinStatus
}

const props = defineProps<Props>()

const statusClass = computed(() => {
  const map: Record<string, string> = {
    'DRAFT': 'status-draft',
    'PUBLISHED': 'status-published',
    'ARCHIVED': 'status-archived'
  }
  return map[props.status] || ''
})

const statusText = computed(() => {
  const map: Record<BulletinStatus, string> = {
    'DRAFT': '草稿',
    'PUBLISHED': '已发布',
    'ARCHIVED': '已归档'
  }
  return map[props.status] || props.status
}
</script>

<style scoped>
.status-badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.status-draft {
  background: #95A5A6;
  color: white;
}

.status-published {
  background: #27AE60;
  color: white;
}

.status-archived {
  background: #3498DB;
  color: white;
}
</style>
