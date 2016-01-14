# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

@admin.register(SiteSettings)
class SettingsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        model = self.model
        obj, created = model.objects.get_or_create(id=1)
        id = str(obj.id)
        return super(SettingsAdmin, self).change_view(request, id)