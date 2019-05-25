#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import uuid

class GenId(object):
    """
     生成自定义id
    """

    def _gen_id(self, prefix="000"):
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

    def basic_config(self):
        """
        Orgin id
        :return:
        """
        prefix = "001"
        id = self._gen_id(prefix)
        return id

    def cabinet(self):
        """
        Cabinet id
        :return:
        """
        prefix = "002"
        id = self._gen_id(prefix)
        return id

    def ip_pool(self):
        """
        IpPool id
        :return:
        """
        prefix = "003"
        id = self._gen_id(prefix)
        return id

    def organization(self):
        """
        Organization id
        :return:
        """
        prefix = "004"
        id = self._gen_id(prefix)
        return id

    def origin(self):
        """
        Origin id
        :return:
        """
        prefix = "005"
        id = self._gen_id(prefix)
        return id

    def port_pool(self):
        """
        PortPool id
        :return:
        """
        prefix = "006"
        id = self._gen_id(prefix)
        return id

    def user(self):
        """
        User id
        :return:
        """
        prefix = "007"
        id = self._gen_id(prefix)
        return id

    def physical_machine(self):
        """
        PhysicalMachine id
        :return:
        """
        prefix = "008"
        id = self._gen_id(prefix)
        return id

def make_aware_datetime(strptime, time_zone=None):
    """
    把字符串时间转换成aware datetime(带时区信息格式的时间)
    :param strptime: 字符串时间(str)，如"2019-05-25 17:37:23"
    :param time_zone: 时区(str)，如"Asia/Shanghai" , "UTC"
    :return: aware_datetime
    """
    from django.utils import timezone
    import pytz
    import datetime

    naive_datetime = datetime.datetime.strptime(strptime, '%Y-%m-%d %H:%M:%S')

    if time_zone:
        try:
            tz = pytz.timezone(time_zone)
        except Exception as e:
            tz = pytz.timezone("UTC")
        aware_datetime = timezone.make_aware(naive_datetime, timezone=tz)
    else: # 使用settings中设置的TIME_ZONE
        aware_datetime = timezone.make_aware(naive_datetime)
    return aware_datetime

def make_aware_datetime_v2(strptime, time_zone=None):
    """
    把字符串时间转换成aware datetime(带时区信息格式的时间) v2
    :param strptime: 字符串时间(str)，如"2019-05-25 17:37:23"
    :param time_zone: 时区(str)，如"Asia/Shanghai" , "UTC"
    :return: aware_datetime
    """
    import pytz
    import datetime
    from django.conf import settings

    naive_datetime = datetime.datetime.strptime(strptime, '%Y-%m-%d %H:%M:%S')
    print("naive_datetime", naive_datetime)
    if time_zone:
        try:
            tz = pytz.timezone(time_zone)
        except Exception as e:
            tz = pytz.timezone("UTC")
    else: # 使用settings中设置的TIME_ZONE
        # tz = pytz.timezone("UTC")
        tz = pytz.timezone(settings.TIME_ZONE)
    aware_datetime = naive_datetime.replace(tzinfo=tz)
    return aware_datetime

