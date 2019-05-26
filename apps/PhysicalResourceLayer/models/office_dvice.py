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

class OfficeDvice(BasicModel):
    """
    办公设备
    """
    id = models.CharField(max_length=36, default=generate_id.office_dvice, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="设备名")
    model = models.CharField(max_length=64, null=True, blank=True, verbose_name="型号")
    location = models.CharField(max_length=128, null=True, blank=True, verbose_name="位置")
    management_info = models.CharField(max_length=512, null=True, blank=True, verbose_name="管理信息")
    other_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="其他信息")