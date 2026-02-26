/**
 * Attributes Store
 *
 * Generated at: 2026-02-26 06:03:49
 * SDK Version: 0.12.8
 * App Name: Nexus
 * App Version: 0.2.0
 * Author: RIGOL Technology
 * Description: Nexus is the app manager to browse, install, update, launch, and uninstall applications.
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface CurrentUserAttributes {
  name: string
  age: number
  email: string
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
    },
    {}
  )

  appId = appId || '14706eda67f34b7ebb4b487a0b6e7f2d'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}

export interface InstallStatusAttributes {
  app_id: string | undefined
  install_status: string | undefined
  timestamp: number | undefined
}

/**
 * Create or get InstallStatusAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useInstallStatus = (appId?: string, initialState?: InstallStatusAttributes) => {
  const store = storeManager.register<InstallStatusAttributes>(
    'InstallStatusAttributes',
    initialState || {
      app_id: undefined,
      install_status: undefined,
      timestamp: undefined,
    },
    {}
  )

  appId = appId || '14706eda67f34b7ebb4b487a0b6e7f2d'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
