# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160122_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='creator',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('owner', 'friend')]),
        ),
    ]
