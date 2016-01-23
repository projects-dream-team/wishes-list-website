# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'activate/(?P<code>[A-Za-z0-9\d]+)/', views.activate, name='activate'),
        url(r'login/$', views.login, name='login'),
        url(r'register/$', views.register, name='register'),
        url(r'my_profile/$', views.my_profile, name='my_profile'),
        url(r'search_friends/$', views.search_friends, name='search_friends'),
        url(r'friends/$', views.my_friends, name='my_friends'),

]
