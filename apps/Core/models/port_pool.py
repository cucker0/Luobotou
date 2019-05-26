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

class PortPool(BasicModel):
    """
    port池
    """
    id = models.CharField(max_length=36, default=generate_id.port_pool, primary_key=True)
    port = models.IntegerField(verbose_name="端口(int)")
    protocol = models.CharField(max_length=32, default="tcp", verbose_name="协议")
    use_object = models.CharField(max_length=64, null=True, blank=True, verbose_name="使用对象")
    status = models.CharField(max_length=8, default="false", verbose_name="是在使用状态")

    class Meta:
        # 联合约束
        unique_together = ["port", "protocol"]


