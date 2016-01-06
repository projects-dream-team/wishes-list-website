# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from .models import *
from .serializers import *


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.active()
    serializer_class = EventSerializer


class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.active()
    serializer_class = GiftSerializer


class EventInvitedViewSet(viewsets.ModelViewSet):
    queryset = EventInvitedFriends.objects.active()
    serializer_class = EventInvitedFriendsSerializer