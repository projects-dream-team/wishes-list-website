# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'my_lists/$', views.my_lists, name='my_lists'),
    url(r'list/(?P<code>[A-Za-z0-9-\d]+)/$', views.list_detail, name='list_detail'),
]
