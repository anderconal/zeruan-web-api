# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils import Choices
from services.models import Service
from clients.models import Client
from invoices.models import Invoice

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
