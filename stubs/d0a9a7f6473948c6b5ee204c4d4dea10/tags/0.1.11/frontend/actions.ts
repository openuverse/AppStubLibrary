/**
 * Actions API Client
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

import { RestAPIClient, type RestAPIConfig, type DeepPartial } from '@rigol/uv-api'


/**
 * 设备能力标记，嵌套于 InstrumentInfoSchema.capabilities。
 * 
 * AI发送SCPI命令前必须检查 supportsSCPI=True，否则该设备不支持SCPI通信。
 */
export interface CapabilitiesSchema {
  supportsSCPI?: boolean
  supportsIVI?: boolean
  supportsDataStreaming?: boolean
  supportsWebUi?: boolean
}

/**
 * 设备分类节点（设备树一级分类），嵌套于 InstrumentTreeSchema.categories。
 * 
 * AI可通过key字段识别分类:
 * - LAN_INSTRUMENT=网络LAN仪器
 * - USB_INSTRUMENT=USB仪器
 * - GPIB_INSTRUMENT=GPIB仪器
 * - SERIAL_INSTRUMENT=串口仪器
 * - PXI_INSTRUMENT=PXI仪器
 * - VIRTUAL_INSTRUMENT=虚拟仪器
 * - UNREGISTERED_INSTRUMENT=未注册仪器（需调用instrument_register_manual注册后方可使用）
 */
export interface CategoryNodeSchema {
  label?: string
  key?: string
  children: InstrumentInfoSchema[]
}

/**
 * 仪器连接测试结果模型。
 * 
 * 关联Action:
 * - instrument_test_connection(devicekey_or_ResourceStr: str) -> ConnectTestResult
 * 
 * AI调用指引:
 * - 参数可传入 device_key（从设备树 InstrumentInfoSchema.key 获取）或 VISA资源字符串（如"TCPIP0::192.168.1.100::inst0::INSTR"）。
 * - 测试前无需独占设备。
 * - 根据返回的 status 判断设备状态: AVAILABLE 才可正常操作。
 */
export interface ConnectTestResult {
  success?: boolean
  error?: string | undefined
  status?: string
}

/**
 * 设备静态属性信息，嵌套于 InstrumentInfoSchema.deviceInfo。
 * 
 * AI可通过 instrumentType 判断设备类别以选择合适的SCPI命令集，通过 interfaceType 判断通信接口。
 */
export interface DeviceInfoSchema {
  name?: string
  model?: string
  manufacturer?: string
  alias?: string | undefined
  type?: string
  instrumentType?: string
  interfaceType?: string
  serialNumber?: string | undefined
  firmwareVersion?: string | undefined
  description?: string | undefined
}

/**
 * 仪器扫描结果模型。
 * 
 * 关联Action:
 * - discovery_start(config: dict) -> InsScanResult: 启动/轮询扫描。
 * - discovery_stop() -> InsScanResult: 停止当前扫描。
 * 
 * AI调用指引:
 * 1. 调用 discovery_start(config={"discoverType":"TCPIP"}) 启动扫描。
 *    discoverType可选值: TCPIP|USB|GPIB|SERIAL|PXI|VIRTUAL|UNKNOWN(扫描全部)。
 * 2. 若返回 is_finished=False，需每隔2-3秒重复调用 discovery_start(config=相同参数) 轮询。
 * 3. 直到 is_finished=True 表示扫描完成。
 * 4. message 字段包含AI流程引导信息，请务必阅读并遵循。
 * 5. 扫描完成后，调用 insTree_full_get() 获取设备树查看发现的仪器。
 * 6. 若需提前终止，调用 discovery_stop()。
 */
export interface InsScanResult {
  device_count?: number
  is_finished?: boolean
  error?: string | undefined
  message?: string | undefined
}

