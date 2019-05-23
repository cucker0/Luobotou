#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ..common.basic_model import BasicModel
from ..common.utils import GenId
from ..common.model_utils import GetChoices

class Origin(BasicModel):
    """
    机房
    """
    id = models.CharField(max_length=36, default=GenId().origin(), primary_key=True, unique=True)
    name = models.CharField(max_length=64, verbose_name="机房")
    address = models.CharField(max_length=255, verbose_name="地址")
    type = models.SmallIntegerField(default=0, choices=GetChoices().origin_type_choices(), verbose_name="机房类型")
    bandwidth = models.IntegerField(default=0, verbose_name="带宽(int)，单位:Mbps")
    network_info = models.CharField(max_length=255, verbose_name="网络信息")
    contact_info = models.CharField(max_length=255, verbose_name="联系信息")

