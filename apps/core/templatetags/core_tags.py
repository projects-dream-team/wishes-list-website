# coding: utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.template import Library

from core.models import *


''
register = Library()


@register.assignment_tag()
def get_site_settings():
    return SiteSettings.objects.get_settings()

@register.assignment_tag()
def get_facebook_app_id():
    return SiteSettings.objects.get_settings().facebook_app_id