/**
 * 单台设备的完整信息模型（设备树节点）。
 * 
 * 关联Action:
 * - insTree_full_get() -> InstrumentTreeSchema: 返回的设备树中每个设备即此类型。
 * - instrument_create_manual(visaResourceString) -> Optional[InstrumentInfoSchema]: 创建新设备后返回此类型。
 * - instrument_register_manual(instrument_info: InstrumentInfoSchema) -> bool: 注册设备时传入此类型。
 * 
 * AI调用指引:
 * - key字段是所有设备操作的核心标识符。scpi_execute、session_request_device、instrument_test_connection、
 *   instrument_unregister等action的device_key参数均使用此值。
 * - 操作设备前应检查 status.connection==AVAILABLE 且 capabilities.supportsSCPI==True。
 * - 支持无限层级嵌套（children），机箱类设备可包含子模块设备。
 */
export interface InstrumentInfoSchema {
  label?: string
  key?: string
  visaResourceString?: string
  status?: StatusSchema
  deviceInfo?: DeviceInfoSchema
  capabilities?: CapabilitiesSchema
  scpiCapabilities?: ScpiCapabilitiesSchema
  selfCapabilities: Record<string, any>
  dynamicData: Record<string, any>
  resourceProfiles: ResourceProfileSchema[]
  children: any[]
}

/**
 * 完整的设备树结构（顶层模型）。
 * 
 * 关联Action:
 * - insTree_full_get() -> InstrumentTreeSchema: 获取完整设备树，无需参数。
 * 
 * AI调用指引（典型工作流）:
 * 1. 调用 discovery_start(config={"discoverType":"TCPIP"}) 扫描发现设备。
 * 2. 扫描完成后调用 insTree_full_get() 获取完整设备树。
 * 3. 遍历 categories[i].children 找到目标设备，获取其 key。
 * 4. 使用 key 调用 scpi_execute/session_request_device 等action操作设备。
 */
export interface InstrumentTreeSchema {
  timestamp?: string
  syncId?: number
  messageType?: string
  categories: CategoryNodeSchema[]
}

/**
 * 设备关联资源配置，嵌套于 InstrumentInfoSchema.resourceProfiles。
 * 
 * AI可通过type字段筛选资源:
 * - SCPI_COMMAND_SET类型的uri可传入 scpi_resources_get(resource_id) 获取完整命令集。
 * - ICON_SET类型的uri可传入 icon_resources_get(resource_id) 获取图标资源。
 */
export interface ResourceProfileSchema {
  uri?: string
  version?: string
  type?: string
  other?: string | undefined
}

/**
 * SCPI批量命令序列执行结果模型。
 * 
 * 关联Action:
 * - scpi_batch_execute(device_key: str, commands: List[str]) -> ScpiBatchExecuteResult
 * 
 * AI调用指引:
 * - 向同一设备按顺序发送多条SCPI命令。commands 按数组顺序依次执行。
 * - 示例: commands=["*RST", "*IDN?", ":MEAS:VOLT:DC?"]
 * - results 列表中每个元素对应 commands 中同索引位置的命令结果。
 * - 适用于需要按顺序执行多步操作的场景（如先复位再测量）。
 */
export interface ScpiBatchExecuteResult {
  success?: boolean
  results: ScpiExecuteResult[]
  error?: string | undefined
}

/**
 * 设备SCPI能力集合，嵌套于 InstrumentInfoSchema.scpiCapabilities。
 * 
 * AI操作SCPI前可先查阅commands列表了解该设备支持哪些命令，参考historyLog了解操作上下文。
 */
export interface ScpiCapabilitiesSchema {
  commands: ScpiCommandSchema[]
  historyLog: ScpilogHistorySchema[]
  defCRCFormat?: string
}

/**
 * SCPI命令定义条目，嵌套于 ScpiCapabilitiesSchema.commands。
 * 
 * AI可遍历此列表查找设备支持的SCPI命令，根据description理解命令用途，
 * 根据ranges确定参数范围，根据returnType解析返回数据。
 */
export interface ScpiCommandSchema {
  command?: string
  description?: string
  units?: string
  ranges?: string
  returnType?: string
}

