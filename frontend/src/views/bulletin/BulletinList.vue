<template>
  <div class="bulletin-list">
    <!-- Header -->
    <div class="header">
      <h1 class="title">公告列表</h1>
      <button class="create-btn" @click="goToCreate">
        + 发布公告
      </button>
    </div>
    
    <!-- Filters -->
    <div class="filters">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="搜索公告..."
        class="search-input"
        @input="handleSearch"
      />
      <select v-model="statusFilter" class="status-select" @change="handleFilter">
        <option value="">全部状态</option>
        <option value="DRAFT">草稿</option>
        <option value="PUBLISHED">已发布</option>
        <option value="ARCHIVED">已归档</option>
      </select>
    </div>
    
    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>加载中...</p>
    </div>
    
    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      <p class="error-text">{{ error }}</p>
      <button class="retry-btn" @click="refresh">重试</button>
    </div>
    
    <!-- Empty State -->
    <div v-else-if="bulletins.length === 0" class="empty-state">
      <div class="empty-icon">📋</div>
      <p class="empty-text">暂无公告</p>
      <button class="create-first-btn" @click="goToCreate">发布第一个公告</button>
    </div>
    
    <!-- Bulletin List -->
    <div v-else class="bulletin-grid">
      <BulletinCard
        v-for="bulletin in bulletins"
        :key="bulletin.id"
        :bulletin="bulletin"
        @view="goToDetail"
        @edit="goToEdit"
        @delete="handleDelete"
        @publish="handlePublish"
      />
    </div>
    
    <!-- Pagination -->
    <div v-if="totalCount > pageSize" class="pagination">
      <button :disabled="currentPage <= 1" @click="prevPage">上一页</button>
      <span class="page-info">第 {{ currentPage }} 页 / 共 {{ Math.ceil(totalCount / pageSize) }} 页</span>
      <button :disabled="currentPage * pageSize >= totalCount" @click="nextPage">下一页</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useBulletinStore } from '../stores/bulletin'
import BulletinCard from '../components/bulletin/BulletinCard.vue'
import type { BulletinStatus } from '../types/bulletin'

const router = useRouter()
const store = useBulletinStore()

const searchQuery = ref('')
const statusFilter = ref<BulletinStatus | ''>('')
const pageSize = 20

const bulletins = computed(() => store.bulletins)
const loading = computed(() => store.loading)
const error = computed(() => store.error)
const totalCount = computed(() => store.totalCount)
const currentPage = computed(() => store.currentPage)

onMounted(() => {
  store.fetchBulletins({ page: 1, page_size: pageSize })
})

const handleSearch = () => {
  store.fetchBulletins({
    page: 1,
    page_size: pageSize,
    search: searchQuery.value || undefined,
    status: statusFilter.value || undefined
  })
}

const handleFilter = () => {
  store.fetchBulletins({
    page: 1,
    page_size: pageSize,
    status: statusFilter.value || undefined,
    search: searchQuery.value || undefined
  })
}

const refresh = () => {
  store.fetchBulletins({ page: 1, page_size: pageSize })
}

const goToCreate = () => {
  router.push('/bulletins/new')
}

const goToDetail = (id: number) => {
  router.push(`/bulletins/${id}`)
}

const goToEdit = (id: number) => {
  router.push(`/bulletins/${id}/edit`)
}

const handleDelete = async (id: number) => {
  if (confirm('确定要删除这个公告吗？')) {
    await store.deleteBulletin(id)
  }
}

const handlePublish = async (id: number) => {
  if (confirm('确定要发布这个公告吗？')) {
    await store.publishBulletin(id)
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    store.fetchBulletins({ page: currentPage.value - 1, page_size: pageSize })
  }
}

const nextPage = () => {
  store.fetchBulletins({ page: currentPage.value + 1, page_size: pageSize })
}
</script>

<style scoped>
.bulletin-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.title {
  font-size: 24px;
  font-weight: 700;
  color: #1C2833;
}

.create-btn {
  background: #3498DB;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: background 0.3s;
}

.create-btn:hover {
  background: #2980B9;
}

.filters {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.search-input,
.status-select {
  padding: 10px 16px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.search-input {
  flex: 1;
}

.status-select {
  min-width: 150px;
}

.loading-state,
.error-state,
.empty-state {
  text-align: center;
  padding: 60px 20px;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498DB;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-text {
  color: #E74C3C;
  margin-bottom: 16px;
}

.retry-btn,
.create-first-btn {
  background: #3498DB;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
}

.empty-icon {
  font-size: 64px;
  margin-bottom: 16px;
}

.empty-text {
  color: #666;
  margin-bottom: 24px;
}

.bulletin-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  margin-top: 32px;
}

.pagination button {
  background: #3498DB;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
}

.pagination button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.page-info {
  color: #666;
  font-size: 14px;
}
</style>
