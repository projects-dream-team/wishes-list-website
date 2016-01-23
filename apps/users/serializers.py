# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import render_to_string, get_template
from rest_framework import fields, serializers, filters
from core.exceptions import EmailServiceUnavailable
from django.utils.translation import ugettext_lazy as _
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    url_to_lists = serializers.SerializerMethodField()

    def get_url_to_lists(self, obj):
        return obj.lists_url

    class Meta:
        model = User
        fields = ('id', 'nick', 'email', 'password', 'url_to_lists',)

    def create(self, validated_data):
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        validated_data['is_active'] = False
        user = super(UserSerializer, self).create(validated_data)
        code = UserCode.objects.create_code(user=user, type=UserCode.ACCOUNT_REGISTRATION,
                                            override=False)

        request = self.context.get("request")
        page_url = request.META['HTTP_HOST']
        subject = _('Account registration')
        ctx = {"activate_link": "%s%s" % (page_url, reverse('users:activate', args=(code.code,))), "subject": subject,
               "page_url": page_url, "nick": user.nick}
        email_message = get_template('email/index.html').render(Context(ctx))
        try:
            msg = EmailMessage(subject, email_message, to=[user.email, ], from_email='projects.dream.team@gmail.com')
            msg.content_subtype = 'html'
            msg.send()
        except:
            user.delete()
            raise EmailServiceUnavailable()
        return user


class FriendshipSerializer(serializers.ModelSerializer):
    owner_nick = serializers.CharField(source='owner.nick', read_only=True)
    friend_nick = serializers.CharField(source='friend.nick', read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Friendship

    def get_user(self, obj):
        request = self.context.get("request")
        if request.user == obj.owner:
            return UserSerializer(obj.friend).data
        else:
            return UserSerializer(obj.owner).data


class UserCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCode
