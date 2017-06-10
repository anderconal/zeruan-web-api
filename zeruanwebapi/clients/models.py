# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
from model_utils import Choices

PARTNER_OPTIONS = Choices(
    ('NO_PARTNER', 'No socio'),
    ('PARTNER_A', 'Tipo A'),
    ('PARTNER_B', 'Tipo B'),
    ('PARTNER_C', 'Tipo C')
)

KNOWN_FOR_CHOICES = Choices(
    ('FACEBOOK', 'Facebook'),
    ('INSTAGRAM', 'Instagram'),
    ('INTERNET', 'Internet'),
    ('RADIO', 'Radio'),
    ('BOCA_A_BOCA', 'Boca a boca'),
    ('LOCALIZACION', 'Localización'),
    ('PUBLICIDAD_IMPRESA', 'Publicidad impresa'),
    ('OTROS', 'Otros')
)

LOPD_CHANNEL_CHOICES = Choices(
    ('WHATSAPP', 'WhatsApp'),
    ('EMAIL', 'Email'),
    ('NONE', 'No LOPD')
)

LOPD_OPTION_CHOICES = Choices(
    ('FOTODEPILACION', 'Fotodepilación'),
    ('MANICURA', 'Manicura'),
    ('PEDICURA', 'Pedicura'),
    ('MAQUILLAJE', 'Maquillaje'),
    ('TRATAMIENTOS_FACIALES', 'Tratamientos faciales'),
    ('TRATAMIENTOS_CORPORALES', 'Tratamientos corporales'),
    ('CEJAS_Y_PESTANAS', 'Cejas y pestañas')
)


class Client(models.Model):
    """ Client model. """
    dni = models.CharField(max_length=9, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True)
    phone_number = models.CharField(max_length=21)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    release_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True)
    partner = models.CharField(
        choices=PARTNER_OPTIONS,
        default=PARTNER_OPTIONS.NO_PARTNER,
        max_length=255
    )
    partner_release_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True, null=True
    )
    known_for = models.CharField(
        choices=KNOWN_FOR_CHOICES,
        default=KNOWN_FOR_CHOICES.FACEBOOK,
        max_length=255
    )
    lopd = models.BooleanField(default=False)
    lopd_channel = models.CharField(
        choices=LOPD_CHANNEL_CHOICES,
        default=LOPD_CHANNEL_CHOICES.NONE,
        max_length=255
    )
    lopd_options = MultiSelectField(
        choices=LOPD_OPTION_CHOICES,
        default=None,
        max_length=255,
        blank=True,
        null=True
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.second_surname
