# Python Action Stub
#
# Generated at: 2026-03-02 08:57:04
# SDK Version: 0.12.12
# App Name: Atlas
# App Version: 0.1.11
# Author: RIGOL Technology
# Description: Professional test and measurement instrument management software with automatic discovery, unified management, and real-time monitoring capabilities
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class DeviceInfoSchema(BaseModel):
    """设备静态属性信息，嵌套于 InstrumentInfoSchema.deviceInfo。"""

    name: "str"
    model: "str"
    manufacturer: "str"
    alias: "Optional[str]"
    type: "str"
    instrumentType: "str"
    interfaceType: "str"
    serialNumber: "Optional[str]"
    firmwareVersion: "Optional[str]"
    description: "Optional[str]"


class CapabilitiesSchema(BaseModel):
    """设备能力标记，嵌套于 InstrumentInfoSchema.capabilities。"""

    supportsSCPI: "bool"
    supportsIVI: "bool"
    supportsDataStreaming: "bool"
    supportsWebUi: "bool"


class StatusSchema(BaseModel):
    """设备实时运行状态，嵌套于 InstrumentInfoSchema.status。"""

    connection: "str"
    health: "str"
    discoverSource: "Optional[str]"
    registeredAt: "Optional[str]"
    lastUpdated: "Optional[str]"
    isLocked: "bool"


class ScpilogHistorySchema(BaseModel):
    """SCPI命令执行历史日志，嵌套于 ScpiCapabilitiesSchema.historyLog。"""

    id: "int"
    text: "str"
    sendresult: "Optional[str]"
    readresult: "Optional[str]"
    timestamp: "Optional[str]"


class ScpiCommandSchema(BaseModel):
    """SCPI命令定义条目，嵌套于 ScpiCapabilitiesSchema.commands。"""

    command: "str"
    description: "str"
    units: "str"
    ranges: "str"
    returnType: "str"


class ScpiCapabilitiesSchema(BaseModel):
    """设备SCPI能力集合，嵌套于 InstrumentInfoSchema.scpiCapabilities。"""

    commands: "List[ScpiCommandSchema]" = ('_class_ref_', 'list')
    historyLog: "List[ScpilogHistorySchema]" = ('_class_ref_', 'list')
    defCRCFormat: "str"


class ResourceProfileSchema(BaseModel):
    """设备关联资源配置，嵌套于 InstrumentInfoSchema.resourceProfiles。"""

    uri: "str"
    version: "str"
    type: "str"
    other: "Optional[str]"


class InstrumentInfoSchema(BaseModel):
    """单台设备的完整信息模型（设备树节点）。"""

    label: "str"
    key: "str"
    visaResourceString: "str"
    status: "StatusSchema"
    deviceInfo: "DeviceInfoSchema"
    capabilities: "CapabilitiesSchema"
    scpiCapabilities: "ScpiCapabilitiesSchema"
    selfCapabilities: "Dict[str, Any]" = ('_class_ref_', 'dict')
    dynamicData: "Dict[str, Any]" = ('_class_ref_', 'dict')
    resourceProfiles: "List[ResourceProfileSchema]" = ('_class_ref_', 'list')
    children: "List[InstrumentInfoSchema]" = ('_class_ref_', 'list')


class CategoryNodeSchema(BaseModel):
    """设备分类节点（设备树一级分类），嵌套于 InstrumentTreeSchema.categories。"""

    label: "str"
    key: "str"
    children: "List[InstrumentInfoSchema]" = ('_class_ref_', 'list')


class ScpiExecuteResult(BaseModel):
    """单条SCPI命令执行结果模型。"""

    success: "bool"
    command: "str"
    response: "Optional[str]"
    error: "Optional[str]"


class ScpimultiInsExecuteResult(BaseModel):
    """多设备统一SCPI命令执行结果模型。"""

    success: "bool"
    results: "Dict[str, ScpiExecuteResult]" = ('_class_ref_', 'dict')
    error: "Optional[str]"


