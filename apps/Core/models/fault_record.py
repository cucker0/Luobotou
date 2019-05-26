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


class FaultRecord(BasicModel):
    """
    事故记录
    """
    id = models.CharField(max_length=36, default=generate_id.fault_record, primary_key=True)
    brief = models.CharField(max_length=128, verbose_name="事故摘要")
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    status = models.CharField(max_length=16, null=True, blank=True, verbose_name="状态")
    center = models.CharField(max_length=64, null=True, blank=True, verbose_name="事故处理中心")
    participant_organization = models.CharField(max_length=2048, null=True, blank=True, verbose_name="参与人组织架构(json)")
    list_and_work_order = models.CharField(max_length=512, null=True, blank=True, verbose_name="待办列表及已提交工单")
    timeline = models.TextField(null=True, blank=True, verbose_name="事故时间线(json)")
