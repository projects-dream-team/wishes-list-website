# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import fields, serializers, filters
from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift


class EventInvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInvitedFriends
