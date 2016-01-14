# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxLengthValidator
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.db import models
from core.models import BaseModel, BaseManager
from core.utils import upload_file_name
from users.models import User


@python_2_unicode_compatible
class Shop(BaseModel):
    name = models.CharField(_('Name'), max_length=50)
    url = models.URLField(_('Url'))

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.name


class ProductManager(BaseManager):
    def shop_products(self):
        return self.active().exclude(shop__isnull=True)


@python_2_unicode_compatible
class Product(BaseModel):
    name = models.CharField(_('Name'), max_length=100)
    url = models.URLField(_('Url'), null=True, blank=True)
    description = models.TextField(_('Description'), validators=[MaxLengthValidator(300)], null=True, blank=True)
    image = models.ImageField(_('Image'), null=True, blank=True, upload_to=upload_file_name)
    shop = models.ForeignKey(Shop, verbose_name=_('Shop'), related_name='products', null=True, blank=True)
    owner = models.ForeignKey(User, verbose_name=_('Owner'), related_name='user_products', null=True, blank=True)

    objects = ProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def has_image(self):
        return self.image != ''

    has_image.boolean = True
    has_image.short_name = _('Has image')

    def __str__(self):
        return self.name
