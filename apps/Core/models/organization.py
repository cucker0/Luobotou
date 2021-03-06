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

class Organization(BasicModel):
    """
    组织
    """
    id = models.CharField(max_length=36, default=generate_id.organization, primary_key=True)
    name = models.CharField(max_length=128, verbose_name="组织名称")
    parent_id = models.IntegerField(default=None, null=True, blank=True, verbose_name="父组织ID")


























