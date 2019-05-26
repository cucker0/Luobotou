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

class Manufacturer(BasicModel):
    """
    厂商
    """
    id = models.CharField(max_length=36, default=generate_id.manufacturer, primary_key=True)
    name = models.CharField(max_length=32, unique=True, verbose_name="厂商名称")
    overview = models.CharField(max_length=255, null=True, blank=True, verbose_name="厂商概况")
    website = models.CharField(max_length=128, null=True, blank=True, verbose_name="网址")
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name="地址")
    contact_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="联系信息(json)")