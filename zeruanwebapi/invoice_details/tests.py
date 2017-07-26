# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import InvoiceDetail, VAT_CHOICES, PAYMENT_METHODS
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from invoices.models import Invoice
from services.models import Service, CATEGORIES
from products.models import Product, PrepaidCard, PRODUCT_CATEGORIES
from datetime import datetime
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class InvoiceDetailModelTestCase(TestCase):
    """This class defines the test suite for the InvoiceDetail model."""
    def setUp(self):
        """Defines needed test variables for the InvoiceDetail model."""
        self.test_client = Client.objects.create(
            dni='12345678t',
            name='Ander',
            surname='Conal',
            second_surname='Fuertes',
            birthdate=datetime.now(),
            phone_number='666666666',
            address='Fake Street, 7',
            postal_code='66666',
            city='Bilbao',
            province='Vizcaya',
            email='ander.conal@gmail.com',
            release_date=datetime.now(),
            partner=PARTNER_OPTIONS.NO_PARTNER,
            partner_release_date=datetime.now(),
            known_for=KNOWN_FOR_CHOICES.FACEBOOK,
            lopd=True,
            lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
            lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
            notes='Test'
        )

        self.test_invoice = Invoice.objects.create(
            client=self.test_client
        )

        self.test_service = Service.objects.create(
            name='Manicura Flash',
            price=11.00,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

        self.test_product = Product.objects.create(
            name='The best product',
            price=10.00,
            stock=0,
            category=PRODUCT_CATEGORIES.UNCATEGORIZED
        )

        self.test_prepaid_card = PrepaidCard.objects.create(
            name='Pack Zeruan Bat',
            price=120.00,
            stock=0,
            category=PRODUCT_CATEGORIES.METODOS_DE_PAGO,
            available_amount=0.00,
            client=self.test_client
        )

        self.test_invoice_detail = InvoiceDetail.objects.create(
            invoice=self.test_invoice,
            service=self.test_service
        )


    def test_string_representation(self):
        """String representation of InvoiceDetail model should be: 'Invoice: ' + str(self.invoice.id) + ' Invoice detail: ' + str(self.id)."""
        self.assertEqual(str(self.test_invoice_detail), 'Invoice: ' + str(self.test_invoice.id) + ' Invoice detail: ' + str(self.test_invoice_detail.id))


    def test_verbose_name_plural(self):
        """The pluralization of InvoiceDetail should be InvoiceDetails."""
        self.assertEqual(str(InvoiceDetail._meta.verbose_name_plural), 'invoice details')


    def test_model_can_create_a_invoice_detail_with_all_the_defaults(self):
        """Test the InvoiceDetail model can create a InvoiceDetail with all the defaults."""
        old_count = InvoiceDetail.objects.count()

        test_invoice_detail = InvoiceDetail.objects.create(
            invoice=self.test_invoice,
            service=self.test_service
        )

        new_count = InvoiceDetail.objects.count()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(test_invoice_detail.quantity, 1)
        self.assertEqual(test_invoice_detail.vat, VAT_CHOICES.GENERAL)
        self.assertEqual(test_invoice_detail.payment_method, PAYMENT_METHODS.CASH)
        self.assertEqual(test_invoice_detail.discount, 0)


class InvoiceDetailViewTestCase(TestCase):
    """Test suite for the InvoiceDetail views."""
    def setUp(self):
        """Defines the test client and other test variables."""
        self.api_client = APIClient()

        self.test_client = Client.objects.create(
            dni='12345678t',
            name='Ander',
            surname='Conal',
            second_surname='Fuertes',
            birthdate=datetime.now(),
            phone_number='666666666',
            address='Fake Street, 7',
            postal_code='66666',
            city='Bilbao',
            province='Vizcaya',
            email='ander.conal@gmail.com',
            release_date=datetime.now(),
            partner=PARTNER_OPTIONS.NO_PARTNER,
            partner_release_date=datetime.now(),
            known_for=KNOWN_FOR_CHOICES.FACEBOOK,
            lopd=True,
            lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
            lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
            notes='Test'
        )

        self.test_invoice = Invoice.objects.create(
            client=self.test_client
        )

        self.test_service = Service.objects.create(
            name='Manicura Flash',
            price=11.00,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

        self.test_product = Product.objects.create(
            name='The best product',
            price=10.00,
            stock=0,
            category=PRODUCT_CATEGORIES.UNCATEGORIZED
        )

        self.test_prepaid_card = PrepaidCard.objects.create(
            name='Pack Zeruan Bat',
            price=120.00,
            stock=0,
            category=PRODUCT_CATEGORIES.METODOS_DE_PAGO,
            available_amount=0.00,
            client=self.test_client
        )

        self.invoice_detail_data = {
            "invoice": self.test_invoice.id,
            "service": self.test_service.id
        }

        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.test_invoice,
            service=self.test_service
        )


    def test_api_can_create_a_invoice_detail_with_a_service(self):
        """Test the API has InvoiceDetail creation capability (with a service)."""
        invoice_detail_with_a_service = {
            "invoice": self.test_invoice.id,
            "service": self.test_service.id
        }

        response = self.api_client.post(
            reverse('invoice-detail-create'),
            invoice_detail_with_a_service,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        InvoiceDetail.objects.get(pk=response.json().get('id'))


    def test_api_can_create_a_invoice_detail_with_a_product(self):
        """Test the API has InvoiceDetail creation capability (with a product)."""
        invoice_detail_with_a_product = {
            "invoice": self.test_invoice.id,
            "product": self.test_product.id
        }

        response = self.api_client.post(
            reverse('invoice-detail-create'),
            invoice_detail_with_a_product,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        InvoiceDetail.objects.get(pk=response.json().get('id'))


    def test_api_can_create_a_invoice_detail_paid_with_a_prepaid_card(self):
        """Test the API has InvoiceDetail creation capability (paid with a prepaid card)."""
        invoice_detail_with_a_product = {
            "invoice": self.test_invoice.id,
            "product": self.test_product.id,
            "prepaid_card": self.test_prepaid_card.id
        }

        response = self.api_client.post(
            reverse('invoice-detail-create'),
            invoice_detail_with_a_product,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        InvoiceDetail.objects.get(pk=response.json().get('id'))


    def test_default_quantity(self):
        """The default quantity should be 1."""
        response = self.api_client.post(
            reverse('invoice-detail-create'),
            self.invoice_detail_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('quantity'), 1)


    def test_default_vat(self):
        """The default vat should be GENERAL."""
        response = self.api_client.post(
            reverse('invoice-detail-create'),
            self.invoice_detail_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('vat'), VAT_CHOICES.GENERAL)


    def test_default_discount(self):
        """The default discount should be 0."""
        response = self.api_client.post(
            reverse('invoice-detail-create'),
            self.invoice_detail_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('discount'), 0)


    def test_default_payment_method(self):
        """The default payment method should be CASH."""
        response = self.api_client.post(
            reverse('invoice-detail-create'),
            self.invoice_detail_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('payment_method'), PAYMENT_METHODS.CASH)


    def test_api_can_get_a_invoice_detail(self):
        """Test the API can get a given InvoiceDetail."""
        response = self.api_client.get(
            reverse('invoice-detail-details',
            kwargs={'pk': self.invoice_detail.id}),
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        InvoiceDetail.objects.get(pk=response.json().get('id'))


    def test_api_can_update_a_invoice_detail(self):
        """Test the API can update a given InvoiceDetail."""
        response = self.api_client.put(
            reverse('invoice-detail-details',
            kwargs={'pk': self.invoice_detail.id}),
            self.invoice_detail_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        InvoiceDetail.objects.get(pk=response.json().get('id'))
        self.assertEqual(response.json().get('client'), self.invoice_detail_data.get('client'))


    def test_api_can_delete_a_invoice_detail(self):
        response = self.api_client.delete(
            reverse('invoice-detail-details',
            kwargs={'pk': self.invoice_detail.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
