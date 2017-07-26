# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import InvoiceDetail, VAT_CHOICES, PAYMENT_METHODS
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from invoices.models import Invoice
from services.models import Service, CATEGORIES
from products.models import Product, PrepaidCard, PRODUCT_CATEGORIES
from datetime import datetime
from django.utils import timezone
from django.db import IntegrityError

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
            issueDate=timezone.now(),
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


    def test_model_can_create_a_invoice_detail(self):
        """Test the InvoiceDetail model can create a InvoiceDetail."""
        old_count = InvoiceDetail.objects.count()

        InvoiceDetail.objects.create(
            invoice=self.test_invoice,
            service=self.test_service
        )

        new_count = InvoiceDetail.objects.count()

        self.assertNotEqual(old_count, new_count)
