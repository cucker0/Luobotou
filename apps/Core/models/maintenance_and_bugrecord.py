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

class MaintenanceAndBugRecord(BasicModel):
    """
    维修和BUG记录
    """
    id = models.CharField(max_length=36, default=generate_id.maintenance_and_bugrecord, primary_key=True)
    brief = models.CharField(max_length=128, verbose_name="故障/BUG摘要")
    object = models.CharField(max_length=512, verbose_name="故障/BUG对象")
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="故障/BUG开始时间")
    detaile = models.CharField(max_length=255, null=True, blank=True, verbose_name="故障/BUG祥情")
    type = models.CharField(max_length=32, verbose_name="故障/BUG类型")
    fault_processing = models.TextField(null=True, blank=True, verbose_name="故障/BUG处理")