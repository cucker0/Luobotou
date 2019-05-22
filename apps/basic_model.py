#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from django.db import models

class BasicModel(models.Model):
    """
    基础Model
    """
    note = models.CharField(max_length=255, null=True, blank=True, default="", verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="更新时间")