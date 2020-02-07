from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# 这里我们的项目名称为,所以为platform.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "macroDjango.settings")

# 创建celery应用
app = Celery('macroDjango_celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)