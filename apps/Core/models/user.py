#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ...basic_model import BasicModel

class User(BasicModel):
    """
    用户，包含各种系统用户
    """
    name = models.CharField(max_length=64, verbose_name="用户名")
    global_id = models.CharField(max_length=36, verbose_name="全局ID")
    password = models.CharField(max_length=64, verbose_name="密码")
    role = models.CharField(max_length=64, verbose_name="角色")
    status = models.CharField(max_length=6, verbose_name="用户状态")
    password_expire = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="密码过期时间")
    user_expire = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="用户过期时间")
    ssh_key_type = models.CharField(max_length=16, verbose_name="ssh key加密算法类型")
    ssh_private_key = models.CharField(max_length=255, verbose_name="ssh私钥")
    ssh_public_key = models.CharField(max_length=255, verbose_name="ssh公钥")
    secret_id = models.CharField(max_length=64, verbose_name="安全访问ID(如腾讯的CAM 、阿里的accessKeys)")
    secret_key = models.CharField(max_length=64, verbose_name="安全访问key")
    otp_secret_key = models.CharField(max_length=64, verbose_name="OTP一次性密码的安全key")
    other_info = models.CharField(max_length=255, verbose_name="其他信息")
