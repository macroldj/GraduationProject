from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models

# Create your models here.


class book(models.Model):
    name = models.CharField(max_length=20, verbose_name="书名")
    auther = models.CharField(max_length=10, verbose_name="作者")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name