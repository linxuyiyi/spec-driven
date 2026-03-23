<template>
  <div class="bulletin-card" :class="priorityClass">
    <div class="card-header">
      <h3 class="card-title">{{ bulletin.title }}</h3>
      <div class="badges">
        <BulletinStatusBadge :status="bulletin.status" />
        <BulletinPriorityBadge :priority="bulletin.priority" />
      </div>
    </div>
    
    <div class="card-content">
      <p class="content-preview">{{ contentPreview }}</p>
    </div>
    
    <div class="card-footer">
      <div class="meta">
        <span class="author" v-if="bulletin.author">By {{ bulletin.author }}</span>
        <span class="date">{{ formattedDate }}</span>
      </div>
      
      <div class="actions">
        <button class="action-btn view" @click="$emit('view', bulletin.id)">
          查看
        </button>
        <button 
          v-if="canEdit" 
          class="action-btn edit" 
          @click="$emit('edit', bulletin.id)"
        >
          编辑
        </button>
        <button 
          v-if="canPublish" 
          class="action-btn publish" 
          @click="$emit('publish', bulletin.id)"
        >
          发布
        </button>
        <button 
          v-if="canDelete" 
          class="action-btn delete" 
          @click="$emit('delete', bulletin.id)"
        >
          删除
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { Bulletin } from '../../types/bulletin'
import BulletinStatusBadge from './BulletinStatusBadge.vue'
import BulletinPriorityBadge from './BulletinPriorityBadge.vue'

interface Props {
  bulletin: Bulletin
  canEdit?: boolean
  canPublish?: boolean
  canDelete?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  canEdit: false,
  canPublish: false,
  canDelete: false
})

defineEmits<{
  view: [id: number]
  edit: [id: number]
  delete: [id: number]
  publish: [id: number]
}>()

const contentPreview = computed(() => {
  const content = props.bulletin.content
  return content.length > 100 ? content.substring(0, 100) + '...' : content
})

const formattedDate = computed(() => {
  const date = new Date(props.bulletin.published_at || props.bulletin.created_at)
  return date.toLocaleDateString('zh-CN')
})

const priorityClass = computed(() => {
  const map: Record<string, string> = {
    'URGENT': 'priority-urgent',
    'HIGH': 'priority-high',
    'NORMAL': 'priority-normal',
    'LOW': 'priority-low'
  }
  return map[props.bulletin.priority] || ''
})
</script>

<style scoped>
.bulletin-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.bulletin-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.bulletin-card.priority-urgent {
  border-left: 4px solid #E74C3C;
  background: #FEF5F5;
}

.bulletin-card.priority-high {
  border-left: 4px solid #F39C12;
  background: #FFFBF5;
}

.bulletin-card.priority-normal {
  border-left: 4px solid #3498DB;
}

.bulletin-card.priority-low {
  border-left: 4px solid #95A5A6;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #1C2833;
  margin: 0;
  flex: 1;
}

.badges {
  display: flex;
  gap: 8px;
}

.card-content {
  margin-bottom: 16px;
}

.content-preview {
  color: #666;
  font-size: 14px;
  line-height: 1.6;
  margin: 0;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #eee;
}

.meta {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 12px;
  color: #999;
}

.actions {
  display: flex;
  gap: 8px;
}

.action-btn {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  transition: background 0.3s;
}

.action-btn.view {
  background: #3498DB;
  color: white;
}

.action-btn.view:hover {
  background: #2980B9;
}

.action-btn.edit {
  background: #F39C12;
  color: white;
}

.action-btn.publish {
  background: #27AE60;
  color: white;
}

.action-btn.delete {
  background: #E74C3C;
  color: white;
}
</style>
