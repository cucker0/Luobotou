#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from Core.common.basic_model import BasicModel
from Core.common import generate_id

class Application(BasicModel):
    """
    应用列表
    """
    id = models.CharField(max_length=36, primary_key=True, default=generate_id.application)
    name = models.CharField(max_length=64, verbose_name="应用名")
    stable_version = models.CharField(max_length=128, null=True, blank=True, verbose_name="稳定版本(json)")
    latest_version = models.CharField(max_length=128, null=True, blank=True, verbose_name="最新版本(json)")
    project_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="对应项目信息")
    jenkins_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="jenkins相关信息(json)，如任务名，作业URL")
    group_info = models.CharField(max_length=512, null=True, blank=True, verbose_name="分组信息(json")
    start_parameter = models.CharField(max_length=255, null=True, blank=True, verbose_name="启动参数信息(json)")
    deployment_path = models.CharField(max_length=128, null=True, blank=True, verbose_name="部署路径")
    log_path = models.CharField(max_length=128, null=True, blank=True, verbose_name="日志路径")
    leader_info = models.CharField(max_length=128, null=True, blank=True, verbose_name="负责人信息(json)")
    dependent_service = models.CharField(max_length=128, null=True, blank=True, verbose_name="依赖服务(json)")
    connecting_basic_service_info = models.CharField(max_length=512, null=True, blank=True, verbose_name="连接基础服务信息(json)")
    status = models.CharField(max_length=16, default="start", verbose_name="应用在线状态")
    online_time = models.DateTimeField(auto_now_add=True, verbose_name="上架时间")
    offline_time = models.DateTimeField(auto_now_add=True, verbose_name="下架回收时间")
    bug_record_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="bug记录(json)")