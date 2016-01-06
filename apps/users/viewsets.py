# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class FrendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.active()
    serializer_class = FriendshipSerializer