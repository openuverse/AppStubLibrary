# Python Action Stub
#
# Generated at: 2026-03-02 09:17:14
# SDK Version: 0.12.12
# App Name: uvapp_srv_sequenceworker
# App Version: 0.1.6
# Author: RIGOL Technology
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = '01bfa07867bc4b09a323fce50b0cfd2b', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'workflow_execute': Dict[str, Any],
            'workflow_stop': Dict[str, Any],
            'query_dll_functions': Dict[str, Any],
            'query_ivi_metadata': Dict[str, Any],
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

    def workflow_execute(self, execution_dsl: "Dict[str, Any]", inputs: "Optional[Dict[str, Any]]", workflow_id: "str") -> "Dict[str, Any]":
        """工作流启动执行"""
        return self('workflow_execute', execution_dsl=execution_dsl, inputs=inputs, workflow_id=workflow_id)

    def workflow_stop(self, project_id: "str", workflow_id: "str") -> "Dict[str, Any]":
        """工作流停止执行"""
        return self('workflow_stop', project_id=project_id, workflow_id=workflow_id)

    def query_dll_functions(self) -> "Dict[str, Any]":
        """反查dll中的函数"""
        return self('query_dll_functions', _timeout=60)

    def query_ivi_metadata(self) -> "Dict[str, Any]":
        """根据 session 获取 IVI 驱动的通道和属性信息"""
        return self('query_ivi_metadata', _timeout=60)
