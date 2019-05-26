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

class CpuInfoTemplate(BasicModel):
    """
    CPU信息模板
    """
    id = models.CharField(max_length=36, default=generate_id.cpu_info_template, primary_key=True)
    model = models.CharField(max_length=64, unique=True, verbose_name="型号")
    brand = models.CharField(max_length=32, verbose_name="品牌")
    number_of_cores = models.SmallIntegerField(null=True, blank=True, verbose_name="核心数(smallint)")
    number_of_threads = models.SmallIntegerField(null=True, blank=True, verbose_name="线程数(smallint)")
    base_frequency = models.FloatField(null=True, blank=True, verbose_name="基本频率(float),单位:GHz")
    max_frequency = models.FloatField(null=True, blank=True, verbose_name="最大睿频频率(float),单位:GHz")
    cache = models.CharField(max_length=64, null=True, blank=True, verbose_name="缓存(json)")
    index = models.SmallIntegerField(null=True, blank=True, verbose_name="序号(smallint)")

class MemoryInfoTemplate(BasicModel):
    """
    内存信息模板
    """
    id = models.CharField(max_length=36, default=generate_id.memory_info_template, primary_key=True)
    model = models.CharField(max_length=64, unique=True, verbose_name="型号")
    brand = models.CharField(max_length=32, verbose_name="品牌")
    type = models.CharField(max_length=16, verbose_name="内存类型")
    capacity = models.IntegerField(verbose_name="容量(int)，单位:GB")
    frequency = models.IntegerField(null=True, blank=True, verbose_name="频率(int)，单位:MHz")
    voltage = models.SmallIntegerField(null=True, blank=True, verbose_name="电压(smallint)，单位:v")
    index = models.SmallIntegerField(null=True, blank=True, verbose_name="序号(smallint)")

class DiskInfoTemplate(BasicModel):
    """
    硬盘信息模样
    """
    id = models.CharField(max_length=36, default=generate_id.disk_info_template, primary_key=True)
    lable = models.CharField(max_length=64, unique=True, verbose_name="标识")
    model = models.CharField(max_length=64, null=True, blank=True, verbose_name="型号")
    brand = models.CharField(max_length=32, verbose_name="品牌")
    type = models.CharField(max_length=32, null=True, blank=True, verbose_name="介质类型(Media Type)")
    capacity = models.IntegerField(verbose_name="容量(int)，单位:GB")
    form_factor = models.CharField(max_length=32, null=True, blank=True, verbose_name="规格")
    interface = models.CharField(max_length=32, null=True, blank=True, verbose_name="接口类型")
    sequential_read = models.IntegerField(null=True, blank=True, verbose_name="最高顺序读取速度(int)，单位:MB/s")
    sequential_write = models.IntegerField(null=True, blank=True, verbose_name="最高顺序写入速度(int)，单位:MB/s")
    random_read = models.IntegerField(null=True, blank=True, verbose_name="最高随机读取速度(int)，单位:IOPS")
    random_write = models.IntegerField(null=True, blank=True, verbose_name="最高随机写入速度(int)，单位:IOPS")
    rotate_speed = models.IntegerField(null=True, blank=True, verbose_name="转速(int)，单位:rpm(转每分钟)")
    index = models.SmallIntegerField(null=True, blank=True, verbose_name="序号(smallint)")