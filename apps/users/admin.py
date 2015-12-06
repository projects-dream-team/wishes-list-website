# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import User, Friendship
from django.utils.translation import ugettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('nick', 'email', 'is_active', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('nick', 'email', 'mobile_app_uuid')}),
        (_('Permissions'), {'fields': ('is_admin', 'is_active')}),
        (_('Important dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nick', 'email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email', 'nick')
    ordering = ('email', 'nick')
    filter_horizontal = ()

    def get_readonly_fields(self, request, obj=None):
        fields = tuple(super(UserAdmin, self).get_readonly_fields(request, obj))
        return fields

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    pass