# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import fields, serializers, filters
from .models import *
from products.serializers import ProductSerializer


class GiftSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', required=False)
    product_url = serializers.CharField(source='product.url', required=False, allow_null=True)
    product_id = serializers.CharField(source='product.id', required=False)

    class Meta:
        model = Gift
        extra_kwargs = {'id': {'required': False}, 'event': {'required': False}, 'product': {'required': False}, 'product_url':{'required': False}}

    def get_validation_exclusions(self):
        exclusions = super(GiftSerializer, self).get_validation_exclusions()
        return exclusions + ['product_url']

class EventSerializer(serializers.ModelSerializer):
    gifts = GiftSerializer(many=True, source='wishes_set')
    full_url = serializers.SerializerMethodField()

    class Meta:
        model = Event

    def get_full_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.url)

    def create(self, validated_data):
        gifts = validated_data.pop('wishes_set', [])
        event = Event.objects.create(**validated_data)
        event.save()
        for prod in gifts:
            gift = prod.get('product')
            if gift is not None:
                gift_name = gift.get('name', 'nowy produkt')
                gift_url = gift.get('url', '')
                read_only = gift.get('external', True)

                product, created = Product.objects.get_or_create(name=gift_name, owner=event.owner)
                product.name = gift_name
                product.url = gift_url
                product.save()
                gift = Gift.objects.create(product=product, event=event)
                gift.save()
        return event

    def update(self, instance, validated_data):
        gifts = validated_data.pop('wishes_set', [])
        event = instance
        event.name = validated_data.get('name', None)
        event.date = validated_data.get('date', None)
        event.save()
        event.wishes_set.all().delete()
        for prod in gifts:
            product_dict = prod.get('product')
            if isinstance(product_dict,dict):
                product, created = Product.objects.get_or_create(name=product_dict.get('name'), owner=event.owner)
                product.url = product_dict.get('url','#')
                product.save()
            else:
                product = product_dict
            if product is not None:
                gift, created = Gift.objects.get_or_create(product=product, event=event)
                gift.save()
        return event


class EventInvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInvitedFriends
