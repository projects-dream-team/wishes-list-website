# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('access_code', models.SlugField(verbose_name='Url')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes_lists', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventInventedFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_invitations', to='wishes.Event', verbose_name='Event')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_invitations', to=settings.AUTH_USER_MODEL, verbose_name='Friend')),
            ],
            options={
                'verbose_name': 'Event - invented friend',
                'verbose_name_plural': 'Event - invented friends',
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('reservetion_date', models.DateTimeField(verbose_name='Reservation date')),
                ('reserved_by_anonymous', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Reserved by anonymous')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes_set', to='wishes.Event', verbose_name='Event')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes_set', to='products.Product', verbose_name='Product')),
                ('reserved_by', models.ForeignKey(blank=True, null=True, on_delete='id', to=settings.AUTH_USER_MODEL, verbose_name='Reserved by')),
            ],
            options={
                'verbose_name': 'Gift',
                'verbose_name_plural': 'Gifts',
            },
        ),
    ]