# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 22:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0002_auto_20170324_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 22, 40, 37, 47806, tzinfo=utc), verbose_name='Time Logged'),
        ),
    ]