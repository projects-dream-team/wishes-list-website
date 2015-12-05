# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventInvitedFriends)
class EventInvitedAdmin(admin.ModelAdmin):
    pass

@admin.register(Gift)
class EventAdmin(admin.ModelAdmin):
    pass