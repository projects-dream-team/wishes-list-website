# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import fields, serializers, filters
from .models import *
from products.serializers import ProductSerializer


class GiftSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', required=False)
    product_url = serializers.CharField(source='product.url', required=False)
    product_id = serializers.CharField(source='product.id', required=False)

    class Meta:
        model = Gift
        extra_kwargs = {'id': {'read_only': True}, 'event': {'read_only': True}, 'product': {'read_only': True}}


class EventSerializer(serializers.ModelSerializer):
    gifts = GiftSerializer(many=True, source='wishes_set')
    full_url = serializers.SerializerMethodField()

    class Meta:
        model = Event

    def get_full_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.url)

    def create(self, validated_data):
        test = validated_data.get('wishes_set', [])
        print validated_data.get('gifts', [])
        print validated_data.get('wishes_set', [])[0]
        gifts = validated_data.pop('wishes_set', [])
        # event = super(EventSerializer, self).create(validated_data)
        event = Event.objects.create(**validated_data)
        event.save()
        for prod in gifts:
            gift = prod.get('product')
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
            gift.save()
        return event

    def update(self, instance, validated_data):
        gifts = validated_data.pop('wishes_set', [])
        event = instance
        # event = super(EventSerializer, self).create(validated_data)
        event.name = validated_data.get('name', None)
        event.date = validated_data.get('date', None)
        event.save()
        print event
        for prod in gifts:
            gift = prod.get('product')
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
            gift.save()
        return event


class EventInvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInvitedFriends
