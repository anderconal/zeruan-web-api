from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Service
        fields = ('id', 'name', 'price', 'duration', 'category', 'description')
