# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_logger_testnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='logger',
            name='entry',
            field=models.CharField(max_length=1000),
        ),
    ]
