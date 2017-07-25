# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .serializers import InvoiceSerializer
from .models import Invoice

class InvoiceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
