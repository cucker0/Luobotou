#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ...basic_model import BasicModel
from ...utils import GetChoices
import uuid

class PhysicalMachine(BasicModel):
    """
    物理机
    """
    id = models.UUIDField(uuid.uuid4, primary_key=True, unique=True, verbose_name="id")
    sn = models.CharField(max_length=32, unique=True, verbose_name="序列号")
    asset_id = models.CharField(max_length=128, verbose_name="资产编号")
    model = models.CharField(max_length=64, choices=GetChoices().os_choices(), verbose_name="型号")
    os = models.CharField(max_length=32, choices=GetChoices().os_choices(), verbose_name="操作系统")
