# Python Action Stub
#
# Generated at: 2026-02-28 10:31:39
# SDK Version: 0.12.10
# App Name: uv_srv_messagebus
# App Version: 0.5.1
# Author: RIGOL Technology
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class ClientInfo(BaseModel):
    """平台Client信息"""

    worker_id: "str"
    worker_name: "str"
    version: "str"
    app_config: "Optional[Dict[str, Any]]"
    manifest: "Optional[Dict[str, Any]]"
    topics: "Any" = ('_class_ref_', 'set')
    last_heartbeat: "datetime"
    status: "str" = 'active'
    heartbeat_count: "int" = 0
    heartbeat_interval: "int" = 3
    missed_heartbeats: "int" = 0
    connect_time: "datetime"


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = 'e6c8dfd5d79045e8b3e21515aceda86d', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'get_active_clients': Dict[str, ClientInfo] | None,
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

    def get_messagebus_status(self) -> "Any":
        """获取MessageBus服务状态"""
        return self('get_messagebus_status')

    def get_active_clients(self) -> "Dict[str, Any]":
        """获取活跃的Clients"""
        return self('get_active_clients')

    def get_message_probe_config(self) -> "Any":
        """获取消息探针配置"""
        return self('get_message_probe_config')

    def change_probe_config(self, key: "str", value: "Any") -> "None":
        """更改消息探针配置"""
        return self('change_probe_config', key=key, value=value)

    def open_message_probe(self) -> "None":
        """打开消息探针"""
        return self('open_message_probe')

    def close_message_probe(self) -> "None":
        """关闭消息探针"""
        return self('close_message_probe')

    def query_probe_records(self, page: "int", page_size: "int", message_type: "Any", topic: "Any", source_id: "Any", target_id: "Any") -> "Any":
        """查询消息探针记录（支持分页）"""
        return self('query_probe_records', page=page, page_size=page_size, message_type=message_type, topic=topic, source_id=source_id, target_id=target_id)

    def count_probe_records(self) -> "Any":
        """统计消息探针文件记录数"""
        return self('count_probe_records')
