# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Invoice
from datetime import datetime
from django.utils import timezone
from clients.models import Client
from clients.models import PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class InvoiceModelTestCase(TestCase):
    """This class defines the test suite for the Invoice model."""
    def setUp(self):
        """Defines needed test variables for the Invoice model."""
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
            release_date=timezone.now(),
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
            client = self.test_client
        )


    def test_string_representation(self):
        """String representation of Invoice model should be: Invoice: (white space) id."""
        self.assertEqual(str(self.test_invoice), 'Invoice: ' + str(self.test_invoice.id))


    def test_verbose_name_plural(self):
        """The pluralization of Invoice should be Invoices."""
        self.assertEqual(str(Invoice._meta.verbose_name_plural), 'invoices')


    def test_model_can_create_a_invoice(self):
        """Test the Invoice model can create a Invoice."""
        old_count = Invoice.objects.count()

        Invoice.objects.create(
            issueDate=timezone.now(),
            client=self.test_client
        )

        new_count = Invoice.objects.count()

        self.assertNotEqual(old_count, new_count)


    def test_default_issue_date_on_model_create(self):
        """Test the default issue date is the current date."""
        test_invoice = Invoice.objects.create(
            client=self.test_client
        )

        self.assertEqual(test_invoice.issueDate.year, timezone.now().year)
        self.assertEqual(test_invoice.issueDate.month, timezone.now().month)
        self.assertEqual(test_invoice.issueDate.day, timezone.now().day)


class InvoiceViewTestCase(TestCase):
    """Test suite for the Invoice views."""
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

        self.invoice_data = {
            "client": self.test_client.id
        }

        self.invoice = Invoice.objects.create(
            client=self.test_client
        )


    def test_api_can_create_a_invoice(self):
        """Test the API has invoice creation capability."""
        response = self.api_client.post(
            reverse('invoice-create'),
            self.invoice_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Invoice.objects.get(pk=response.json().get('id'))


    def test_api_can_get_a_invoice(self):
        """Test the API can get a given Invoice."""
        response = self.api_client.get(
            reverse('invoice-details',
            kwargs={'pk': self.invoice.id}),
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Invoice.objects.get(pk=response.json().get('id'))


    def test_api_can_update_a_invoice(self):
        """Test the API can update a given Invoice."""
        response = self.api_client.put(
            reverse('invoice-details',
            kwargs={'pk': self.invoice.id}),
            self.invoice_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Invoice.objects.get(pk=response.json().get('id'))
        self.assertEqual(response.json().get('client'), self.invoice_data.get('client'))


    def test_api_can_delete_a_invoice(self):
        response = self.api_client.delete(
            reverse('invoice-details',
            kwargs={'pk': self.invoice.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
