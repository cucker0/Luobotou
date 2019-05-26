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


class Stock(BasicModel):
    """
    库存
    """
    id = models.CharField(max_length=36, default=generate_id.stock, primary_key=True)
    type = models.CharField(max_length=32, verbose_name="类型")
    model = models.CharField(max_length=32, verbose_name="型号")
    sn = models.CharField(max_length=128, null=True, blank=True, verbose_name="SN序列号")
    basic_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="基本信息")
    checkin_time = models.DateTimeField(auto_now_add=True, verbose_name="入库登录时间")
    checkout_time = models.DateTimeField(auto_now_add=True, verbose_name="出库时间")
    other_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="其他信息")
