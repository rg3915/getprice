# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exam', models.PositiveIntegerField()),
                ('score', models.PositiveIntegerField()),
            ],
        ),
    ]
