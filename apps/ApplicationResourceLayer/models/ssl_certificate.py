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

class SslCertificate(BasicModel):
    """
    SSL证书
    """
    id = models.CharField(max_length=36, default=generate_id.ssl_certificate, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="证书名标识")
    domain = models.CharField(max_length=64, null=True, blank=True, verbose_name="域名")
    certificate_file = models.CharField(max_length=10240, verbose_name="证书文件")
    certificate_key = models.CharField(max_length=10240, verbose_name="证书私钥(key)")