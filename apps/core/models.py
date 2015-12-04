# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

class BaseManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)



class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(_('Modified'), auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(_('Is active'), default=True)

    objects = BaseManager()

    class Meta:
        abstract = True