/**
 * 单条SCPI命令执行结果模型。
 * 
 * 关联Action:
 * - scpi_execute(device_key: str, command: str) -> ScpiExecuteResult
 * 
 * AI调用指引:
 * - device_key: 从设备树 InstrumentInfoSchema.key 获取，是设备的唯一标识。
 * - command: 标准SCPI命令字符串，如 "*IDN?"(查询设备标识)、"*RST"(复位设备)、":MEASure:VOLTage:DC?"(测量直流电压)。
 * - 查询命令（以?结尾）的结果在 response 字段返回；设置命令通常无响应。
 * - 建议先调用 session_request_device(device_key) 独占设备，完成后调用 session_release_device(device_key) 释放。
 */
export interface ScpiExecuteResult {
  success?: boolean
  command?: string
  response?: string | undefined
  error?: string | undefined
}

/**
 * SCPI命令执行历史日志，嵌套于 ScpiCapabilitiesSchema.historyLog。
 * 
 * AI可参考历史记录了解设备之前执行过的命令和响应结果。
 */
export interface ScpilogHistorySchema {
  id?: number
  text?: string
  sendresult?: string | undefined
  readresult?: string | undefined
  timestamp?: string | undefined
}

/**
 * 多设备统一SCPI命令执行结果模型。
 * 
 * 关联Action:
 * - scpi_multiIns_execute(device_list: List[str], command: str) -> ScpimultiInsExecuteResult
 * 
 * AI调用指引:
 * - 向多台设备同时发送同一条SCPI命令。
 * - device_list: 设备key列表，从设备树各 InstrumentInfoSchema.key 获取。示例: ["LAN_0001","LAN_0002"]
 * - command: 单条SCPI命令字符串，同时发送给所有目标设备。
 * - results 字典以 device_key 为键，可按设备逐一检查执行结果。
 */
export interface ScpimultiInsExecuteResult {
  success?: boolean
  results: Record<string, ScpiExecuteResult>
  error?: string | undefined
}

/**
 * 设备实时运行状态，嵌套于 InstrumentInfoSchema.status。
 * 
 * AI可根据 connection 字段判断设备是否可操作:
 * - 仅 AVAILABLE 状态的设备可正常发送SCPI命令。
 * - LOCKED 状态需等待释放或由当前会话持有锁。
 * - UNREGISTERED 需先调用 instrument_register_manual 注册。
 * - OFFLINE/FAULT 不可通信，建议先调用 instrument_test_connection 测试。
 */
export interface StatusSchema {
  connection?: string
  health?: string
  discoverSource?: string | undefined
  registeredAt?: string | undefined
  lastUpdated?: string | undefined
  isLocked?: boolean
}

/**
 * 应用全局设置参数模型。
 * 
 * 关联Action:
 * - Setting_parameter_get() -> Optional[setting_model]: 获取当前设置，无需参数。
 * - Setting_parameter_update(config: setting_model) -> setting_model: 更新设置并返回更新后的完整配置。
 * 
 * AI调用指引:
 * 1. 先调用 Setting_parameter_get() 获取当前配置。
 * 2. 修改需要变更的字段后，调用 Setting_parameter_update(config=修改后的对象) 提交更新。
 */
export interface setting_model {
  is_show_guidelines: boolean
  is_multi_network_scan: boolean
  scan_network_mask: string
  scan_ip_ranges: string[]
  scan_timeout: number
  is_scan_send_scpi_command: boolean
  lan_connect_test_interval: number
  scpi_command_end_setting?: string | undefined
}

/**
 * API Client
 *
 * Auto-generated from backend actions
 */
export class Client extends RestAPIClient {
  /**
   * Default Worker ID
   * @remarks This ID is generated by the backend and used to identify the current Worker instance
   */
  static readonly DEFAULT_WORKER_ID = 'd0a9a7f6473948c6b5ee204c4d4dea10'

