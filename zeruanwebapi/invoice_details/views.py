# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .serializers import InvoiceDetailSerializer
from .models import InvoiceDetail

class InvoiceDetailCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer


class InvoiceDetailDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
