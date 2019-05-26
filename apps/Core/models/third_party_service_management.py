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

class ThirdPartyServiceManagement(BasicModel):
    """
    第三方服务管理信息
    """
    id = models.CharField(max_length=36, default=generate_id.third_party_service_management, primary_key=True)
    name = models.CharField(max_length=64, verbose_name="平台/服务名")
    management_info = models.CharField(max_length=512, verbose_name="关联User 表用户的ID(json)")
    other_info = models.CharField(max_length=255, verbose_name="其他信息")