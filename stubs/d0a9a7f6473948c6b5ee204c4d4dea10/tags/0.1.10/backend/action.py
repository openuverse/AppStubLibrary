# Python Action Stub
#
# Generated at: 2026-02-28 07:19:31
# SDK Version: 0.12.10
# App Name: Atlas
# App Version: 0.1.10
# Author: RIGOL Technology
# Description: Professional test and measurement instrument management software with automatic discovery, unified management, and real-time monitoring capabilities
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class InsScanResult(BaseModel):
    """仪器扫描结果"""

    device_count: "int"
    is_finished: "bool"
    error: "Optional[str]"
    message: "Optional[str]"


class ConnectTestResult(BaseModel):
    """资源连接测试结果"""

    success: "bool"
    error: "Optional[str]"
    status: "str"


class ScpiExecuteResult(BaseModel):
    """SCPI执行结果"""

    success: "bool"
    command: "str"
    response: "Optional[str]"
    error: "Optional[str]"


class DeviceInfoSchema(BaseModel):
    """设备静态信息（Schema）"""

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


class ScpilogHistorySchema(BaseModel):
    """SCPI 日志历史记录（Schema）"""

    id: "int"
    text: "str"
    sendresult: "Optional[str]"
    readresult: "Optional[str]"
    timestamp: "Optional[str]"


class CapabilitiesSchema(BaseModel):
    """设备能力描述（Schema）"""

    supportsSCPI: "bool"
    supportsIVI: "bool"
    supportsDataStreaming: "bool"
    supportsWebUi: "bool"


class ScpiCommandSchema(BaseModel):
    """SCPI 命令定义（Schema）"""

    command: "str"
    description: "str"
    units: "str"
    ranges: "str"
    returnType: "str"


class ScpiCapabilitiesSchema(BaseModel):
    """SCPI 能力集合（Schema）"""

    commands: "List[ScpiCommandSchema]" = ('_class_ref_', 'list')
    historyLog: "List[ScpilogHistorySchema]" = ('_class_ref_', 'list')
    defCRCFormat: "str"


class StatusSchema(BaseModel):
    """设备运行状态信息（Schema）"""

    connection: "str"
    health: "str"
    discoverSource: "Optional[str]"
    registeredAt: "Optional[str]"
    lastUpdated: "Optional[str]"
    isLocked: "bool"


class ResourceProfileSchema(BaseModel):
    """资源配置信息（Schema）"""

    uri: "str"
    version: "str"
    type: "str"
    other: "Optional[str]"


class InstrumentInfoSchema(BaseModel):
    """设备信息主类（Schema）"""

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
    """设备分类节点（Schema）"""

    label: "str"
    key: "str"
    children: "List[InstrumentInfoSchema]" = ('_class_ref_', 'list')


class InstrumentTreeSchema(BaseModel):
    """完整的设备树结构（Schema）"""

    timestamp: "str"
    syncId: "int"
    messageType: "str"
    categories: "List[CategoryNodeSchema]" = ('_class_ref_', 'list')


class ScpimultiInsExecuteResult(BaseModel):
    """多设备统一SCPI指令执行结果"""

    success: "bool"
    results: "Dict[str, ScpiExecuteResult]" = ('_class_ref_', 'dict')
    error: "Optional[str]"


class ScpiBatchExecuteResult(BaseModel):
    """SCPI批量执行结果"""

    success: "bool"
    results: "List[ScpiExecuteResult]" = ('_class_ref_', 'list')
    error: "Optional[str]"


