# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_initial'),
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('state', models.CharField(choices=[('PENDING', 'Pendiente'), ('CANCELLED', 'Cancelada'), ('MODIFIED', 'Modificada'), ('FINISHED', 'Finalizada')], default='PENDING', max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice')),
                ('service', models.ManyToManyField(to='services.Service')),
            ],
        ),
    ]