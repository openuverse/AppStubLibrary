# Python Action Stub
#
# Generated at: 2026-01-20 10:50:07
# SDK Version: 0.12.3
# App Name: AppManager
# App Version: 0.1.5
# Author: RIGOL Technology
# Description: The app manager to browse, install, update, launch, and uninstall applications.
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppRuntimeConfig


class UserCreate(BaseModel):
    """创建用户的请求模型."""

    name: "str"
    email: "str"
    age: "Optional[int]"


class UserDelete(BaseModel):
    """删除用户的请求模型."""

    id: "int"


class TaskRead(BaseModel):
    """读取任务的响应模型."""

    id: "int"
    title: "str"
    description: "Optional[str]"
    completed: "bool"
    priority: "int"
    user_id: "Optional[int]"
    created_at: "datetime"
    updated_at: "Optional[datetime]"


class UserUpdate(BaseModel):
    """更新用户的请求模型."""

    name: "Optional[str]"
    email: "Optional[str]"
    age: "Optional[int]"


class TaskCreate(BaseModel):
    """创建任务的请求模型."""

    title: "str"
    description: "Optional[str]"
    completed: "bool" = False
    priority: "int" = 1
    user_id: "Optional[int]"


class TaskDelete(BaseModel):
    """删除任务的请求模型."""

    id: "int"


class TaskUpdate(BaseModel):
    """更新任务的请求模型."""

    title: "Optional[str]"
    description: "Optional[str]"
    completed: "Optional[bool]"
    priority: "Optional[int]"
    user_id: "Optional[int]"


class UserRead(BaseModel):
    """读取用户的响应模型."""

    id: "int"
    name: "str"
    email: "str"
    age: "Optional[int]"
    created_at: "datetime"
    updated_at: "Optional[datetime]"


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = '14706eda67f34b7ebb4b487a0b6e7f2d', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'create_user': UserRead,
            'get_users': List[UserRead],
            'get_user': UserRead,
            'update_user': UserRead,
            'delete_user': Dict[str, str],
            'create_task': TaskRead,
            'get_tasks': List[TaskRead],
            'get_task': TaskRead,
            'update_task': TaskRead,
            'delete_task': Dict[str, str],
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

    def create_user(self, user: "UserCreate") -> "UserRead":
        """创建新用户"""
        return self('create_user', user=user)

    def get_users(self) -> "List[UserRead]":
        """获取所有用户列表"""
        return self('get_users')

    def get_user(self, user_id: "int") -> "UserRead":
        """根据ID获取用户"""
        return self('get_user', user_id=user_id)

    def update_user(self, user_id: "int", user_update: "UserUpdate") -> "UserRead":
        """更新用户信息"""
        return self('update_user', user_id=user_id, user_update=user_update)

    def delete_user(self, user_delete: "UserDelete") -> "Dict[str, str]":
        """删除用户"""
        return self('delete_user', user_delete=user_delete)

    def create_task(self, task: "TaskCreate") -> "TaskRead":
        """创建新任务"""
        return self('create_task', task=task)

    def get_tasks(self) -> "List[TaskRead]":
        """获取所有任务列表"""
        return self('get_tasks')

    def get_task(self, task_id: "int") -> "TaskRead":
        """根据ID获取任务"""
        return self('get_task', task_id=task_id)

    def update_task(self, task_id: "int", task_update: "TaskUpdate") -> "TaskRead":
        """更新任务信息"""
        return self('update_task', task_id=task_id, task_update=task_update)

    def delete_task(self, task_delete: "TaskDelete") -> "Dict[str, str]":
        """删除任务"""
        return self('delete_task', task_delete=task_delete)

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
