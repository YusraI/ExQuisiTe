# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0003_auto_20171004_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotation',
            old_name='annotatorr',
            new_name='annotator',
        ),
    ]
