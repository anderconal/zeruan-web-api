# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Product, PrepaidCard, PRODUCT_CATEGORIES
from clients.models import Client
from clients.models import PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


def add_years(date, years):
    new_year = date.year + years
    try:
        return date.replace(year=new_year)
    except ValueError:
        if (date.month == 2 and date.day == 29 and  # leap day
                isleap(date.year) and not isleap(new_year)):
            return date.replace(year=new_year, day=28)
        raise


class ProductModelTestCase(TestCase):
    """This class defines the test suite for the Product model."""


    def setUp(self):
        """Define the test Product and other test variables."""
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

        self.test_product = Product.objects.create(
            name='The best product',
            price = 10.00,
            stock = 0,
            category = PRODUCT_CATEGORIES.UNCATEGORIZED
        )


    def test_string_representation(self):
        """String representation of Product model should be: name."""

        self.assertEqual(str(self.test_product), self.test_product.name)


    def test_verbose_name_plural(self):
        """The pluralization of Product should be Products."""
        self.assertEqual(str(Product._meta.verbose_name_plural), 'products')


    def test_model_can_create_a_product(self):
        old_count = Product.objects.count()
        Product.objects.create(
            name='The best product',
            price=10.00,
            stock=0,
            category=PRODUCT_CATEGORIES.UNCATEGORIZED
        )
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)


class ProductViewTestCase(TestCase):
    """Test suite for the Product views."""


    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.product_data = {
            "name": "Crema hidratante total descontracturante",
            "price": "39.90",
            "stock": 2,
            "category": "LINEA_ESENCIAL"
        }


    def test_api_can_create_a_product(self):
        """Test the api has product creation capability."""
        response = self.client.post(
            reverse('product-create'),
            self.product_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Product.objects.get(pk=response.json().get('id')))
        self.assertEqual(response.json().get('name'), self.product_data.get('name'))
        self.assertEqual(response.json().get('price'), self.product_data.get('price'))
        self.assertEqual(response.json().get('stock'), self.product_data.get('stock'))
        self.assertEqual(response.json().get('category'), self.product_data.get('category'))


class PrepaidCardModelTestCase(TestCase):
    """This class defines the test suite for the PrepaidCard model."""


    def setUp(self):
        """Define the test Prepaid Card and other test variables."""
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

        self.test_prepaid_card = PrepaidCard.objects.create(
            name='Pack Zeruan Bat',
            price=120.00,
            stock=0,
            category=PRODUCT_CATEGORIES.METODOS_DE_PAGO,
            available_amount=0.00,
            client=self.test_client
        )


    def test_string_representation(self):
        """String representation of PrepaidCard model should be: name (whitespace) id (whitespace) client.name
        (whitespace) client.id."""
        stringRepresentation = \
            self.test_prepaid_card.name + ' ' + \
            str(self.test_prepaid_card.id) + ' ' + \
            self.test_prepaid_card.client.name + ' ' + \
            str(self.test_prepaid_card.client.id)
        self.assertEqual(str(self.test_prepaid_card), stringRepresentation)


    def test_verbose_name_plural(self):
        """The pluralization of PrepaidCard should be prepaid cards."""
        self.assertEqual(str(PrepaidCard._meta.verbose_name_plural), 'prepaid cards')


    def test_expiry_date(self):
        """The default expiry date should be the current year plus 1."""
        self.assertEqual(self.test_prepaid_card.expiry_date.year, add_years(timezone.now(), 1).year)
        self.assertEqual(self.test_prepaid_card.expiry_date.month, add_years(timezone.now(), 1).month)
        self.assertEqual(self.test_prepaid_card.expiry_date.day, add_years(timezone.now(), 1).day)


    def test_purchase_date(self):
        """The default purchase date should be the current one."""
        self.assertEqual(self.test_prepaid_card.purchase_date.year, timezone.now().year)
        self.assertEqual(self.test_prepaid_card.purchase_date.month, timezone.now().month)
        self.assertEqual(self.test_prepaid_card.purchase_date.day, timezone.now().day)


    def test_model_can_create_a_prepaid_card(self):
        old_count = PrepaidCard.objects.count()
        PrepaidCard.objects.create(
            name='Pack Zeruan Bat',
            price=120.00,
            stock=0,
            category=PRODUCT_CATEGORIES.METODOS_DE_PAGO,
            available_amount=0.00,
            client=self.test_client
        )
        new_count = PrepaidCard.objects.count()
        self.assertNotEqual(old_count, new_count)


class PrepaidCardViewTestCase(TestCase):
    """Test suite for the PrepaidCard views."""


    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
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
        self.prepaid_card_data = {
            "name": "Another Pack",
            "price": "120.00",
            "stock": 0,
            "category": "METODOS_DE_PAGO",
            "available_amount": "120.00",
            "client": self.test_client.id,
            "expiry_date": "2018-07-01T21:39:33.315323Z",
            "purchase_date": "2017-07-01T21:39:33.315291Z"
        }

    def test_api_can_create_a_prepaid_card(self):
        """Test the api has prepaid card creation capability."""
        response = self.client.post(
            reverse('prepaid-card-create'),
            self.prepaid_card_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PrepaidCard.objects.get(pk=response.json().get('id')))
        self.assertEqual(response.json().get('name'), self.prepaid_card_data.get('name'))
        self.assertEqual(response.json().get('price'), self.prepaid_card_data.get('price'))
        self.assertEqual(response.json().get('stock'), self.prepaid_card_data.get('stock'))
        self.assertEqual(response.json().get('category'), self.prepaid_card_data.get('category'))
        self.assertEqual(response.json().get('available_amount'), self.prepaid_card_data.get('available_amount'))
        self.assertEqual(response.json().get('client'), self.prepaid_card_data.get('client'))
        self.assertEqual(response.json().get('expiry_date'), self.prepaid_card_data.get('expiry_date'))
        self.assertEqual(response.json().get('purchase_date'), self.prepaid_card_data.get('purchase_date'))
