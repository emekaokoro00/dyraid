# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-27 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0010_auto_20170527_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 8, 42, 39, 569155, tzinfo=utc), verbose_name='Time Logged'),
        ),
    ]