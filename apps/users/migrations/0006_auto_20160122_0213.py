# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160115_2103'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('creator', 'friend')]),
        ),
    ]
