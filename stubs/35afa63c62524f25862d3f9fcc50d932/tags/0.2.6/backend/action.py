# Python Action Stub
#
# Generated at: 2026-03-31 07:51:20
# SDK Version: 0.13.3
# App Name: uvapp_srv_loggingworker
# App Version: 0.2.6
# Author: RIGOL Technology
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayInfo, AppRuntimeConfig


class AppRead(BaseModel):
    """读取应用的响应模型."""

    app_id: "str"
    app_name: "str"


class LogPagination(BaseModel):
    """日志分页参数模型"""

    page_size: "int"
    current_page: "int"


class LogFilter(BaseModel):
    """日志过滤条件."""

    app_id: "Optional[str]"
    lvl: "Optional[str]"
    ctx: "Optional[str]"
    start_ts: "Optional[float]"
    end_ts: "Optional[float]"
    search_mode: "Optional[Any]" = 'fuzzy'
    keywords: "Optional[List[str]]"
    search_logic: "Optional[Any]" = 'OR'
    search_fields: "Optional[List[Any]]" = ['ctx']
    exclude_keywords: "Optional[List[str]]"
    code: "Optional[str]"
    min_id: "Optional[int]"
    max_id: "Optional[int]"


class LogExport(BaseModel):
    """日志导出的请求模型."""

    export_type: "Any" = 'json'


class LogRead(BaseModel):
    """读取日志的响应模型."""

    log_id: "int"
    app_id: "str"
    app_name: "Optional[str]"
    lvl: "str"
    code: "str"
    ctx: "str"
    ts: "str"


class AppDelete(BaseModel):
    """删除应用的请求模型."""

    app_ids: "List[str]"


class LogPaginationRead(BaseModel):
    """日志分页响应模型"""

    total: "int"
    page_size: "int"
    current_page: "int"
    logs: "List[LogRead]" = ('_class_ref_', 'list')


class LogDelete(BaseModel):
    """删除日志的请求模型."""

    log_ids: "List[int]"


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = '35afa63c62524f25862d3f9fcc50d932', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'get_apps': List[AppRead],
            'get_logs': LogPaginationRead,
            'filter_logs': LogPaginationRead,
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

    def get_apps(self) -> "List[AppRead]":
        """获取所有存储过日志的应用id和应用名称"""
        return self('get_apps')

    def delete_app(self, app_info: "AppDelete") -> "bool":
        """删除app信息,同时删除外键关联的日志"""
        return self('delete_app', app_info=app_info)

    def delete_log(self, log_info: "LogDelete") -> "bool":
        """删除多条日志"""
        return self('delete_log', log_info=log_info)

    def get_logs(self, log_pagination: "LogPagination") -> "LogPaginationRead":
        """获取所有已经存储的日志"""
        return self('get_logs', log_pagination=log_pagination)

    def filter_logs(self, log_filter: "LogFilter", log_pagination: "LogPagination") -> "LogPaginationRead":
        """筛选已经存储的日志"""
        return self('filter_logs', log_filter=log_filter, log_pagination=log_pagination)

    def clear_all(self) -> "bool":
        """清空数据库中所有内容"""
        return self('clear_all')

    def export_all(self, export_info: "LogExport") -> "Any":
        """导出所有日志"""
        return self('export_all', export_info=export_info, _timeout=300)
