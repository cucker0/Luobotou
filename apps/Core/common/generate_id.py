#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

# 生成自定义ID(36位长的字符串)

import uuid

def _gen_id(prefix="000"):
    """
    生成自定义id
    :param prefix: 前缀标识
    :return:
    """
    prefix = str(prefix).strip().lower()
    if len(prefix) > 3:
        prefix = prefix[0:3] + ','
    elif len(prefix) >= 1:
        prefix = prefix.zfill(3) + ','
    else:
        prefix = "000,"

    uuid_filter = ''.join(str(uuid.uuid4()).split('-'))
    id = "%s%s" %(prefix, uuid_filter)
    return id

def basic_config():
    """
    Orgin id
    :return:
    """
    prefix = "001"
    id = _gen_id(prefix)
    return id

def cabinet():
    """
    Cabinet id
    :return:
    """
    prefix = "002"
    id = _gen_id(prefix)
    return id

def ip_pool():
    """
    IpPool id
    :return:
    """
    prefix = "003"
    id = _gen_id(prefix)
    return id

def organization():
    """
    Organization id
    :return:
    """
    prefix = "004"
    id = _gen_id(prefix)
    return id

def origin():
    """
    Origin id
    :return:
    """
    prefix = "005"
    id = _gen_id(prefix)
    return id

def port_pool():
    """
    PortPool id
    :return:
    """
    prefix = "006"
    id = _gen_id(prefix)
    return id

def user():
    """
    User id
    :return:
    """
    prefix = "007"
    id = _gen_id(prefix)
    return id

def physical_machine():
    """
    PhysicalMachine id
    :return:
    """
    prefix = "008"
    id = _gen_id(prefix)
    return id

def cpu_info_template():
    """
    CpuInfoTemplate id
    :return:
    """
    prefix = "009"
    id = _gen_id(prefix)
    return id

def memory_info_template():
    """
    MemoryInfoTemplate id
    :return:
    """
    prefix = "010"
    id = _gen_id(prefix)
    return id

def disk_info_template():
    """
    DiskInfoTemplate id
    :return:
    """
    prefix = "011"
    id = _gen_id(prefix)
    return id

def server():
    """
    Server id
    :return:
    """
    prefix = "012"
    id = _gen_id(prefix)
    return id

def network_device():
    """
    NetworkDevice id
    :return:
    """
    prefix = "013"
    id = _gen_id(prefix)
    return id

def application():
    """
    Application id
    :return:
    """
    prefix = "014"
    id = _gen_id(prefix)
    return id

def app_instance():
    """
    AppInstance id
    :return:
    """
    prefix = "015"
    id = _gen_id(prefix)
    return id

def third_party_service_management():
    """
    ThirdPartyServiceManagement id
    :return:
    """
    prefix = "016"
    id = _gen_id(prefix)
    return id

def ssl_certificate():
    """
    ThirdPartyServiceManagement id
    :return:
    """
    prefix = "017"
    id = _gen_id(prefix)
    return id

def office_dvice():
    """
    OfficeDvice id
    :return:
    """
    prefix = "018"
    id = _gen_id(prefix)
    return id

def manufacturer():
    """
    Manufacturer id
    :return:
    """
    prefix = "019"
    id = _gen_id(prefix)
    return id

def maintenance_and_bugrecord():
    """
    MaintenanceAndBugRecord id
    :return:
    """
    prefix = "020"
    id = _gen_id(prefix)
    return id