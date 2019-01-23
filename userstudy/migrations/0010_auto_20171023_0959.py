# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0009_auto_20171016_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annotation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
