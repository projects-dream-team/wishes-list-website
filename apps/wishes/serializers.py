# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import fields, serializers, filters
from .models import *


class EventSerializer(serializers.ModelSerializer):
    gifts = serializers.JSONField(write_only=True)

    class Meta:
        model = Event

    def create(self, validated_data):
        gifts = validated_data.pop('gifts')
        event = super(EventSerializer, self).create(validated_data)
        for gift in gifts:
            gift_id = gift.get('id', None)
            gift_name = gift.get('name', 'nowy produkt')
            gift_url = gift.get('url', '')
            read_only = gift.get('external', True)
            if gift_id is None:
                product = Product.objects.create(id=gift_id)
                created = True
            else:
                created, product = Product.objects.get_or_create(id=gift_id)
            if created or not read_only:
                product.name = gift_name
                product.url = gift_url
                product.save()
            gift = Gift.objects.create(product=product, event=event)
            gift.save();
        return event


class GiftSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True, source='product.name')

    class Meta:
        model = Gift


class EventInvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInvitedFriends
