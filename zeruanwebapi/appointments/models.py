# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils import Choices
from services.models import Service
from clients.models import Client
from invoices.models import Invoice
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

APPOINTMENT_STATES = Choices(
    ('PENDING', 'Pendiente'),
    ('CANCELLED', 'Cancelada'),
    ('MODIFIED', 'Modificada'),
    ('FINISHED', 'Finalizada')
)


class Appointment(models.Model):
    """ Appointment model. """
    service = models.ManyToManyField(Service)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    state = models.CharField(
        choices=APPOINTMENT_STATES,
        default=APPOINTMENT_STATES.PENDING,
        max_length=255
    )
    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE
    )
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return 'Appointment: ' + str(self.id)

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
