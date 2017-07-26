from rest_framework import serializers
from .models import InvoiceDetail
from services.models import Service
from products.models import Product, PrepaidCard
from invoices.models import Invoice

class InvoiceDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
        service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
        product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
        prepaid_card = serializers.PrimaryKeyRelatedField(queryset=PrepaidCard.objects.all())

        model = InvoiceDetail
        fields = ('id', 'invoice', 'service', 'product', 'prepaid_card', 'quantity', 'vat', 'discount', 'payment_method', 'unit_price')
