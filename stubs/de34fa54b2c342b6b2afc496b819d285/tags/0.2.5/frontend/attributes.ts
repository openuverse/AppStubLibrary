/**
 * Attributes Store
 *
 * Generated at: 2026-02-26 06:30:23
 * SDK Version: 0.12.8
 * App Name: uvapp_srv_daemonworker
 * App Version: 0.2.5
 * Author: RIGOL Technology
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface PlatformConfig {
  platform_name: string
  version: string
  language: string
  theme: string
  mode: string
  restapi_port: number
  mcp_port: number
  auth_status: string
  internal_status: string
}

export interface DaemonWorkerAttributes {
  worker_name: string
  worker_id: string
  platform_config: PlatformConfig
  worker_configs: any
}

/**
 * Create or get DaemonWorkerAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useDaemonWorker = (appId?: string, initialState?: DaemonWorkerAttributes) => {
  const store = storeManager.register<DaemonWorkerAttributes>(
    'DaemonWorkerAttributes',
    initialState || {
      worker_name: 'uv_srv_daemonworker',
      worker_id: 'de34fa54b2c342b6b2afc496b819d285',
      platform_config: undefined,
      worker_configs: undefined,
    },
    {}
  )

  appId = appId || 'de34fa54b2c342b6b2afc496b819d285'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
