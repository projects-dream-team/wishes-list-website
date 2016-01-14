# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
import random
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from core.models import BaseModel, BaseManager


class UserManager(BaseManager, BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    nick = models.CharField(_('Nick'), max_length=50, unique=True)
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    is_admin = models.BooleanField(_('Is admin'), default=False)
    mobile_app_uuid = models.UUIDField(_('Mobile app id'), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        return self.nick + self.email

    def get_short_name(self):
        return self.nick

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin

    def has_perms(self, perm_list, obj=None):
        if self.is_admin:
            return True

        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.nick


class UserCodeManager(models.Manager):
    def generate_code(self):
        exists = True
        code = ''
        while exists:
            hash = hashlib.md5()
            from datetime import datetime

            now = datetime.now()
            hash.update(str(random.random()) + now.strftime('%Y-%m-%d %H:%M') + settings.SECRET_KEY)
            code = hash.hexdigest()
            exists = len(self.filter(code=code)) > 0
        return code

    def create_code(self, user, type, override=False, data=None):
        if override:
            codes = self.filter(user=user, type=type)
            for code in codes:
                code.is_active = False
                code.save()
        code = self.model()
        code.user = user
        code.type = type
        code.data = data
        code.is_active = True
        code.code = self.generate_code()
        code.save()
        return code


@python_2_unicode_compatible
class UserCode(models.Model):
    ACCOUNT_REGISTRATION = 1
    PASSWORD_RECOVERY = 2

    CODE_CHOICES = (
        (ACCOUNT_REGISTRATION, _('Account registration')),
        (PASSWORD_RECOVERY, _('Password recovery'))
    )

    user = models.ForeignKey(User, verbose_name=_('User'), related_name='user_codes')
    code = models.CharField(_('Code'), max_length=32)
    type = models.SmallIntegerField(_('Type'), choices=CODE_CHOICES)
    data = models.CharField(_('Additional data'), max_length=128, blank=True, null=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, blank=True, null=True)
    used_at = models.DateTimeField(_('Used at'), null=True, blank=True)

    objects = UserCodeManager()

    class Meta:
        verbose_name = _('User\'s code')
        verbose_name_plural = _('User\'s codes')

    def __str__(self):
        return self.code

@python_2_unicode_compatible
class Friendship(BaseModel):
    creator = models.ForeignKey(User, verbose_name=_('Creator'), related_name="friendship_creator_set")
    friend = models.ForeignKey(User, verbose_name=_('Friend'), related_name="friend_set")

    class Meta:
        verbose_name = _('Friendship')
        verbose_name_plural = _('Friendships')


    def __str__(self):
        return unicode(_('%(creator)s has added %(friend)s to firends.') % {'creator': self.creator.nick, 'friend': self.friend.nick})