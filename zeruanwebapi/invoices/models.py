# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from clients.models import Client
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Invoice(models.Model):
    """ Invoice model. """
    issueDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default= timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Invoice: ' + str(self.id)
