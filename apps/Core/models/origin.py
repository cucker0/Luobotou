#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ..common.basic_model import BasicModel
from ..common import generate_id

class Origin(BasicModel):
    """
    机房
    """
    id = models.CharField(max_length=36, default=generate_id.origin, primary_key=True)
    name = models.CharField(max_length=64, verbose_name="机房名")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="地址")
    type = models.SmallIntegerField(default=0, verbose_name="机房类型(smallint)")
    bandwidth = models.IntegerField(default=0, verbose_name="带宽(int)，单位:Mbps")
    network_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="网络信息(json)")
    contact_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="联系信息(json)")

