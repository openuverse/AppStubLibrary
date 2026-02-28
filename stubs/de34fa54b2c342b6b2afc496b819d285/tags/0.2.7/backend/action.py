# Python Action Stub
#
# Generated at: 2026-02-28 08:11:09
# SDK Version: 0.12.10
# App Name: uvapp_srv_daemonworker
# App Version: 0.2.7
# Author: RIGOL Technology
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class ChildProcessInfo(BaseModel):
    """子进程信息"""

    pid: "int"
    name: "str"
    status: "str"
    cpu_percent: "float" = 0.0
    memory_rss: "float" = 0.0
    memory_percent: "float" = 0.0
    num_threads: "int" = 0
    create_time: "float" = 0.0
    cmdline: "List[str]" = ('_class_ref_', 'list')


class ProcessMetrics(BaseModel):
    """process metrics"""

    pid: "int"
    worker_id: "str"
    worker_name: "str" = 'UnknownWorker'
    cpu_percent: "float"
    memory_percent: "float"
    memory_rss: "float"
    memory_vms: "float"
    num_threads: "int"
    io_read_count: "int"
    io_write_count: "int"
    io_read_bytes: "int"
    io_write_bytes: "int"
    create_time: "float"
    status: "str"
    timestamp: "datetime"
    num_children: "int" = 0
    children_pids: "List[int]" = ('_class_ref_', 'list')
    children_details: "List[ChildProcessInfo]" = ('_class_ref_', 'list')


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = 'de34fa54b2c342b6b2afc496b819d285', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'get_workers_info': List[Any],
            'get_total_status': List[ProcessMetrics],
            'get_system_status': ProcessMetrics,
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

    def change_platform_language(self, language: "str") -> "None":
        """更改平台语言"""
        return self('change_platform_language', language=language)

    def change_platform_theme(self, theme: "str") -> "None":
        """更改平台主题"""
        return self('change_platform_theme', theme=theme)

    def get_platform_language(self) -> "str":
        """获取平台语言"""
        return self('get_platform_language')

    def get_platform_theme(self) -> "str":
        """获取平台主题"""
        return self('get_platform_theme')

    def get_platform_config(self, tag: "str") -> "Any":
        """获取平台配置"""
        return self('get_platform_config', tag=tag)

    def set_platform_config(self, tag: "str", value: "Any") -> "None":
        """设置平台配置"""
        return self('set_platform_config', tag=tag, value=value)

    def get_workers_info(self) -> "List[Any]":
        """获取启动的worker信息"""
        return self('get_workers_info')

    def start_worker(self, worker_id: "str") -> "bool":
        """启动worker"""
        return self('start_worker', worker_id=worker_id, _timeout=10)

    def stop_worker(self, worker_id: "str") -> "bool":
        """停止worker"""
        return self('stop_worker', worker_id=worker_id)

    def restart_worker(self, worker_id: "str") -> "bool":
        """重启worker"""
        return self('restart_worker', worker_id=worker_id)

    def restart_platform(self) -> "bool":
        """重启主进程"""
        return self('restart_platform')

    def change_data_directory(self, new_data_directory: "str") -> "bool":
        """更改平台数据目录"""
        return self('change_data_directory', new_data_directory=new_data_directory, _timeout=10)

    def change_repo_directory(self, new_repo_directory: "str") -> "bool":
        """更改平台repo目录"""
        return self('change_repo_directory', new_repo_directory=new_repo_directory, _timeout=60)

    def change_rd_directory(self, new_directory: "str") -> "bool":
        """更改repo和data的根目录"""
        return self('change_rd_directory', new_directory=new_directory, _timeout=120)

    def get_rd_directory(self) -> "str":
        """获取repo和data的根目录"""
        return self('get_rd_directory')

    def get_data_directory(self) -> "str":
        """获取平台数据目录"""
        return self('get_data_directory')

    def get_repo_directory(self) -> "str":
        """获取平台repo目录"""
        return self('get_repo_directory')

    def get_root_directory(self) -> "str":
        """获取平台根目录"""
        return self('get_root_directory')

    def get_total_status(self) -> "List[ProcessMetrics]":
        """获取监控进程列表"""
        return self('get_total_status')

    def get_process_status(self, worker_id: "str") -> "Optional[ProcessMetrics]":
        """获取进程资源信息"""
        return self('get_process_status', worker_id=worker_id)

    def get_system_status(self) -> "ProcessMetrics":
        """获取系统资源信息"""
        return self('get_system_status')
