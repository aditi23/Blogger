# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 08:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blblogger', '0004_auto_20161117_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 17, 8, 55, 26, 407144, tzinfo=utc)),
        ),
    ]