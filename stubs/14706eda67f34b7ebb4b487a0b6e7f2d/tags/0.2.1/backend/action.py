# Python Action Stub
#
# Generated at: 2026-02-28 08:04:44
# SDK Version: 0.12.10
# App Name: Nexus
# App Version: 0.2.1
# Author: RIGOL Technology
# Description: Nexus is the app manager to browse, install, update, launch, and uninstall applications.
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = '14706eda67f34b7ebb4b487a0b6e7f2d', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'apps_list': Dict[str, Any],
            'app_detail': Dict[str, Any],
            'app_local_install': Dict[str, Any],
            'app_local_update': Dict[str, Any],
            'app_local_uninstall': Dict[str, Any],
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

    def apps_list(self, scope: "str", search: "str", instrument_type: "str", fee_type: "str", install_status: "str", page: "int", page_size: "int") -> "Dict[str, Any]":
        """应用列表"""
        return self('apps_list', scope=scope, search=search, instrument_type=instrument_type, fee_type=fee_type, install_status=install_status, page=page, page_size=page_size)

    def app_detail(self, app_id: "str") -> "Dict[str, Any]":
        """应用详情"""
        return self('app_detail', app_id=app_id)

    def app_local_install(self, filename: "str", file_content: "Any") -> "Dict[str, Any]":
        """本地安装应用"""
        return self('app_local_install', filename=filename, file_content=file_content, _timeout=60)

    def app_local_update(self, app_id: "str", filename: "str", file_content: "Any") -> "Dict[str, Any]":
        """本地更新应用"""
        return self('app_local_update', app_id=app_id, filename=filename, file_content=file_content, _timeout=60)

    def app_local_uninstall(self, app_id: "str") -> "Dict[str, Any]":
        """卸载本地应用"""
        return self('app_local_uninstall', app_id=app_id, _timeout=30)
