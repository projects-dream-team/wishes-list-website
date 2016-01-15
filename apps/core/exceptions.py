# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException

class EmailServiceUnavailable(APIException):
    status_code = 503
    default_detail = _('Email service temporarily unavailable, try again later.')
