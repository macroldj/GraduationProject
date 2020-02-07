#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import book


class BookCodeAdmin(object):
    list_display = ['name','auther','mobile', "add_time"]
    model_icon = 'fa fa-book'


xadmin.site.register(book, BookCodeAdmin)
