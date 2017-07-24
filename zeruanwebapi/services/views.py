# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import ServiceSerializer
from .models import Service

class ServiceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Service."""
        serializer.save()


class ServiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
