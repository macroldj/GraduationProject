#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import city


class BookCodeAdmin(object):
    list_display = ['name','auther','mobile', "add_time"]
    model_icon = 'fa fa-city'


xadmin.site.register(city, BookCodeAdmin)
