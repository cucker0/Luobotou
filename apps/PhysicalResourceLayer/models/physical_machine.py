#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ...basic_model import BasicModel
from ...Core.common.model_utils import GetChoices
from ...Core.common.utils import GenId
from ...Core.models.cabinet import Cabinet

class PhysicalMachine(BasicModel):
    """
    物理机
    """
    id = models.CharField(max_length=36, default=GenId().physical_machine(), primary_key=True, unique=True)
    sn = models.CharField(max_length=32, unique=True, verbose_name="序列号")
    asset_id = models.CharField(max_length=128, verbose_name="资产编号")
    model = models.CharField(max_length=64, choices=GetChoices().os_choices(), verbose_name="型号")
    os = models.CharField(max_length=32, choices=GetChoices().os_choices(), verbose_name="操作系统")
    cpu_info = models.CharField(max_length=255, verbose_name="cpu信息")
    memory_info = models.CharField(max_length=5120, verbose_name="内存信息")
    disk_info = models.CharField(max_length=5120, verbose_name="硬盘信息")
    raid_info = models.CharField(max_length=5120, verbose_name="阵列信息")
    nic_info = models.CharField(max_length=1024, verbose_name="网卡信息")
    cabinet = models.ForeignKey(Cabinet)
    online_date = models.DateField(auto_now_add=True, verbose_name="上架时间")
    offline_date = models.DateField(auto_now_add=True, verbose_name="下架时间")
    status = models.CharField(max_length=8, default="true", verbose_name="是在线状态")
    purchase_date = models.DateField(auto_now_add=True, verbose_name="购买日期")
    warranty_info = models.CharField(max_length=512, verbose_name="保修信息")
    express_service_code = models.CharField(max_length=32, verbose_name="快速服务代码(dell产品特有)")
    management_info = models.CharField(max_length=255, verbose_name="远程管理信息")
    other_info = models.CharField(max_length=2048, verbose_name="其他信息")