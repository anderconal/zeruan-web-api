from rest_framework import serializers
from .models import Appointment
from services.models import Service
from invoices.models import Invoice
from clients.models import Client

class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
        client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
        invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())

        model = Appointment
        fields = ('id', 'service', 'date', 'client', 'state', 'invoice', 'notes')
