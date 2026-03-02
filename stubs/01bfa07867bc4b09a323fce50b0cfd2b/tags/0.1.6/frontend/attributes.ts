/**
 * Attributes Store
 *
 * Generated at: 2026-03-02 09:17:14
 * SDK Version: 0.12.12
 * App Name: uvapp_srv_sequenceworker
 * App Version: 0.1.6
 * Author: RIGOL Technology
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface WorkflowAttributes {
  value: string
}

/**
 * Create or get WorkflowAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useWorkflow = (appId?: string, initialState?: WorkflowAttributes) => {
  const store = storeManager.register<WorkflowAttributes>(
    'WorkflowAttributes',
    initialState || {
      value: '',
    },
    {}
  )

  appId = appId || '01bfa07867bc4b09a323fce50b0cfd2b'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
