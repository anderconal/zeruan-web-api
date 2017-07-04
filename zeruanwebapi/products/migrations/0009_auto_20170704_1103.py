# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170630_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidcard',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_id', to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='prepaidcard',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 4, 11, 3, 40, 985532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prepaidcard',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 11, 3, 40, 985509, tzinfo=utc)),
        ),
    ]
