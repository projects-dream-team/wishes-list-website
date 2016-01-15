# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from rest_framework import fields, serializers, filters
from core.exceptions import EmailServiceUnavailable
from django.utils.translation import ugettext_lazy as _
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def create(self, validated_data):
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        validated_data['is_active'] = False
        user = super(UserSerializer, self).create(validated_data)
        code = UserCode.objects.create_code(user=user, type=UserCode.ACCOUNT_REGISTRATION,
                                            override=False)
        print code
        print user.email
        request = self.context.get("request")
        print request
        url_tuple = (request.META['HTTP_HOST'], reverse('users:activate', args=(code.code,)))
        try:
            email_message = "Welcome in wishes list! \n\n Use this link to complete registration process \n %s%s" % url_tuple
            send_mail(_('Account registration'), email_message, 'projects.dream.team@gmail.com', [user.email, ])
        except:
            raise EmailServiceUnavailable()
        return user


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship


class UserCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCode
