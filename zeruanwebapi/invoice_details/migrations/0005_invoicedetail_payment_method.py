# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_details', '0004_auto_20170726_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Met\xe1lico'), ('CREDIT_CARD', 'Tarjeta de cr\xe9dito'), ('PREPAID_CARD', 'Bono')], default='CASH', max_length=255),
        ),
    ]
