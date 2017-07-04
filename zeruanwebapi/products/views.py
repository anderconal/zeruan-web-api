# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, PrepaidCardSerializer
from .models import Product, PrepaidCard


class ProductCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()


class PrepaidCardCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PrepaidCard.objects.all()
    serializer_class = PrepaidCardSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new prepaid card."""
        serializer.save()