  /**
   * Create an API client instance
   * @param config - REST API configuration object
   * @param config.workerId - Worker ID, defaults to auto-generated ID
   * @param config.baseURL - API base URL
   * @param config.timeout - Request timeout in milliseconds
   * @param config.apiVersion - API version number
   * @param config.headers - Custom request headers
   * @param config.urlType - URL type, either 'path' or 'header'
   *
   * @example
   * ```typescript
   * // Using default configuration
   * const client = new Client()
   *
   * // Using custom configuration
   * const client = new Client({
   *   baseURL: 'http://localhost:9898',
   *   timeout: 10000,
   *   workerId: 'custom-worker-id'
   * })
   * ```
   */
  constructor(config?: RestAPIConfig) {
    const defaultConfig: RestAPIConfig = {
      workerId: Client.DEFAULT_WORKER_ID,
    }
    super({ ...defaultConfig, ...(config || {}) })
  }

  /**
   * get app info
   */
  async get_app_config() {
    return await this.action<any>('get_app_config')
  }

  /**
   * get app action details
   */
  async get_all_action_details() {
    return await this.action<any>('get_all_action_details')
  }

  /**
   * get all attribute groups
   */
  async get_all_attribute_groups() {
    return await this.action<any>('get_all_attribute_groups')
  }

  /**
   * trigger once attributes snapshot push for a group
   */
  async trig_attributes_snapshot(group_name: string) {
    return await this.action<boolean>('trig_attributes_snapshot', { group_name })
  }

  /**
   * get attribute value by path
   */
  async get_attribute(attribute_path: string) {
    return await this.action<any>('get_attribute', { attribute_path })
  }

  /**
   * set attribute value by path
   */
  async set_attribute(attribute_path: string, value: any) {
    return await this.action<boolean>('set_attribute', { attribute_path, value })
  }

  /**
   * shutdown app
   */
  async shutdown_app(reason: string) {
    return await this.action<any>('shutdown_app', { reason })
  }

  /**
   * 触发完整设备树同步推送（前端专用，AI通常无需调用）。无参数，无返回值。调用后系统通过WebSocket向前端推送最新设备树数据。AI如需获取设备树数据，请改用insTree_full_get。
   */
  async insTree_full_sync() {
    return await this.action<null>('insTree_full_sync')
  }

  /**
   * 获取完整设备树（这是获取设备信息的核心入口）。无参数。返回InstrumentTreeSchema，其中categories列表包含所有分类节点（LAN_INSTRUMENT/USB_INSTRUMENT/GPIB_INSTRUMENT/SERIAL_INSTRUMENT/PXI_INSTRUMENT/VIRTUAL_INSTRUMENT/UNREGISTERED_INSTRUMENT），每个分类的children列表包含该分类下所有设备的InstrumentInfoSchema。【关键】后续所有设备操作（scpi_execute/session_request_device/instrument_test_connection等）的device_key参数，均需从本接口返回的设备树中某个设备的key字段获取。同理，visaResourceString也从设备的visaResourceString字段获取。【典型流程】1.调用本接口获取设备树 → 2.遍历categories[i].children找到目标设备 → 3.取设备的key调用后续action。
   */
  async insTree_full_get() {
    return await this.action<InstrumentTreeSchema>('insTree_full_get')
  }

  /**
   * 手动创建仪器（仅在设备树中不存在该设备时使用，若设备已在未注册分类中，应使用instrument_register_manual注册）。参数visaResourceString(str): 设备的VISA资源字符串。获取方式: 可从insTree_full_get返回的设备树中某设备的visaResourceString字段获取，或由用户手动提供。格式示例: LAN设备"TCPIP0::192.168.1.100::inst0::INSTR"，USB设备"USB0::0x1AB1::0x04CE::DS1ZA123456789::INSTR"。返回InstrumentInfoSchema(创建成功，含key/状态/能力等完整信息)或None(创建失败)。创建后设备自动添加到设备树。
   */
  async instrument_create_manual(visaResourceString: string) {
    return await this.action<InstrumentInfoSchema | undefined>('instrument_create_manual', { visaResourceString }, {
      headers: { 'X-UV-Action-Timeout': '20000' },
    })
  }