class setting_model(BaseModel):
    """创建设置的请求模型."""

    is_show_guidelines: "bool" = True
    is_multi_network_scan: "bool" = True
    scan_network_mask: "str" = '255.255.255.0'
    scan_ip_ranges: "List[str]" = []
    scan_timeout: "int" = 30
    is_scan_send_scpi_command: "bool" = True
    lan_connect_test_interval: "int" = 30
    scpi_command_end_setting: "Optional[str]"


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

    def insTree_full_sync(self) -> "None":
        """请求完整设备树同步"""
        return self('insTree_full_sync')

    def insTree_full_get(self) -> "InstrumentTreeSchema":
        """请求完整设备树获取"""
        return self('insTree_full_get')

    def instrument_create_manual(self, visaResourceString: "str") -> "Optional[InstrumentInfoSchema]":
        """手动创建仪器-未在仪器树中存在"""
        return self('instrument_create_manual', visaResourceString=visaResourceString, _timeout=20)

    def instrument_register_manual(self, instrument_info: "InstrumentInfoSchema") -> "bool":
        """手动注册仪器-已存在仪器树中的未注册分类中"""
        return self('instrument_register_manual', instrument_info=instrument_info, _timeout=20)

    def instrument_unregister(self, device_keys: "List[str]") -> "bool":
        """手动注销仪器"""
        return self('instrument_unregister', device_keys=device_keys, _timeout=15)

    def instrument_Update_info(self, device_key: "str", Incremental_info: "str") -> "bool":
        """获取仪器信息"""
        return self('instrument_Update_info', device_key=device_key, Incremental_info=Incremental_info)

    def discovery_start(self, config: "Any") -> "InsScanResult":
        """扫描仪器"""
        return self('discovery_start', config=config, _timeout=30)

    def discovery_stop(self) -> "InsScanResult":
        """停止扫描"""
        return self('discovery_stop')

    def instrument_test_connection(self, devicekey_or_ResourceStr: "str") -> "ConnectTestResult":
        """测试仪器连接"""
        return self('instrument_test_connection', devicekey_or_ResourceStr=devicekey_or_ResourceStr, _timeout=15)

    def scpi_execute(self, device_key: "str", command: "str") -> "ScpiExecuteResult":
        """执行单条SCPI命令"""
        return self('scpi_execute', device_key=device_key, command=command)

    def scpi_batch_execute(self, device_key: "str", commands: "List[str]") -> "ScpiBatchExecuteResult":
        """执行SCPI命令序列"""
        return self('scpi_batch_execute', device_key=device_key, commands=commands)

    def scpi_multiIns_execute(self, device_list: "List[str]", command: "str") -> "ScpimultiInsExecuteResult":
        """执行多设备统一SCPI指令"""
        return self('scpi_multiIns_execute', device_list=device_list, command=command)

    def scpi_resources_get(self, resource_id: "str") -> "str":
        """获取仪器SCPI资源集"""
        return self('scpi_resources_get', resource_id=resource_id)

    def icon_resources_get(self, resource_id: "str") -> "List[str]":
        """获取仪器SCPI命令集"""
        return self('icon_resources_get', resource_id=resource_id)

    def scpi_Favorites_get(self, device_key: "str") -> "List[str]":
        """获取仪器SCPI收藏夹"""
        return self('scpi_Favorites_get', device_key=device_key)

    def scpi_Favorites_update(self, device_key: "str", scpi_commands_ids: "List[str]") -> "Optional[List[str]]":
        """更新仪器SCPI收藏夹"""
        return self('scpi_Favorites_update', device_key=device_key, scpi_commands_ids=scpi_commands_ids)

    def session_request_device(self, device_key: "str") -> "bool":
        """请求独占设备"""
        return self('session_request_device', device_key=device_key)

    def session_release_device(self, device_key: "str") -> "bool":
        """释放设备占用"""
        return self('session_release_device', device_key=device_key)

    def Setting_parameter_get(self) -> "Optional[setting_model]":
        """设置参数获取"""
        return self('Setting_parameter_get')

    def Setting_parameter_update(self, config: "setting_model") -> "setting_model":
        """设置参数更新"""
        return self('Setting_parameter_update', config=config)

    def Virtual_instrument_config(self, device_key: "str", instrument_map: "str") -> "bool":
        """虚拟仪器配置"""
        return self('Virtual_instrument_config', device_key=device_key, instrument_map=instrument_map, _timeout=15)
