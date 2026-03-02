# Python Action Stub
#
# Generated at: 2026-03-02 09:27:39
# SDK Version: 0.12.12
# App Name: uvapp_srv_aiworker
# App Version: 0.1.4
# Author: RIGOL Technology
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = 'd61cc09a1d8a48198ff5b6ab81dcbfd2', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'get_capabilities': List[Dict],
            'create_capability': Dict[str, Any],
            'update_capability': Dict[str, Any],
            'delete_capability': Dict[str, str],
            'toggle_capability': Dict[str, Any],
            'reload_capabilities': Dict[str, Any],
            'get_model_list': Dict[str, Any],
            'add_custom_model': Dict[str, str],
            'test_api_key': Dict[str, Any],
            'set_default_model': Dict[str, str],
            'get_conversation_list': List[Dict],
            'get_conversation_messages': List[Dict],
            'delete_conversation': Dict[str, str],
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

    def get_capabilities(self) -> "List[Any]":
        """获取能力列表"""
        return self('get_capabilities', _timeout=10)

    def create_capability(self, capability: "Any") -> "Dict[str, Any]":
        """创建新能力"""
        return self('create_capability', capability=capability, _timeout=10)

    def update_capability(self, capability_name: "str", capability_update: "Any") -> "Dict[str, Any]":
        """更新能力配置"""
        return self('update_capability', capability_name=capability_name, capability_update=capability_update, _timeout=10)

    def delete_capability(self, capability_name: "str") -> "Dict[str, str]":
        """删除能力"""
        return self('delete_capability', capability_name=capability_name, _timeout=10)

    def toggle_capability(self, capability_name: "str", in_use: "bool") -> "Dict[str, Any]":
        """切换能力启用状态"""
        return self('toggle_capability', capability_name=capability_name, in_use=in_use, _timeout=10)

    def reload_capabilities(self) -> "Dict[str, Any]":
        """重载能力（测试连接）"""
        return self('reload_capabilities', _timeout=60)

    def get_model_list(self) -> "Dict[str, Any]":
        """获取模型列表"""
        return self('get_model_list', _timeout=10)

    def add_custom_model(self, model_id: "str", input_modalities: "str", vendor: "str") -> "Dict[str, str]":
        """添加自定义模型"""
        return self('add_custom_model', model_id=model_id, input_modalities=input_modalities, vendor=vendor, _timeout=10)

    def test_api_key(self, api_url: "str", api_key: "str") -> "Dict[str, Any]":
        """检查API密钥"""
        return self('test_api_key', api_url=api_url, api_key=api_key, _timeout=30)

    def set_default_model(self, model_id: "str") -> "Dict[str, str]":
        """设置默认模型"""
        return self('set_default_model', model_id=model_id, _timeout=10)

    def get_conversation_list(self) -> "List[Any]":
        """获取会话列表"""
        return self('get_conversation_list', _timeout=10)

    def get_conversation_messages(self, conversation_id: "str") -> "List[Any]":
        """获取会话消息"""
        return self('get_conversation_messages', conversation_id=conversation_id, _timeout=10)

    def delete_conversation(self, conversation_id: "str") -> "Dict[str, str]":
        """删除会话"""
        return self('delete_conversation', conversation_id=conversation_id, _timeout=10)
