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
from Core.models.cabinet import Cabinet # 这里因为在settings.py已经设置 项目根路径/Luobotou/apps加入了sys.path列表中，
                                        # 所以直接从app名开始写，写apps.Core.common.basic_model反而报错：
                                        # RuntimeError: Model class apps.Core.models.cabinet.Cabinet doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
class PhysicalMachine(BasicModel):
    """
    物理机
    """
    id = models.CharField(max_length=36, default=generate_id.physical_machine, primary_key=True)
    sn = models.CharField(max_length=32, unique=True, verbose_name="序列号")
    asset_id = models.CharField(max_length=128, null=True, blank=True, verbose_name="资产编号")
    model = models.CharField(max_length=64, verbose_name="型号")
    os = models.CharField(max_length=32, null=True, blank=True, verbose_name="操作系统")
    cpu_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="cpu信息(json)")
    memory_info = models.CharField(max_length=5120, null=True, blank=True, verbose_name="内存信息(json)")
    disk_info = models.CharField(max_length=5120, null=True, blank=True, verbose_name="硬盘信息(json)")
    raid_info = models.CharField(max_length=5120, null=True, blank=True, verbose_name="阵列信息(json)")
    nic_info = models.CharField(max_length=1024, null=True, blank=True, verbose_name="网卡信息(json)")
    cabinet = models.ForeignKey(Cabinet, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="所在机柜")
    online_date = models.DateField(auto_now_add=True, verbose_name="上架时间")
    offline_date = models.DateField(auto_now_add=True, verbose_name="下架时间")
    status = models.CharField(max_length=16, default="true", verbose_name="是在线状态")
    purchase_date = models.DateField(auto_now_add=True, verbose_name="购买日期")
    warranty_info = models.CharField(max_length=512, null=True, blank=True, verbose_name="保修信息(json)")
    express_service_code = models.CharField(max_length=32, null=True, blank=True, verbose_name="快速服务代码(dell产品特有)")
    management_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="远程管理信息(json)")
    other_info = models.CharField(max_length=2048, null=True, blank=True, verbose_name="其他信息")
