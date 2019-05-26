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

class IpPool(BasicModel):
    """
    IP池
    """
    id = models.CharField(max_length=36, default=generate_id.ip_pool, primary_key=True)
    ip = models.GenericIPAddressField(verbose_name="IP")
    netmask = models.CharField(max_length=64, null=True, blank=True, verbose_name="子网掩码")
    business_type = models.CharField(max_length=32, null=True, blank=True, verbose_name="业务类型")
    is_ipv6 = models.CharField(max_length=8, default="false", verbose_name="是IPv6")
    is_virtual_ip = models.CharField(max_length=8, default="false", verbose_name="是虚拟IP")
    status = models.CharField(max_length=8, default="false", verbose_name="是在使用状态")
    use_object = models.CharField(max_length=64, null=True, blank=True, verbose_name="使用对象")
    other_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="其他信息")