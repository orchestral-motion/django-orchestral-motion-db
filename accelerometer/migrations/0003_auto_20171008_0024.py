# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accelerometer', '0002_auto_20171008_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
