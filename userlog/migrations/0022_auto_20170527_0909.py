# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-27 09:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0021_auto_20170527_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 9, 9, 43, 934115, tzinfo=utc), verbose_name='Time Logged'),
        ),
    ]
