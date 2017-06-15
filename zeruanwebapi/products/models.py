# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from calendar import isleap
from model_utils import Choices
from clients.models import Client


PRODUCT_CATEGORIES = Choices(
    ('CAFETERAPIA', 'Cafeterapia'),
    ('FITOTERAPIA', 'Fitoterapia'),
    ('HIALURÓNICO', 'Hialurónico'),
    ('LINEA_ESENCIAL', 'Línea esencial'),
    ('LINFODRENANTE', 'Linfodrenante'),
    ('PERLAS', 'Perlas'),
    ('PIELES_GRASAS', 'Pieles grasas'),
    ('PIELES_SENSIBLES', 'Pieles sensibles'),
    ('METODOS_DE_PAGO', 'Métodos de pago'),
    ('UNCATEGORIZED', 'Sin categorizar')
)


def add_years(date, years):
    new_year = date.year + years
    try:
        return date.replace(year=new_year)
    except ValueError:
        if (date.month == 2 and date.day == 29 and  # leap day
                isleap(date.year) and not isleap(new_year)):
            return date.replace(year=new_year, day=28)
        raise


class Product(models.Model):
    """ Product model. """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(
        choices=PRODUCT_CATEGORIES,
        default=PRODUCT_CATEGORIES.UNCATEGORIZED,
        max_length=255
    )
    purchase_date = models.DateTimeField(
        default=timezone.now())


    def __unicode__(self):
        return self.name


class PrepaidCard(Product):
    """ Prepaid Card model. Multi-table inheritance. """
    available_amount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    expiry_date = models.DateTimeField(
        default=add_years(timezone.now(), 1)
    )


    def __unicode__(self):
        return self.name + ' ' + str(self.id) + ' ' + self.client.name + ' ' + str(self.client.id)