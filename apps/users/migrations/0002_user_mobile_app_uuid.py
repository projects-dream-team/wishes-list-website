# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_app_uuid',
            field=models.UUIDField(blank=True, null=True, verbose_name='Mobile app id'),
        ),
    ]