class InstrumentTreeSchema(BaseModel):
    """完整的设备树结构（顶层模型）。"""

    timestamp: "str"
    syncId: "int"
    messageType: "str"
    categories: "List[CategoryNodeSchema]" = ('_class_ref_', 'list')


class ScpiBatchExecuteResult(BaseModel):
    """SCPI批量命令序列执行结果模型。"""

    success: "bool"
    results: "List[ScpiExecuteResult]" = ('_class_ref_', 'list')
    error: "Optional[str]"


class ConnectTestResult(BaseModel):
    """仪器连接测试结果模型。"""

    success: "bool"
    error: "Optional[str]"
    status: "str"


class setting_model(BaseModel):
    """应用全局设置参数模型。"""

    is_show_guidelines: "bool" = True
    is_multi_network_scan: "bool" = True
    scan_network_mask: "str" = '255.255.255.0'
    scan_ip_ranges: "List[str]" = []
    scan_timeout: "int" = 30
    is_scan_send_scpi_command: "bool" = True
    lan_connect_test_interval: "int" = 30
    scpi_command_end_setting: "Optional[str]"


class InsScanResult(BaseModel):
    """仪器扫描结果模型。"""

    device_count: "int"
    is_finished: "bool"
    error: "Optional[str]"
    message: "Optional[str]"


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = 'd0a9a7f6473948c6b5ee204c4d4dea10', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'insTree_full_get': InstrumentTreeSchema,
            'discovery_start': InsScanResult,
            'discovery_stop': InsScanResult,
            'instrument_test_connection': ConnectTestResult,
            'scpi_execute': ScpiExecuteResult,
            'scpi_batch_execute': ScpiBatchExecuteResult,
            'scpi_multiIns_execute': ScpimultiInsExecuteResult,
            'Setting_parameter_update': setting_model,
        }

    def get_app_config(self) -> "AppConfig":
        """get app info"""
        return self('get_app_config')

    def get_all_action_details(self) -> "Dict[str, ActionInfo]":
        """get app action details"""
        return self('get_all_action_details')

    def get_all_attribute_groups(self) -> "List[str]":
        """get all attribute groups"""
        return self('get_all_attribute_groups')

    def trig_attributes_snapshot(self, group_name: "str") -> "bool":
        """trigger once attributes snapshot push for a group"""
        return self('trig_attributes_snapshot', group_name=group_name)

    def get_attribute(self, attribute_path: "str") -> "Any":
        """get attribute value by path"""
        return self('get_attribute', attribute_path=attribute_path)

    def set_attribute(self, attribute_path: "str", value: "Any") -> "bool":
        """set attribute value by path"""
        return self('set_attribute', attribute_path=attribute_path, value=value)

    def shutdown_app(self, reason: "str") -> "Any":
        """shutdown app"""
        return self('shutdown_app', reason=reason)

    def insTree_full_sync(self) -> "None":
        """触发完整设备树同步推送（前端专用，AI通常无需调用）。无参数，无返回值。调用后系统通过WebSocket向前端推送最新设备树数据。AI如需获取设备树数据，请改用insTree_full_get。"""
        return self('insTree_full_sync')

    def insTree_full_get(self) -> "InstrumentTreeSchema":
        """获取完整设备树（这是获取设备信息的核心入口）。无参数。返回InstrumentTreeSchema，其中categories列表包含所有分类节点（LAN_INSTRUMENT/USB_INSTRUMENT/GPIB_INSTRUMENT/SERIAL_INSTRUMENT/PXI_INSTRUMENT/VIRTUAL_INSTRUMENT/UNREGISTERED_INSTRUMENT），每个分类的children列表包含该分类下所有设备的InstrumentInfoSchema。【关键】后续所有设备操作（scpi_execute/session_request_device/instrument_test_connection等）的device_key参数，均需从本接口返回的设备树中某个设备的key字段获取。同理，visaResourceString也从设备的visaResourceString字段获取。【典型流程】1.调用本接口获取设备树 → 2.遍历categories[i].children找到目标设备 → 3.取设备的key调用后续action。"""
        return self('insTree_full_get')

    def instrument_create_manual(self, visaResourceString: "str") -> "Optional[InstrumentInfoSchema]":
        """手动创建仪器（仅在设备树中不存在该设备时使用，若设备已在未注册分类中，应使用instrument_register_manual注册）。参数visaResourceString(str): 设备的VISA资源字符串。获取方式: 可从insTree_full_get返回的设备树中某设备的visaResourceString字段获取，或由用户手动提供。格式示例: LAN设备"TCPIP0::192.168.1.100::inst0::INSTR"，USB设备"USB0::0x1AB1::0x04CE::DS1ZA123456789::INSTR"。返回InstrumentInfoSchema(创建成功，含key/状态/能力等完整信息)或None(创建失败)。创建后设备自动添加到设备树。"""
        return self('instrument_create_manual', visaResourceString=visaResourceString, _timeout=20)

    def instrument_register_manual(self, instrument_info: "InstrumentInfoSchema") -> "bool":
        """手动注册仪器（将设备树中未注册分类下的设备注册到系统）。参数instrument_info(InstrumentInfoSchema): 待注册的设备信息对象。获取方式: 调用insTree_full_get获取设备树 → 找到key为UNREGISTERED_INSTRUMENT的分类节点 → 从其children列表中取出目标设备对象，直接作为本参数传入。返回bool，True=注册成功(设备状态变为AVAILABLE，从未注册分类移至对应接口分类)，False=注册失败。"""
        return self('instrument_register_manual', instrument_info=instrument_info, _timeout=20)

    def instrument_unregister(self, device_keys: "List[str]") -> "bool":
        """手动注销仪器（从系统中移除已注册的设备，支持批量）。参数device_keys(list[str]): 要注销的设备key列表。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。示例: ["LAN_0001","LAN_0002"]。返回bool，True=注销成功(设备从已注册分类移至UNREGISTERED_INSTRUMENT分类)，False=注销失败。"""
        return self('instrument_unregister', device_keys=device_keys, _timeout=15)

    def instrument_Update_info(self, device_key: "str", Incremental_info: "str") -> "bool":
        """增量更新仪器信息（仅更新指定字段，不影响其他字段）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数Incremental_info(str): 需要更新的字段JSON字符串，仅包含要修改的字段。示例: '{"deviceInfo":{"alias":"我的示波器"}}' 仅更新设备别名。返回bool，True=更新成功，False=更新失败。"""
        return self('instrument_Update_info', device_key=device_key, Incremental_info=Incremental_info)

    def discovery_start(self, config: "Any") -> "InsScanResult":
        """扫描发现仪器（异步轮询模式）。参数config(dict): 扫描配置字典，必须包含discoverType字段。discoverType当前支持的值: TCPIP(扫描LAN网络仪器，最常用)/USB(扫描USB连接的仪器)/UNKNOWN(扫描所有支持的接口类型)。调用示例: config={"discoverType":"TCPIP"}扫描网络仪器，config={"discoverType":"USB"}扫描USB仪器，config={"discoverType":"UNKNOWN"}扫描全部。返回InsScanResult，关键字段: is_finished(bool)扫描是否完成、device_count(int)已发现设备数、message(str)AI流程引导信息。【重要-异步轮询机制】首次调用启动扫描，若返回is_finished=False，需每隔2-3秒重复调用本接口(传入相同config参数)进行轮询，直到is_finished=True表示扫描完成。【后续步骤】扫描完成后，调用insTree_full_get获取设备树查看所有发现的仪器。新发现的设备会出现在UNREGISTERED_INSTRUMENT分类中，需调用instrument_register_manual注册后才能操作。【必读】message字段包含AI必须遵循的流程引导信息，请优先根据message内容决定下一步操作。"""
        return self('discovery_start', config=config, _timeout=30)

    def discovery_stop(self) -> "InsScanResult":
        """停止当前正在进行的仪器扫描。无参数。返回InsScanResult，包含截止停止时刻的device_count(已发现设备数)和is_finished(通常为True)。若当前无正在运行的扫描任务，error字段会包含提示信息。停止后可调用insTree_full_get获取设备树查看已发现的设备。"""
        return self('discovery_stop')

    def instrument_test_connection(self, devicekey_or_ResourceStr: "str") -> "ConnectTestResult":
        """测试仪器连接是否正常（无需先独占设备）。参数devicekey_or_ResourceStr(str): 设备key或VISA资源字符串均可。获取方式: 调用insTree_full_get获取设备树 → 从目标设备取key字段或visaResourceString字段，任选其一传入。也可由用户直接提供VISA字符串，如"TCPIP0::192.168.1.100::inst0::INSTR"。返回ConnectTestResult，关键字段: success(bool)连接是否成功、status(str)设备状态枚举值(AVAILABLE=可用可操作/LOCKED=被占用/OFFLINE=离线/FAULT=故障/UNREGISTERED=未注册/CONNECTING=连接中)、error(str)失败原因。"""
        return self('instrument_test_connection', devicekey_or_ResourceStr=devicekey_or_ResourceStr, _timeout=15)

    def scpi_execute(self, device_key: "str", command: "str") -> "ScpiExecuteResult":
        """向指定设备发送单条SCPI命令并获取响应。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数command(str): 标准SCPI命令字符串。查询命令以?结尾，如"*IDN?"(查询设备标识)、":MEASure:VOLTage:DC?"(测量直流电压)；设置命令带参数，如"*RST"(复位)、":SOURce:VOLTage 5.0"(设置电压)、":OUTPut ON"(开启输出)。返回ScpiExecuteResult，关键字段: success(bool)是否成功、command(str)执行的命令、response(str)设备响应(查询命令返回数据，设置命令为None)、error(str)失败原因。【前提条件】设备的capabilities.supportsSCPI必须为True且status.connection为AVAILABLE。【建议流程】session_request_device(device_key)独占设备 → scpi_execute发送命令 → session_release_device(device_key)释放设备。"""
        return self('scpi_execute', device_key=device_key, command=command)

    def scpi_batch_execute(self, device_key: "str", commands: "List[str]") -> "ScpiBatchExecuteResult":
        """向同一设备按顺序执行多条SCPI命令序列（适用于需多步操作的场景，如先复位再测量）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数commands(List[str]): SCPI命令字符串列表，按数组顺序依次执行。示例: ["*RST","*IDN?",":MEAS:VOLT:DC?"]（先复位→查询标识→测量电压）。返回ScpiBatchExecuteResult，关键字段: success(bool)是否全部成功、results(List[ScpiExecuteResult])每条命令的独立结果(与commands索引一一对应)、error(str)全局错误。【前提条件】同scpi_execute，设备需supportsSCPI=True且connection=AVAILABLE。"""
        return self('scpi_batch_execute', device_key=device_key, commands=commands)

    def scpi_multiIns_execute(self, device_list: "List[str]", command: "str") -> "ScpimultiInsExecuteResult":
        """向多台设备同时发送同一条SCPI命令（适用于对多台设备批量下发统一指令）。参数device_list(List[str]): 目标设备key列表。获取方式: 调用insTree_full_get获取设备树 → 从各目标设备的InstrumentInfoSchema.key字段获取。示例: ["LAN_0001","LAN_0002"]。参数command(str): 要发送的单条SCPI命令字符串，同时发送给所有目标设备。示例: "*IDN?"。返回ScpimultiInsExecuteResult，关键字段: success(bool)是否全部成功、results(Dict[str,ScpiExecuteResult])以device_key为键的执行结果字典(可逐台检查)、error(str)全局错误。"""
        return self('scpi_multiIns_execute', device_list=device_list, command=command)

    def scpi_resources_get(self, resource_id: "str") -> "str":
        """获取仪器SCPI资源集（命令集数据库）。参数resource_id(str): 资源标识符。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.resourceProfiles列表中 → 找到type=="SCPI_COMMAND_SET"的条目 → 取其uri字段值作为本参数。返回SCPI命令集JSON字符串，包含该设备支持的所有SCPI命令定义。"""
        return self('scpi_resources_get', resource_id=resource_id)

    def icon_resources_get(self, resource_id: "str") -> "List[str]":
        """获取仪器图标资源列表。参数resource_id(str): 资源标识符。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.resourceProfiles列表中 → 找到type=="ICON_SET"的条目 → 取其uri字段值作为本参数。返回图标资源路径列表(list[str])。"""
        return self('icon_resources_get', resource_id=resource_id)

    def scpi_Favorites_get(self, device_key: "str") -> "List[str]":
        """获取仪器SCPI收藏夹（用户收藏的常用SCPI命令）。参数device_key(str): 设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回收藏的SCPI命令ID列表(list[str])。"""
        return self('scpi_Favorites_get', device_key=device_key)

    def scpi_Favorites_update(self, device_key: "str", scpi_commands_ids: "List[str]") -> "Optional[List[str]]":
        """更新仪器SCPI收藏夹（覆盖式更新，传入的列表将替换原有收藏）。参数device_key(str): 设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。参数scpi_commands_ids(list[str]): 要收藏的SCPI命令ID列表，会覆盖替换该设备原有的全部收藏。返回更新后的收藏ID列表(list[str])，失败返回None。"""
        return self('scpi_Favorites_update', device_key=device_key, scpi_commands_ids=scpi_commands_ids)

    def session_request_device(self, device_key: "str") -> "bool":
        """请求独占设备（锁定设备供当前会话专用，防止其他会话同时操作）。参数device_key(str): 目标设备唯一标识。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回bool，True=锁定成功，False=锁定失败(设备可能已被其他会话占用，status.isLocked=True)。【建议流程】执行SCPI命令前调用本接口独占设备 → 执行scpi_execute等命令 → 完成后调用session_release_device(相同device_key)释放。独占期间设备status.connection变为LOCKED，其他会话无法操作该设备。"""
        return self('session_request_device', device_key=device_key)

    def session_release_device(self, device_key: "str") -> "bool":
        """释放设备独占锁定（与session_request_device配对使用）。参数device_key(str): 要释放的设备唯一标识，与之前调用session_request_device时传入的device_key相同。获取方式: 调用insTree_full_get获取设备树 → 从目标设备的InstrumentInfoSchema.key字段获取。返回bool，True=释放成功(设备status.connection恢复为AVAILABLE，其他会话可操作)，False=释放失败。"""
        return self('session_release_device', device_key=device_key)

    def Setting_parameter_get(self) -> "Optional[setting_model]":
        """获取当前应用全局设置参数。无参数。返回setting_model对象，包含: is_show_guidelines(是否开启引导)、is_multi_network_scan(是否多网段扫描)、scan_network_mask(扫描掩码)、scan_ip_ranges(自定义IP范围)、scan_timeout(扫描超时秒数)、is_scan_send_scpi_command(扫描时是否发送*IDN?)、lan_connect_test_interval(LAN检测间隔秒数)、scpi_command_end_setting(SCPI终止符:LF/CR/CRLF/NONE)。首次使用或未配置时可能返回None。"""
        return self('Setting_parameter_get')

    def Setting_parameter_update(self, config: "setting_model") -> "setting_model":
        """更新应用全局设置参数。参数config(setting_model): 更新后的设置对象。【建议流程】先调用Setting_parameter_get获取当前配置 → 修改需要变更的字段 → 将完整对象传入本接口提交更新。返回更新后的完整setting_model对象。"""
        return self('Setting_parameter_update', config=config)

    def Virtual_instrument_config(self, device_key: "str", instrument_map: "str") -> "bool":
        """配置虚拟仪器与物理仪器的映射关系。（AI暂时请务必不要调用此接口，等后续版本支持后再调用）参数device_key(str): 虚拟仪器的设备key。获取方式: 调用insTree_full_get获取设备树 → 找到key为VIRTUAL_INSTRUMENT的分类节点 → 从其children中取目标虚拟仪器的InstrumentInfoSchema.key字段。参数instrument_map(str): 仪器映射配置JSON字符串，定义虚拟仪器与物理仪器的对应关系。返回bool，True=配置成功，False=配置失败。"""
        return self('Virtual_instrument_config', device_key=device_key, instrument_map=instrument_map, _timeout=15)
