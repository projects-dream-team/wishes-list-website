# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import mail_admins
from rest_framework import fields, serializers, filters
from core.exceptions import EmailServiceUnavailable
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage

    def create(self, validated_data):
        try:
            from_email = validated_data.get('email')
            message = validated_data.get('message')
            email_message = "WishesList contact email from %s \n message: \n %s"  % (from_email, message)
            mail_admins(validated_data.get('subject'), email_message)
        except:
            raise EmailServiceUnavailable()
        return super(ContactSerializer, self).create(validated_data)