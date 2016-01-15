# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 20:19
from __future__ import unicode_literals

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_product_image', models.ImageField(blank=True, null=True, upload_to=core.utils.upload_file_name, verbose_name='Image')),
                ('facebook_app_id', models.CharField(blank=True, help_text='This field is required for facebook integration', max_length=200, null=True, verbose_name='Facebook app id')),
            ],
            options={
                'verbose_name': 'Site settings',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]