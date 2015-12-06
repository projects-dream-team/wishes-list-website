# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'url')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'shop', 'url', 'has_image')
