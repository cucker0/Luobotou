#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from Core.common.basic_model import BasicModel # 引用绝对路径，直接从app名开始写，从manage.py运行时这里的顶层包为Core,这里可以通过打印__nanm__来查看
from Core.common import generate_id

# print("__name__: ", __name__)

class BasicConfig(BasicModel):
    """
    基本配置
    """
    id = models.CharField(max_length=36, default=generate_id.basic_config, primary_key=True, unique=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="配置名称(字母与_组成)")
    display = models.CharField(max_length=64, unique=True, verbose_name="显示配置名称")
    category = models.CharField(max_length=64, null=True, blank=True, verbose_name="类别")
    key = models.CharField(max_length=64, null=True, blank=True, verbose_name="key")
    value = models.CharField(max_length=5120, null=True, blank=True, verbose_name="值")
    index = models.IntegerField(null=True, blank=True, verbose_name="序号(int)")