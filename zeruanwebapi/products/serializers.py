from rest_framework import serializers
from .models import Product, PrepaidCard
from clients.models import Client


class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'category')


class PrepaidCardSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PrepaidCard
        fields = ('product_ptr_id', 'name', 'price', 'stock', 'category', 'available_amount', 'client', 'client_id',
                  'expiry_date', 'purchase_date')