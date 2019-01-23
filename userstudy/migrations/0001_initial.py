# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('are_related', models.BooleanField()),
                ('relation', models.CharField(max_length=100)),
                ('related_table_cells', models.CharField(max_length=3000, validators=[django.core.validators.RegexValidator('^(\\([0-9]+,[0-9]+\\)[,\\s]?)*$')])),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('table', models.TextField()),
                ('text_mention_start_offset', models.IntegerField()),
                ('text_mention_end_offset', models.IntegerField()),
                ('page_url', models.URLField(max_length=2000)),
                ('page_id', models.PositiveIntegerField()),
                ('table_id', models.PositiveSmallIntegerField()),
                ('mention_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='evaluationanswer',
            name='exmaple',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='userstudy.EvaluationExample'),
        ),
    ]
