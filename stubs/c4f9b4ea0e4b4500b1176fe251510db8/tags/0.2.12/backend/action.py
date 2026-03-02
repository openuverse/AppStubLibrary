# Python Action Stub
#
# Generated at: 2026-03-02 08:55:26
# SDK Version: 0.12.12
# App Name: Orbit
# App Version: 0.2.12
# Author: RIGOL Technology
# Description: Orbit is a low-code platform for creating custom workflows and automations.
#
# This file is auto-generated. Do not edit manually.

from typing import Any, List, Dict, Optional, Union, Tuple
from pydantic import BaseModel
from uvapi import BaseActionProxy
from uvapi.modules import ActionInfo, AppConfig, AppDisplayConfig, AppDisplayInfo, AppRuntimeConfig


class WorkFlow(BaseModel):
    """工作流数据模型"""

    id: "str"
    name: "str"
    description: "Optional[str]"
    edges: "Optional[List[Any]]"
    icon: "Optional[str]"
    nodes: "Optional[List[Any]]"
    createdAt: "Optional[float]"
    updatedAt: "Optional[float]"


class ProjectDetail(BaseModel):
    """获取工程详情的请求模型."""

    id: "str"


class DeleteInfo(BaseModel):
    """删除文件信息"""

    project_id: "str"
    file_id: "str"
    file_type: "str"


class MetaData(BaseModel):
    """元数据模型."""

    id: "str"
    name: "str"
    description: "str"
    tags: "Optional[str]"
    data_path: "Optional[str]"
    version: "Optional[str]"
    created_at: "Optional[float]"
    updated_at: "Optional[float]"


class UploadInfo(BaseModel):
    """上传文件信息"""

    project_id: "str"
    file_name: "str"
    file_id: "str"
    file: "str"


class ProjectInfo(BaseModel):
    """工程完整信息数据模型"""

    metadata: "Optional[MetaData]"
    workflows: "Optional[List[WorkFlow]]"
    data: "Optional[List[Any]]"
    files: "Optional[List[Any]]"


class TransformInfo(BaseModel):
    """下载文件信息"""

    project_id: "str"
    file_id: "str"


class ProjectRead(BaseModel):
    """读取工程的响应模型."""

    id: "str"
    name: "str"
    description: "str"
    tags: "Optional[str]"
    data_path: "str"
    created_at: "float"
    updated_at: "float"


class DownloadResult(BaseModel):
    """下载文件结果"""

    project_id: "str"
    file_name: "str"
    file_id: "str"
    file: "str"


class ProjectDelete(BaseModel):
    """删除工程的请求模型."""

    id: "str"


class DownloadInfo(BaseModel):
    """下载文件信息"""

    project_id: "str"
    file_id: "str"
    file_type: "str"


class DSLData(BaseModel):
    """DSL数据模型"""

    metadata: "MetaData"
    workflows: "List[WorkFlow]"
    data: "List[Any]"
    files: "List[Any]"


class ActionProxy(BaseActionProxy):
    """Action Proxy for RPC-like calls"""

    def __init__(self, target_id: str = 'c4f9b4ea0e4b4500b1176fe251510db8', service=None):
        super().__init__(target_id, service)
        # 设置每个 action 的返回类型映射
        self._action_return_types = {
            'get_app_config': AppConfig,
            'create_project': ProjectRead,
            'delete_project': Dict[str, str],
            'get_projects': List[ProjectRead],
            'get_project_detail': DSLData,
            'get_project_meta': MetaData,
            'get_project_workflow': List[WorkFlow],
            'update_project_metadata': ProjectRead,
            'update_project_workflow': Dict[str, str],
            'update_project_data': Dict[str, str],
            'upload_static_file': Dict[str, str],
            'delete_file': Dict[str, str],
            'load_project': DSLData,
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

    def create_project(self, project_data: "ProjectInfo") -> "ProjectRead":
        """创建新工程"""
        return self('create_project', project_data=project_data)

    def delete_project(self, project: "ProjectDelete") -> "Dict[str, str]":
        """删除工程"""
        return self('delete_project', project=project)

    def get_projects(self) -> "List[ProjectRead]":
        """获取所有工程列表"""
        return self('get_projects')

    def get_project_detail(self, project: "ProjectDetail") -> "DSLData":
        """获取工程中的DSL"""
        return self('get_project_detail', project=project)

    def get_project_meta(self, project: "ProjectDetail") -> "MetaData":
        """获取工程中的meta信息"""
        return self('get_project_meta', project=project)

    def get_project_workflow(self, project: "ProjectDetail") -> "List[WorkFlow]":
        """获取工程中的工作流信息"""
        return self('get_project_workflow', project=project)

    def get_project_data(self, project: "ProjectDetail") -> "Any":
        """获取工程中的变量信息"""
        return self('get_project_data', project=project)

    def get_project_files(self, project: "ProjectDetail") -> "Any":
        """获取工程中的文件信息"""
        return self('get_project_files', project=project)

    def update_project_metadata(self, project_update: "ProjectInfo") -> "ProjectRead":
        """更新工程信息"""
        return self('update_project_metadata', project_update=project_update)

    def update_project_workflow(self, project_id: "str", project_data: "ProjectInfo") -> "Dict[str, str]":
        """更新工程中的工作流信息"""
        return self('update_project_workflow', project_id=project_id, project_data=project_data)

    def update_project_data(self, project_id: "str", project_data: "ProjectInfo") -> "Dict[str, str]":
        """更新工程中的变量信息"""
        return self('update_project_data', project_id=project_id, project_data=project_data)

    def upload_static_file(self, upload_info: "UploadInfo") -> "Dict[str, str]":
        """上传数据文件"""
        return self('upload_static_file', upload_info=upload_info)

    def delete_file(self, delete_info: "DeleteInfo") -> "Dict[str, str]":
        """删除数据文件"""
        return self('delete_file', delete_info=delete_info)

    def export_project(self, project_id: "str") -> "str":
        """工程数据导出"""
        return self('export_project', project_id=project_id)

    def load_project(self, files: "str") -> "DSLData":
        """工程数据导入"""
        return self('load_project', files=files)

    def download_file(self, download_info: "DownloadInfo") -> "Any":
        """下载指定数据文件"""
        return self('download_file', download_info=download_info)

    def transform_temp_file(self, transform_info: "TransformInfo") -> "Any":
        """临时文件转换为静态文件"""
        return self('transform_temp_file', transform_info=transform_info)
