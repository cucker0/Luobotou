#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

mapping = (
    ("000", "default"), # 格式：("3个字符标识", "app名,model名") , 标识名只包括数字跟字母
    ("001", "Core,BasicConfig"),
    ("002", "Core,Cabinet"),
    ("003", "Core,IpPool"),
    ("004", "Core,Organization"),
    ("005", "Core,Origin"),
    ("006", "Core,PortPool"),
    ("007", "Core,User"),
    ("008", "PhysicalResourceLayer,PhysicalMachine"),
    ("009", "PhysicalResourceLayer,CpuInfoTemplate"),
    ("010", "PhysicalResourceLayer,MemoryInfoTemplate"),
    ("011", "PhysicalResourceLayer,DiskInfoTemplate"),
)

def id2model_mapping():
    """
    id标识到model名的映射
    :return:
    """
    m = {}
    for i in mapping:
        m[i[0]] = i[1]

    return m

def model2id_mapping():
    """
    model名到id标识的映射
    :return:
    """
    m = {}
    for i in mapping:
        m[i[1]] = i[1]

    return m
