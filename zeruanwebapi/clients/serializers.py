from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Client
        fields = ('dni', 'name', 'surname', 'second_surname', 'birthdate', 'phone_number', 'address', 'postal_code',
                  'city', 'province', 'email', 'release_date', 'partner', 'partner_release_date', 'known_for', 'lopd',
                  'lopd_channel', 'lopd_options', 'notes')
