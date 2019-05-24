#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

import os

if __name__ != '__main__':
    exit()

# 加载django项目的配置信息
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Luobotou.settings') # 就在manage.py 文件中第8行
# 导Django 并 启动Django项目
import django
django.setup()

from Core.models.basic_config import BasicConfig

BasicConfig.objects.create(
    name='os_choices',
    display='os类型',
    category='基本',
    key='os_choices',
    value="""{
    "data":[
        {"val":"centos6.6", "display":"CentOS 6.6"},
        {"val":"centos6.7", "display":"CentOS 6.7"},
        {"val":"centos7.6", "display":"CentOS 7.6"},
        {"val":"windows2019", "display":"Windows Server 2019"},
        {"val":"windows2016", "display":"Windows Server 2016"},
        {"val":"windows2016r2", "display":"Windows Server 2016 R2"},
        {"val":"windows2012", "display":"Windows Server 2012"},
        {"val":"windows2012r2", "display":"Windows Server 2012 R2"},
        {"val":"windows2008", "display":"Windows Server 2008"},
        {"val":"windows2008r2", "display":"Windows Server 2008 R2"},
        {"val":"windows2003", "display":"Windows Server 2003"},
        {"val":"windows2003r2", "display":"Windows Server 2003 R2"},
        {"val":"windows10", "display":"Windows 10"},
        {"val":"windows8", "display":"Windows 8"},
        {"val":"windows8.1", "display":"Windows 8.1"},
        {"val":"windows7", "display":"Windows 7"},
        {"val":"windows_xp", "display":"Windows XP"},
    ]
} 
""",
    index=0,
)