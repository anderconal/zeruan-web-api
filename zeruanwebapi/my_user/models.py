# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
     if created:
         Token.objects.create(user=instance)
