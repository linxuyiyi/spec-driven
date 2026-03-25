export interface User {
  id: number
  username: string
  email: string
  created_at: string
}

export interface ApiResponse<T> {
  count?: number
  next?: string | null
  previous?: string | null
  results: T[]
}

export interface TokenPair {
  access: string
  refresh: string
}
