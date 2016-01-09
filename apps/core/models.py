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

class TeamMember(BaseModel):
    name = models.CharField(_('Name'),max_length=100)
    description = models.TextField(_('Description'),null=True,blank=True)
    image = models.ImageField(_('Image'),null=True,blank=True)

    class Meta:
        verbose_name = _('Team member')
        verbose_name_plural = _('Team member')

    def __str__(self):
        return self.name