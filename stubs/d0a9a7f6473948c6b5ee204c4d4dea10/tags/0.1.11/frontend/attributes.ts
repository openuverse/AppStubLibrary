/**
 * Attributes Store
 *
 * Generated at: 2026-03-02 08:57:04
 * SDK Version: 0.12.12
 * App Name: Atlas
 * App Version: 0.1.11
 * Author: RIGOL Technology
 * Description: Professional test and measurement instrument management software with automatic discovery, unified management, and real-time monitoring capabilities
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface CurrentInsTreeAttributes {
  ins_tree: string
  dynamic_data: string
}

/**
 * Create or get CurrentInsTreeAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useCurrentInsTree = (appId?: string, initialState?: CurrentInsTreeAttributes) => {
  const store = storeManager.register<CurrentInsTreeAttributes>(
    'CurrentInsTreeAttributes',
    initialState || {
      ins_tree: '',
      dynamic_data: '',
    },
    {}
  )

  appId = appId || 'd0a9a7f6473948c6b5ee204c4d4dea10'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}

export interface CurrentNoticeAttributes {
  message: string
}

/**
 * Create or get CurrentNoticeAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useCurrentNotice = (appId?: string, initialState?: CurrentNoticeAttributes) => {
  const store = storeManager.register<CurrentNoticeAttributes>(
    'CurrentNoticeAttributes',
    initialState || {
      message: '',
    },
    {}
  )

  appId = appId || 'd0a9a7f6473948c6b5ee204c4d4dea10'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
