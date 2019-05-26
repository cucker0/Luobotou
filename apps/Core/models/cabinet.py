#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from django.db import models
from ..common.basic_model import BasicModel
from .origin import Origin
from .organization import Organization
from ..common.model_utils import GetChoices
from ..common import generate_id

class Cabinet(BasicModel):
    """
    机柜
    """
    id = models.CharField(max_length=36, default=generate_id.cabinet, primary_key=True)
    name = models.CharField(max_length=64, verbose_name="机柜标识")
    origin = models.ForeignKey(Origin, null=True, blank=True, on_delete=models.PROTECT, verbose_name="所属机房")
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.PROTECT, verbose_name="所属组织")
    form_factor = models.CharField(max_length=32, null=True, blank=True, verbose_name="规格")