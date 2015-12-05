# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.db import models
from core.models import BaseModel
from products.models import Product
from users.models import User


@python_2_unicode_compatible
class Event(BaseModel):
    name = models.CharField(_('Name'), max_length=50)
    date = models.DateTimeField(_('Date'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'), related_name='wishes_lists')
    access_code = models.SlugField(_('Url'))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Gift(BaseModel):
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='wishes_set')
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='wishes_set')
    reservetion_date = models.DateTimeField(_('Reservation date'))
    reserved_by = models.ForeignKey(User, verbose_name=_('Reserved by'), null=True, blank=True)
    reserved_by_anonymous = models.EmailField(_('Reserved by anonymous'), null=True, blank=True)

    class Meta:
        verbose_name = _('Gift')
        verbose_name_plural = _('Gifts')

    def __str__(self):
        return unicode(_('Product %(prduct_name)s is on %(event)s wishes list.') % {'product_name': self.product.name,
                                                                                    'event': self.event.name})


@python_2_unicode_compatible
class EventInventedFriends(BaseModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='events_invitations')
    friend = models.ForeignKey(User, verbose_name=_('Friend'), related_name="events_invitations")

    class Meta:
        verbose_name = _('Event - invented friend')
        verbose_name_plural = _('Event - invented friends')

    def __str__(self):
        return self.name
