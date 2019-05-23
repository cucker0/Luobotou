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

class BasicConfig(BasicModel):
    """
    基本配置
    """
    id = models.CharField(max_length=36, default=GenId().basic_config(), primary_key=True, unique=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="配置名称(字母与_组成)")
    display = models.CharField(max_length=64, unique=True, verbose_name="显示配置名称")
    category = models.CharField(max_length=64, verbose_name="类别")
    key = models.CharField(max_length=64, verbose_name="key")
    value = models.CharField(max_length=5120, verbose_name="值")
    index = models.IntegerField(verbose_name="序号", unique=True)