  /**
   * 手动注册仪器（将设备树中未注册分类下的设备注册到系统）。参数instrument_info(InstrumentInfoSchema): 待注册的设备信息对象。获取方式: 调用insTree_full_get获取设备树 → 找到key为UNREGISTERED_INSTRUMENT的分类节点 → 从其children列表中取出目标设备对象，直接作为本参数传入。返回bool，True=注册成功(设备状态变为AVAILABLE，从未注册分类移至对应接口分类)，False=注册失败。
   */
  async instrument_register_manual(instrument_info: InstrumentInfoSchema) {
    return await this.action<boolean>('instrument_register_manual', { instrument_info }, {
      headers: { 'X-UV-Action-Timeout': '20000' },
    })
  }

  /**
   * 手动注销仪器（从系统中移除已注册的设备，支持批量）。参数device_keys(list[str]): 要注销的设备key列表。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。示例: ["LAN_0001","LAN_0002"]。返回bool，True=注销成功(设备从已注册分类移至UNREGISTERED_INSTRUMENT分类)，False=注销失败。
   */
  async instrument_unregister(device_keys: any) {
    return await this.action<boolean>('instrument_unregister', { device_keys }, {
      headers: { 'X-UV-Action-Timeout': '15000' },
    })
  }

  /**
   * 增量更新仪器信息（仅更新指定字段，不影响其他字段）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数Incremental_info(str): 需要更新的字段JSON字符串，仅包含要修改的字段。示例: '{"deviceInfo":{"alias":"我的示波器"}}' 仅更新设备别名。返回bool，True=更新成功，False=更新失败。
   */
  async instrument_Update_info(device_key: string, Incremental_info: string) {
    return await this.action<boolean>('instrument_Update_info', { device_key, Incremental_info })
  }

  /**
   * 扫描发现仪器（异步轮询模式）。参数config(dict): 扫描配置字典，必须包含discoverType字段。discoverType当前支持的值: TCPIP(扫描LAN网络仪器，最常用)/USB(扫描USB连接的仪器)/UNKNOWN(扫描所有支持的接口类型)。调用示例: config={"discoverType":"TCPIP"}扫描网络仪器，config={"discoverType":"USB"}扫描USB仪器，config={"discoverType":"UNKNOWN"}扫描全部。返回InsScanResult，关键字段: is_finished(bool)扫描是否完成、device_count(int)已发现设备数、message(str)AI流程引导信息。【重要-异步轮询机制】首次调用启动扫描，若返回is_finished=False，需每隔2-3秒重复调用本接口(传入相同config参数)进行轮询，直到is_finished=True表示扫描完成。【后续步骤】扫描完成后，调用insTree_full_get获取设备树查看所有发现的仪器。新发现的设备会出现在UNREGISTERED_INSTRUMENT分类中，需调用instrument_register_manual注册后才能操作。【必读】message字段包含AI必须遵循的流程引导信息，请优先根据message内容决定下一步操作。
   */
  async discovery_start(config: any) {
    return await this.action<InsScanResult>('discovery_start', { config }, {
      headers: { 'X-UV-Action-Timeout': '30000' },
    })
  }

  /**
   * 停止当前正在进行的仪器扫描。无参数。返回InsScanResult，包含截止停止时刻的device_count(已发现设备数)和is_finished(通常为True)。若当前无正在运行的扫描任务，error字段会包含提示信息。停止后可调用insTree_full_get获取设备树查看已发现的设备。
   */
  async discovery_stop() {
    return await this.action<InsScanResult>('discovery_stop')
  }

