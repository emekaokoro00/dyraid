# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 02:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0002_auto_20170217_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 58, 15, 847525, tzinfo=utc), verbose_name='Time Logged'),
        ),
    ]
