# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20170725_2129'),
        ('invoice_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='prepaid_card',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prepaid_card', to='products.PrepaidCard'),
        ),
        migrations.RemoveField(
            model_name='invoicedetail',
            name='product',
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Product'),
        ),
    ]