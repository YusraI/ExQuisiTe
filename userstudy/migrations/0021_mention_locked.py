# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0020_auto_20171205_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='mention',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
