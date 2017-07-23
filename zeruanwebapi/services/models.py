# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils import Choices

CATEGORIES = Choices(
    ('FOTODEPILACION', 'Fotodepilación'),
    ('MANICURA', 'Manicura'),
    ('PEDICURA', 'Pedicura'),
    ('MAQUILLAJE', 'Maquillaje'),
    ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'),
    ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'),
    ('CEJAS_Y_PESTANAS', 'Cejas y pestañas')
)


class Service(models.Model):
    """ Service model. """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField(default=900)
    category = models.CharField(
        choices=CATEGORIES,
        default=CATEGORIES.FOTODEPILACION,
        max_length=255
    )
    description = models.TextField()

    def __unicode__(self):
        return self.category + ': ' + self.name
