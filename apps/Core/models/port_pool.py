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

class PortPool(BasicModel):
    """
    port池
    """
    id = models.CharField(max_length=36, default=GenId().port_pool(), primary_key=True, unique=True)
    port = models.IntegerField(verbose_name="端口")
    protocol = models.CharField(max_length=32, verbose_name="协议")
    global_id = models.CharField(max_length=36, verbose_name="全局ID")
    use_object = models.CharField(max_length=64, verbose_name="使用对象")
    status = models.CharField(max_length=8, verbose_name="是在使用状态")

    class Meta:
        # 联合约束
        unique_together = ["port", "protocol"]


