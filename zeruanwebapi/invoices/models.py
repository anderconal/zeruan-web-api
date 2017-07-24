# -*- coding: utf-8 -*-
""" Set UTF-8 enconding """

from __future__ import unicode_literals
from django.db import models
from clients.models import Client
from django.utils import timezone

class Invoice(models.Model):
    """ Invoice model. """
    issueDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default= timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Invoice: ' + str(self.id)
