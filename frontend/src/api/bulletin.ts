/** 公告 API 客户端 */

import type {
  Bulletin,
  BulletinListResponse,
  CreateBulletinRequest,
  UpdateBulletinRequest,
  BulletinFilters
} from '../types/bulletin'

const BASE_URL = '/api/bulletins'

/** 处理 API 响应 */
async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: '请求失败' }))
    throw new Error(error.detail || '请求失败')
  }
  return response.json()
}

/** 获取公告列表 */
export async function getBulletins(filters?: BulletinFilters): Promise<BulletinListResponse> {
  const params = new URLSearchParams()
  if (filters) {
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        params.set(key, String(value))
      }
    })
  }
  
  const response = await fetch(`${BASE_URL}/?${params}`)
  return handleResponse<BulletinListResponse>(response)
}

/** 获取公告详情 */
export async function getBulletin(id: number): Promise<Bulletin> {
  const response = await fetch(`${BASE_URL}/${id}/`)
  return handleResponse<Bulletin>(response)
}

/** 创建公告 */
export async function createBulletin(data: CreateBulletinRequest): Promise<Bulletin> {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return handleResponse<Bulletin>(response)
}

/** 更新公告 */
export async function updateBulletin(id: number, data: UpdateBulletinRequest): Promise<Bulletin> {
  const response = await fetch(`${BASE_URL}/${id}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return handleResponse<Bulletin>(response)
}

/** 删除公告 */
export async function deleteBulletin(id: number): Promise<void> {
  const response = await fetch(`${BASE_URL}/${id}/`, {
    method: 'DELETE'
  })
  if (!response.ok) {
    throw new Error('删除失败')
  }
}

/** 发布公告 */
export async function publishBulletin(id: number): Promise<Bulletin> {
  const response = await fetch(`${BASE_URL}/${id}/publish/`, {
    method: 'POST'
  })
  return handleResponse<Bulletin>(response)
}
