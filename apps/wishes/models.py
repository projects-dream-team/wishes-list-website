# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
import random
import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.db import models
from core.models import BaseModel
from products.models import Product
from users.models import User
from core.models import BaseManager


def generate_slug():
    exists = True
    code = ''
    while exists:
        hash = hashlib.md5()
        from datetime import datetime

        now = datetime.now()
        hash.update(str(random.random()) + now.strftime('%Y-%m-%d %H:%M') + settings.SECRET_KEY)
        code = hash.hexdigest()
        exists = len(Event.objects.filter(slug=code)) > 0
    return code


class EventManager(BaseManager):
    def not_past(self):
        return self.active().filter(date__gte=datetime.date.today())


@python_2_unicode_compatible
class Event(BaseModel):
    name = models.CharField(_('Name'), max_length=50)
    date = models.DateTimeField(_('Date'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'), related_name='wishes_lists')
    slug = models.SlugField(_('Access url'), null=True, blank=True, unique=True)

    objects = EventManager()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def save(self, **kwargs):
        if not self.slug:
            self.slug = generate_slug()
        super(Event, self).save(**kwargs)

    def is_past(self):
        return self.date < timezone.now()
    is_past.boolean = True
    is_past.short_name = _('Is past')

    @property
    def url(self):
        return reverse('wishes:list_detail', kwargs={'code':self.slug})

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Gift(BaseModel):
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='wishes_set')
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='wishes_set')
    reservation_date = models.DateTimeField(_('Reservation date'), null=True, blank=True)
    reserved_by = models.ForeignKey(User, verbose_name=_('Reserved by'), null=True, blank=True)
    reserved_by_anonymous = models.EmailField(_('Reserved by anonymous'), null=True, blank=True)

    class Meta:
        verbose_name = _('Gift')
        verbose_name_plural = _('Gifts')

    def is_reserved(self):
        return self.reserved_by is not None or self.reserved_by_anonymous != ''

    @property
    def is_reserved_property(self):
        return self.is_reserved()

    is_reserved.short_name = _('Is reserved')
    is_reserved.boolean = True

    def __str__(self):
        return unicode(_('Product %(product_name)s is on %(event)s wishes list.') % {'product_name': self.product.name,
                                                                                     'event': self.event.name})


@python_2_unicode_compatible
class EventInvitedFriends(BaseModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='events_invitations')
    friend = models.ForeignKey(User, verbose_name=_('Friend'), related_name="events_invitations")

    class Meta:
        verbose_name = _('Event - invented friend')
        verbose_name_plural = _('Event - invented friends')

    def __str__(self):
        return unicode(_('%(friend)s has been invited to %(event)s event.') % {'friend': self.friend.nick,
                                                                               'event': self.event.name})
