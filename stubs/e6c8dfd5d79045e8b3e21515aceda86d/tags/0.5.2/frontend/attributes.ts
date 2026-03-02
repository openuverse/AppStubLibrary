/**
 * Attributes Store
 *
 * Generated at: 2026-03-02 09:15:39
 * SDK Version: 0.12.12
 * App Name: uv_srv_messagebus
 * App Version: 0.5.2
 * Author: RIGOL Technology
 *
 * This file is auto-generated. Do not edit manually.
 */

import { onUnmounted } from 'vue'

import { storeManager, useAttributeMonitor } from '@rigol/uv-api'


export interface MessageBusAttributes {
  worker_id: string
  worker_name: string
  version: string
  bind_ip: string
  connect_port: number
  command_port: number
  data_publish_port: number
  stream_port: number
  zmq_context_io_threads: number
  socket_linger: number
  socket_rcvhwm: number
  socket_sndhwm: number
  heartbeat_interval: number
  worker_timeout: number
  max_missed_heartbeats: number
  max_message_size: number
  platform_workers_connected: number
  platform_workers_active: number
  is_enabled: boolean
  is_running: boolean
  start_time: string
  uptime_seconds: number
  probe_attributes: ProbeAttributes | undefined
}

/**
 * Create or get MessageBusAttributes store
 *
 * @param appId - Application ID
 * @param initialState - Optional initial state
 * @returns Store manager instance
 */
export const useMessageBus = (appId?: string, initialState?: MessageBusAttributes) => {
  const store = storeManager.register<MessageBusAttributes>(
    'MessageBusAttributes',
    initialState || {
      worker_id: '0x0001',
      worker_name: 'UltraView MessageBus',
      version: '0.0.1',
      bind_ip: '0.0.0.0',
      connect_port: 14000,
      command_port: 14001,
      data_publish_port: 14002,
      stream_port: 14003,
      zmq_context_io_threads: 16,
      socket_linger: 1000,
      socket_rcvhwm: 100000,
      socket_sndhwm: 100000,
      heartbeat_interval: 3,
      worker_timeout: 15,
      max_missed_heartbeats: 1,
      max_message_size: undefined,
      platform_workers_connected: 0,
      platform_workers_active: 0,
      is_enabled: true,
      is_running: false,
      start_time: '',
      uptime_seconds: 0,
      probe_attributes: undefined,
    },
    {}
  )

  appId = appId || 'e6c8dfd5d79045e8b3e21515aceda86d'
  const monitor = useAttributeMonitor({
    appId: appId,
    store: store,
  })

  onUnmounted(() => {
    monitor.close()
  })

  return { store, monitor }
}
