# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import fields, serializers, filters
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship


class UserCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCode
