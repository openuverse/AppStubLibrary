/**
 * Attributes Store
 *
 * Generated at: 2026-02-26 08:02:43
 * SDK Version: 0.12.9
 * App Name: uvapp_srv_licenseworker
 * App Version: 0.1.1
 * Author: RIGOL Technology
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface UserContactInfo {
  address: string
  phone: string
  country: string
}

export interface CurrentUserAttributes {
  name: string
  age: number
  email: string
  contact: UserContactInfo
  settings: Record<string, any>
  tags: any[]
}

/**
 * Create or get CurrentUserAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useCurrentUser = (appId?: string, initialState?: CurrentUserAttributes) => {
  const store = storeManager.register<CurrentUserAttributes>(
    'CurrentUserAttributes',
    initialState || {
      name: 'John Doe',
      age: 30,
      email: 'john.doe@example.com',
      contact: {
        address: 'Beijing',
        phone: '123-456-7890',
        country: 'China',
      },
      settings: {theme: 'light', language: 'zh'},
      tags: ['vip', 'active'],
    },
    {}
  )

  appId = appId || '48e5a3f7ffa14d5cb5a70485863dff1f'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
