# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WishesConfig(AppConfig):
    name = 'wishes'
    verbose_name = _('Wishes')
