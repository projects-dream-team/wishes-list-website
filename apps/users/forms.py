# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'is_active', 'is_admin')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class NickForm(forms.ModelForm):
    nick = forms.CharField(error_messages={'unique': _('Given nick is already registered')})

    class Meta:
        model = User
        fields = (
            'nick',
        )


class PasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'password',
        )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_validation.validate_password(password)
        return password


class EmailForm(forms.ModelForm):
    email = forms.EmailField(error_messages={'unique': _('Given email is already registered')})

    class Meta:
        model = User
        fields = (
            'email',
        )