# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from .models import *
from .serializers import *


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.active()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('owner',)


class GiftViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Gift.objects.active()
    serializer_class = GiftSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('event',)


class EventInvitedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = EventInvitedFriends.objects.active()
    serializer_class = EventInvitedFriendsSerializer


class FriendsEventsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.active()
    serializer_class = EventSerializer

    def get_queryset(self):
        return self.queryset.filter(events_invitations__friend=self.request.user)