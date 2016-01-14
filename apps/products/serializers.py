# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import fields, serializers, filters
from .models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
