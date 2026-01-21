/**
 * Attributes Store
 *
 * Generated at: 2026-01-20 10:50:07
 * SDK Version: 0.12.3
 * App Name: AppManager
 * App Version: 0.1.5
 * Author: RIGOL Technology
 * Description: The app manager to browse, install, update, launch, and uninstall applications.
 *
 * This file is auto-generated. Do not edit manually.
 */

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

  useAttributeMonitor({
    appId: appId,
    store: store,
  })
  return store
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

  useAttributeMonitor({
    appId: appId,
    store: store,
  })
  return store
}
