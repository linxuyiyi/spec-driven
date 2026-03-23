/** 公告类型定义 */

export type BulletinStatus = 'DRAFT' | 'PUBLISHED' | 'ARCHIVED'
export type BulletinPriority = 'LOW' | 'NORMAL' | 'HIGH' | 'URGENT'

export interface Bulletin {
  id: number
  title: string
  content: string
  status: BulletinStatus
  priority: BulletinPriority
  author: string | null
  published_at: string | null
  created_at: string
  updated_at: string
}

export interface BulletinListResponse {
  count: number
  next: string | null
  previous: string | null
  results: Bulletin[]
}

export interface CreateBulletinRequest {
  title: string
  content: string
  status?: BulletinStatus
  priority?: BulletinPriority
}

export interface UpdateBulletinRequest {
  title?: string
  content?: string
  status?: BulletinStatus
  priority?: BulletinPriority
}

export interface BulletinFilters {
  status?: BulletinStatus
  search?: string
  page?: number
  page_size?: number
}
