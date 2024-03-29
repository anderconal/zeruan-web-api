# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import ClientSerializer
from .models import Client

class ClientCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Client."""
        serializer.save()


class ClientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
