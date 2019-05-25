from django.db import models
from Core.common.basic_model import BasicModel
from Core.common import generate_id
from PhysicalResourceLayer.models.physical_machine import PhysicalMachine

# Create your models here.

class Server(BasicModel):
    """
    服务器
    """
    id = models.CharField(max_length=36, default=generate_id.server, primary_key=True, unique=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="服务器名")
    type = models.CharField(max_length=64, verbose_name="服务器类型")
    os = models.CharField(max_length=64, verbose_name="操作系统")
    cpu_info = models.CharField(max_length=255, verbose_name="CPU信息(json)")
    memory_info = models.CharField(max_length=5120, verbose_name="内存信息(json)")
    disk_info = models.CharField(max_length=5120, verbose_name="硬盘信息(json)")
    nic_info = models.CharField(max_length=5120, verbose_name="网卡信息(json)")
    management_info = models.CharField(max_length=255, verbose_name="远程管理信息(json)")
    boss_host = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="首领主机，所在宿主机")
    physical_machine = models.ForeignKey(PhysicalMachine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="所在物理机(type为stand_alone和host时需要指定)")
    other_info = models.CharField(max_length=2048, verbose_name="其他信息")