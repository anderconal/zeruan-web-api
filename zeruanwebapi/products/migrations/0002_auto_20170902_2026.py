# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidcard',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 2, 20, 26, 20, 234932, tzinfo=utc)),
        ),
    ]
