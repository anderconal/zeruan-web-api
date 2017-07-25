from rest_framework import serializers
from .models import Invoice
from clients.models import Client

class InvoiceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

        model = Invoice
        fields = ('id', 'issueDate', 'client')
