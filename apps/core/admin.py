# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
