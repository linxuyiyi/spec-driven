/** 公告 Store */

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Bulletin, BulletinFilters, BulletinStatus } from '../types/bulletin'
import * as bulletinApi from '../api/bulletin'

export const useBulletinStore = defineStore('bulletin', () => {
  // State
  const bulletins = ref<Bulletin[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const totalCount = ref(0)
  const currentPage = ref(1)
  
  // Getters
  const publishedBulletins = computed(() => 
    bulletins.value.filter(b => b.status === 'PUBLISHED')
  )
  
  const draftBulletins = computed(() => 
    bulletins.value.filter(b => b.status === 'DRAFT')
  )
  
  const urgentBulletins = computed(() => 
    bulletins.value.filter(b => b.priority === 'URGENT' || b.priority === 'HIGH')
  )
  
  // Actions
  async function fetchBulletins(filters?: BulletinFilters) {
    loading.value = true
    error.value = null
    
    try {
      const response = await bulletinApi.getBulletins(filters)
      bulletins.value = response.results
      totalCount.value = response.count
      currentPage.value = filters?.page || 1
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取公告列表失败'
    } finally {
      loading.value = false
    }
  }
  
  async function fetchBulletin(id: number) {
    loading.value = true
    error.value = null
    
    try {
      const bulletin = await bulletinApi.getBulletin(id)
      const index = bulletins.value.findIndex(b => b.id === id)
      if (index >= 0) {
        bulletins.value[index] = bulletin
      } else {
        bulletins.value.push(bulletin)
      }
      return bulletin
    } catch (e) {
      error.value = e instanceof Error ? e.message : '获取公告详情失败'
      throw e
    } finally {
      loading.value = false
    }
  }
  
  async function createBulletin(data: { title: string; content: string; priority?: string }) {
    error.value = null
    
    try {
      const bulletin = await bulletinApi.createBulletin({
        ...data,
        status: 'DRAFT'
      })
      bulletins.value.unshift(bulletin)
      totalCount.value++
      return bulletin
    } catch (e) {
      error.value = e instanceof Error ? e.message : '创建公告失败'
      throw e
    }
  }
  
  async function updateBulletin(id: number, data: { title?: string; content?: string; status?: string; priority?: string }) {
    error.value = null
    
    try {
      const bulletin = await bulletinApi.updateBulletin(id, data)
      const index = bulletins.value.findIndex(b => b.id === id)
      if (index >= 0) {
        bulletins.value[index] = bulletin
      }
      return bulletin
    } catch (e) {
      error.value = e instanceof Error ? e.message : '更新公告失败'
      throw e
    }
  }
  
  async function deleteBulletin(id: number) {
    error.value = null
    
    try {
      await bulletinApi.deleteBulletin(id)
      const index = bulletins.value.findIndex(b => b.id === id)
      if (index >= 0) {
        bulletins.value.splice(index, 1)
        totalCount.value--
      }
    } catch (e) {
      error.value = e instanceof Error ? e.message : '删除公告失败'
      throw e
    }
  }
  
  async function publishBulletin(id: number) {
    error.value = null
    
    try {
      const bulletin = await bulletinApi.publishBulletin(id)
      const index = bulletins.value.findIndex(b => b.id === id)
      if (index >= 0) {
        bulletins.value[index] = bulletin
      }
      return bulletin
    } catch (e) {
      error.value = e instanceof Error ? e.message : '发布公告失败'
      throw e
    }
  }
  
  // Reset store
  function reset() {
    bulletins.value = []
    loading.value = false
    error.value = null
    totalCount.value = 0
    currentPage.value = 1
  }
  
  return {
    // State
    bulletins,
    loading,
    error,
    totalCount,
    currentPage,
    // Getters
    publishedBulletins,
    draftBulletins,
    urgentBulletins,
    // Actions
    fetchBulletins,
    fetchBulletin,
    createBulletin,
    updateBulletin,
    deleteBulletin,
    publishBulletin,
    reset
  }
})
