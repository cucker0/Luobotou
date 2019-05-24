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
    id = models.CharField(max_length=36, default=generate_id.cabinet, primary_key=True, unique=True)
    name = models.CharField(max_length=64, verbose_name="机柜标识")
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT, verbose_name="所属机房")
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="所属组织")
    form_factor = models.CharField(max_length=32, choices=GetChoices().cabinet_form_factor_choices(), verbose_name="规格")