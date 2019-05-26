from django.db import models
from Core.common.basic_model import BasicModel
from Core.common import generate_id
from Core.models.cabinet import Cabinet

# Create your models here.

class NetworkDevice(BasicModel):
    """
    网络设备
    """
    id = models.CharField(max_length=36, default=generate_id.network_device, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name="设备名")
    type = models.CharField(max_length=64, verbose_name="设备类型")
    model = models.CharField(max_length=64, null=True, blank=True, verbose_name="型号")
    form_factor = models.CharField(max_length=32, null=True, blank=True, verbose_name="外形规格")
    firmware = models.CharField(max_length=64, null=True, blank=True, verbose_name="固件型号")
    port_info = models.CharField(max_length=5120, null=True, blank=True, verbose_name="端口信息(json)")
    management_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="远程管理信息(json)")
    cabinet = models.ForeignKey(Cabinet, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="所在机柜")
    location = models.CharField(max_length=128, null=True, blank=True, verbose_name="位置")
    online_time = models.DateTimeField(auto_now_add=True, verbose_name="上架时间")
    offline_time = models.DateTimeField(auto_now_add=True, verbose_name="下架时间")
    status = models.CharField(max_length=8, default="oneline" ,verbose_name="状态")
    purchase_date = models.DateField(auto_now_add=True, verbose_name="购买日期")
    warranty_info = models.CharField(max_length=512, null=True, blank=True, verbose_name="保修信息")
    other_info = models.CharField(max_length=2048, null=True, blank=True, verbose_name="其他信息")