  /**
   * 测试仪器连接是否正常（无需先独占设备）。参数devicekey_or_ResourceStr(str): 设备key或VISA资源字符串均可。获取方式: 调用insTree_full_get获取设备树 → 从目标设备取key字段或visaResourceString字段，任选其一传入。也可由用户直接提供VISA字符串，如"TCPIP0::192.168.1.100::inst0::INSTR"。返回ConnectTestResult，关键字段: success(bool)连接是否成功、status(str)设备状态枚举值(AVAILABLE=可用可操作/LOCKED=被占用/OFFLINE=离线/FAULT=故障/UNREGISTERED=未注册/CONNECTING=连接中)、error(str)失败原因。
   */
  async instrument_test_connection(devicekey_or_ResourceStr: string) {
    return await this.action<ConnectTestResult>('instrument_test_connection', { devicekey_or_ResourceStr }, {
      headers: { 'X-UV-Action-Timeout': '15000' },
    })
  }

  /**
   * 向指定设备发送单条SCPI命令并获取响应。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数command(str): 标准SCPI命令字符串。查询命令以?结尾，如"*IDN?"(查询设备标识)、":MEASure:VOLTage:DC?"(测量直流电压)；设置命令带参数，如"*RST"(复位)、":SOURce:VOLTage 5.0"(设置电压)、":OUTPut ON"(开启输出)。返回ScpiExecuteResult，关键字段: success(bool)是否成功、command(str)执行的命令、response(str)设备响应(查询命令返回数据，设置命令为None)、error(str)失败原因。【前提条件】设备的capabilities.supportsSCPI必须为True且status.connection为AVAILABLE。【建议流程】session_request_device(device_key)独占设备 → scpi_execute发送命令 → session_release_device(device_key)释放设备。
   */
  async scpi_execute(device_key: string, command: string) {
    return await this.action<ScpiExecuteResult>('scpi_execute', { device_key, command })
  }

  /**
   * 向同一设备按顺序执行多条SCPI命令序列（适用于需多步操作的场景，如先复位再测量）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数commands(List[str]): SCPI命令字符串列表，按数组顺序依次执行。示例: ["*RST","*IDN?",":MEAS:VOLT:DC?"]（先复位→查询标识→测量电压）。返回ScpiBatchExecuteResult，关键字段: success(bool)是否全部成功、results(List[ScpiExecuteResult])每条命令的独立结果(与commands索引一一对应)、error(str)全局错误。【前提条件】同scpi_execute，设备需supportsSCPI=True且connection=AVAILABLE。
   */
  async scpi_batch_execute(device_key: string, commands: string[]) {
    return await this.action<ScpiBatchExecuteResult>('scpi_batch_execute', { device_key, commands })
  }

  /**
   * 向多台设备同时发送同一条SCPI命令（适用于对多台设备批量下发统一指令）。参数device_list(List[str]): 目标设备key列表。获取方式: 调用insTree_full_get获取设备树 → 从各目标设备的InstrumentInfoSchema.key字段获取。示例: ["LAN_0001","LAN_0002"]。参数command(str): 要发送的单条SCPI命令字符串，同时发送给所有目标设备。示例: "*IDN?"。返回ScpimultiInsExecuteResult，关键字段: success(bool)是否全部成功、results(Dict[str,ScpiExecuteResult])以device_key为键的执行结果字典(可逐台检查)、error(str)全局错误。
   */
  async scpi_multiIns_execute(device_list: string[], command: string) {
    return await this.action<ScpimultiInsExecuteResult>('scpi_multiIns_execute', { device_list, command })
  }

  /**
   * 获取仪器SCPI资源集（命令集数据库）。参数resource_id(str): 资源标识符。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.resourceProfiles列表中 → 找到type=="SCPI_COMMAND_SET"的条目 → 取其uri字段值作为本参数。返回SCPI命令集JSON字符串，包含该设备支持的所有SCPI命令定义。
   */
  async scpi_resources_get(resource_id: string) {
    return await this.action<string>('scpi_resources_get', { resource_id })
  }

