# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import *
from .serializers import *


class ContactViewSet(CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = ContactMessage.objects.active()
    serializer_class = ContactSerializer


