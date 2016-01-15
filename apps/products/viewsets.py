# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from .models import *
from .serializers import *


class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Shop.objects.active()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.active()
    serializer_class = ProductSerializer

