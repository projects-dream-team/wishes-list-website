# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MaxLengthValidator
from core.utils import upload_file_name


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

@python_2_unicode_compatible
class TeamMember(BaseModel):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    image = models.ImageField(_('Image'), null=True, blank=True)

    class Meta:
        verbose_name = _('Team member')
        verbose_name_plural = _('Team member')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class ContactMessage(BaseModel):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100)
    subject = models.CharField(_('Subject'), max_length=100)
    message = models.TextField(_('Message'), validators=[MaxLengthValidator(2000)])
    read = models.BooleanField(_('Read'), default=False)

    class Meta:
        verbose_name = _('Contact message')
        verbose_name_plural = _('Contact messages')

    def __str__(self):
        return unicode(_('Contact message from %(email)s with subject: %(subject)s.') % {'email': self.email,
                                                                                         'subject': self.subject})


class SiteSettingManager(models.Manager):
    def get_settings(self):
        obj, created = self.get_or_create(id=1)
        return obj


@python_2_unicode_compatible
class SiteSettings(models.Model):
    default_product_image = models.ImageField(_('Image'), null=True, blank=True, upload_to=upload_file_name)
    facebook_app_id = models.CharField(_('Facebook app id'), max_length=200, null=True, blank=True, help_text=_('This field is required for facebook integration'))

    objects = SiteSettingManager()

    class Meta:
        verbose_name = _("Site settings")
        verbose_name_plural = _("Site settings")

    def __str__(self):
        return unicode(_('Settings'))