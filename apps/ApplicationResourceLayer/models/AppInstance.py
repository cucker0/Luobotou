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
from ComputingResourceLayer.models import Server

class AppInstance(BasicModel):
    """
    应用实例
    """
    id = models.CharField(max_length=36, default=generate_id.app_instance, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="实例标识")
    latest_version = models.CharField(max_length=255, null=True, blank=True, verbose_name="版本信息(json)")
    connection_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="对外提供服务的连接信息(json)")
    server = models.ForeignKey(Server, on_delete=models.PROTECT, related_name="app_instance", verbose_name="所在服务器")
    private_parameter = models.CharField(max_length=255, null=True, blank=True, verbose_name="私有参数(json)")