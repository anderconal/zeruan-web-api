# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Appointment."""
        serializer.save()


class AppointmentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
