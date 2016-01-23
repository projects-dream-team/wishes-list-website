# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
# Register your models here.

class GiftInline(admin.TabularInline):
    model = Gift
    pass
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'owner', 'is_past')
    list_filter = ('date', 'owner',)
    search_fields = ('name', 'owner')
    inlines = (GiftInline,)

@admin.register(EventInvitedFriends)
class EventInvitedAdmin(admin.ModelAdmin):
    pass


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('event', 'product', 'is_reserved', 'reservation_date',)
    list_filter = ('event', 'product', 'reservation_date',)
    search_fields = ('event', 'product')
