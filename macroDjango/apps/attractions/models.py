from datetime import datetime

from django.db import models

# Create your models here.


class Attractions(models.Model):
    name = models.CharField(max_length=20, verbose_name="景点名称")
    auther = models.CharField(max_length=10, verbose_name="地址")
    mobile = models.CharField(max_length=11, verbose_name="联系电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "景点信息"
        verbose_name_plural = verbose_name