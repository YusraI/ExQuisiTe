# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationanswer',
            name='are_related',
        ),
        migrations.RemoveField(
            model_name='evaluationanswer',
            name='exmaple',
        ),
        migrations.AddField(
            model_name='evaluationexample',
            name='answer',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='userstudy.EvaluationAnswer'),
            preserve_default=False,
        ),
    ]