  /**
   * 获取仪器图标资源列表。参数resource_id(str): 资源标识符。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.resourceProfiles列表中 → 找到type=="ICON_SET"的条目 → 取其uri字段值作为本参数。返回图标资源路径列表(list[str])。
   */
  async icon_resources_get(resource_id: string) {
    return await this.action<any>('icon_resources_get', { resource_id })
  }

  /**
   * 获取仪器SCPI收藏夹（用户收藏的常用SCPI命令）。参数device_key(str): 设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回收藏的SCPI命令ID列表(list[str])。
   */
  async scpi_Favorites_get(device_key: string) {
    return await this.action<any>('scpi_Favorites_get', { device_key })
  }

  /**
   * 更新仪器SCPI收藏夹（覆盖式更新，传入的列表将替换原有收藏）。参数device_key(str): 设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数scpi_commands_ids(list[str]): 要收藏的SCPI命令ID列表，会覆盖替换该设备原有的全部收藏。返回更新后的收藏ID列表(list[str])，失败返回None。
   */
  async scpi_Favorites_update(device_key: string, scpi_commands_ids: any) {
    return await this.action<any | undefined>('scpi_Favorites_update', { device_key, scpi_commands_ids })
  }

  /**
   * 请求独占设备（锁定设备供当前会话专用，防止其他会话同时操作）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回bool，True=锁定成功，False=锁定失败(设备可能已被其他会话占用，status.isLocked=True)。【建议流程】执行SCPI命令前调用本接口独占设备 → 执行scpi_execute等命令 → 完成后调用session_release_device(相同device_key)释放。独占期间设备status.connection变为LOCKED，其他会话无法操作该设备。
   */
  async session_request_device(device_key: string) {
    return await this.action<boolean>('session_request_device', { device_key })
  }

  /**
   * 释放设备独占锁定（与session_request_device配对使用）。参数device_key(str): 要释放的设备唯一标识，与之前调用session_request_device时传入的device_key相同。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回bool，True=释放成功(设备status.connection恢复为AVAILABLE，其他会话可操作)，False=释放失败。
   */
  async session_release_device(device_key: string) {
    return await this.action<boolean>('session_release_device', { device_key })
  }

  /**
   * 获取当前应用全局设置参数。无参数。返回setting_model对象，包含: is_show_guidelines(是否开启引导)、is_multi_network_scan(是否多网段扫描)、scan_network_mask(扫描掩码)、scan_ip_ranges(自定义IP范围)、scan_timeout(扫描超时秒数)、is_scan_send_scpi_command(扫描时是否发送*IDN?)、lan_connect_test_interval(LAN检测间隔秒数)、scpi_command_end_setting(SCPI终止符:LF/CR/CRLF/NONE)。首次使用或未配置时可能返回None。
   */
  async Setting_parameter_get() {
    return await this.action<setting_model | undefined>('Setting_parameter_get')
  }

  /**
   * 更新应用全局设置参数。参数config(setting_model): 更新后的设置对象。【建议流程】先调用Setting_parameter_get获取当前配置 → 修改需要变更的字段 → 将完整对象传入本接口提交更新。返回更新后的完整setting_model对象。
   */
  async Setting_parameter_update(config: DeepPartial<setting_model>) {
    return await this.action<setting_model>('Setting_parameter_update', { config })
  }

  /**
   * 配置虚拟仪器与物理仪器的映射关系。（AI暂时请务必不要调用此接口，等后续版本支持后再调用）参数device_key(str): 虚拟仪器的设备key。获取方式: 调用insTree_full_get获取设备树 → 找到key为VIRTUAL_INSTRUMENT的分类节点 → 从其children中取目标虚拟仪器的InstrumentInfoSchema.key字段。参数instrument_map(str): 仪器映射配置JSON字符串，定义虚拟仪器与物理仪器的对应关系。返回bool，True=配置成功，False=配置失败。
   */
  async Virtual_instrument_config(device_key: string, instrument_map: string) {
    return await this.action<boolean>('Virtual_instrument_config', { device_key, instrument_map }, {
      headers: { 'X-UV-Action-Timeout': '15000' },
    })
  }

}