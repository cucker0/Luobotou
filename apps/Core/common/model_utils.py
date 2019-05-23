#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
author: song.yanlin
mail: hanxiao2100@qq.com
"""

from ..models.basic_config import BasicConfig

class GetChoices(object):
    """
    从BasicConfig表获取相应的选项
    """

    def _gen_choices(self, search_key):
        """
        生成tuple选项
        如 (('0', 'female'), ('1', 'male'))

        raw_data数据格式示例：
{
    'data': [
        {'val':0, 'display':'电信机房'},
        {'val':1, 'display':'联通机房'},
        {'val':2, 'display':'移动机房'},
        {'val':3, 'display':'BGP机房'},
        {'val':4, 'display':'阿里云'},
        {'val':5, 'display':'腾讯云'}
    ]
}
        """

        try:
            search_key = str(search_key)
            raw_data = BasicConfig.objects.get(name=search_key)  # jsong字符串
            raw_data = eval(raw_data)  # 把raw_data转成字典或列表，这种方法比json要好用，json须要求双引号，且列表最后一个元素后不能有,
            choices = []
            for i in raw_data["data"]:
                choice = []
                choice.append(i["val"])
                choice.append(i["display"])
                choice = tuple(choice)
                choices.append(choice)
            choices = tuple(choices)
        except Exception as e:
            choices = (('', ''),)
        return choices

    def origin_type_choices(self):
        """
        获取 origin type 选项
        :return:
        """
        search_key = "origin_type_choices"
        choices = self._gen_choices(search_key)
        return choices

    def cabinet_form_factor_choices(self):
        """
        获取机柜规格选项
        :return:
        """
        search_key = "cabinet_form_factor_choices"
        choices = self._gen_choices(search_key)
        return choices

    def disk_type_choices(self):
        """
        硬盘介质类型选项
        :return:
        """
        search_key = "disk_type_choices"
        choices = self._gen_choices(search_key)
        return choices

    def memory_type_choices(self):
        """
        内存类型选项
        :return:
        """
        search_key = "memory_type_choices"
        choices = self._gen_choices(search_key)
        return choices

    def disk_form_factor_choices(self):
        """
        硬盘规格选项
        :return:
        """
        search_key = "disk_form_factor_choices"
        choices = self._gen_choices(search_key)
        return choices

    def disk_interface_choices(self):
        """
        硬盘接口类型选项
        :return:
        """
        search_key = "disk_interface_choices"
        choices = self._gen_choices(search_key)
        return choices

    def os_choices(self):
        """
        OS选项
        :return:
        """
        search_key = "os_choices"
        choices = self._gen_choices(search_key)
        return choices

    def physical_machine_model_choices(self):
        """
        物理机型号选项
        :return:
        """
        search_key = "physical_machine_model_choices"
        choices = self._gen_choices(search_key)
        return choices