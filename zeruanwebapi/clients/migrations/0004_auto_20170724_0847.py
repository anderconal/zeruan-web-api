# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20170723_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='known_for',
            field=models.CharField(choices=[('FACEBOOK', 'Facebook'), ('INSTAGRAM', 'Instagram'), ('INTERNET', 'Internet'), ('RADIO', 'Radio'), ('BOCA_A_BOCA', 'Boca a boca'), ('LOCALIZACION', 'Localizaci\xf3n'), ('PUBLICIDAD_IMPRESA', 'Publicidad impresa'), ('OTROS', 'Otros')], default='OTROS', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='lopd_options',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('FOTODEPILACION', 'Fotodepilaci\xf3n'), ('MANICURA', 'Manicura'), ('PEDICURA', 'Pedicura'), ('MAQUILLAJE', 'Maquillaje'), ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'), ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'), ('CEJAS_Y_PESTANAS', 'Cejas y pesta\xf1as')], default=None, max_length=255, null=True),
        ),
    ]