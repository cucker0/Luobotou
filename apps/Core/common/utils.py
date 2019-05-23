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