# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-27 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_type_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(default=0),
        ),
    ]
