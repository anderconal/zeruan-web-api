# -*- coding: utf-8 -*-
from datetime import datetime
from django.test import TestCase
from .models import Client
from .models import PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ClientModelTestCase(TestCase):
    """This class defines the test suite for the Client model."""
    def setUp(self):
        """Defines needed test variables for the Client model."""
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


    def test_string_representation(self):
        """String representation of Client model should be: name (white space) surname (white space) second_surname."""
        self.assertEqual(str(self.test_client), self.test_client.name + ' ' +
                         self.test_client.surname + ' ' +
                         self.test_client.second_surname)


    def test_verbose_name_plural(self):
        """The pluralization of Client should be Clients."""
        self.assertEqual(str(Client._meta.verbose_name_plural), 'clients')


    def test_model_can_create_a_client(self):
        """Test the Client model can create a Client."""
        old_count = Client.objects.count()

        Client.objects.create(
            dni='87654321t',
            name='Pepe',
            surname='Test',
            second_surname='Django',
            birthdate=datetime.now(),
            phone_number='999999999',
            address='Fake Street, 9',
            postal_code='99999',
            city='Bilbao',
            province='Vizcaya',
            email='test@gmail.com',
            release_date=datetime.now(),
            partner=PARTNER_OPTIONS.NO_PARTNER,
            partner_release_date=datetime.now(),
            known_for=KNOWN_FOR_CHOICES.FACEBOOK,
            lopd=True,
            lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
            lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
            notes='Test'
        )

        new_count = Client.objects.count()

        self.assertNotEqual(old_count, new_count)


class ClientViewTestCase(TestCase):
    """Test suite for the Client view."""
    def setUp(self):
        """Defines the test API client and other test variables."""
        self.api_client = APIClient()

        self.client_data = {
            "dni": "00099887y",
            "name": "Harry",
            "surname": "Potter",
            "second_surname": "",
            "birthdate": "1992-06-22",
            "phone_number": "999323456",
            "address": "Tellafake, 2",
            "postal_code": "48012",
            "city": "London",
            "province": "Vizcaya",
            "email": "harry@potter.es",
            "release_date": "2017-06-11",
            "partner": "NO_PARTNER",
            "partner_release_date": None,
            "known_for": "FACEBOOK",
            "lopd": False,
            "lopd_channel": "WHATSAPP",
            "lopd_options": "",
            "notes": ""
        }

        self.client = Client.objects.create(
            dni='87654321t',
            name='Pepe',
            surname='Test',
            second_surname='Django',
            birthdate=datetime.now(),
            phone_number='999999999',
            address='Fake Street, 9',
            postal_code='99999',
            city='Bilbao',
            province='Vizcaya',
            email='test@gmail.com',
            release_date=datetime.now(),
            partner=PARTNER_OPTIONS.NO_PARTNER,
            partner_release_date=datetime.now(),
            known_for=KNOWN_FOR_CHOICES.FACEBOOK,
            lopd=True,
            lopd_channel=LOPD_CHANNEL_CHOICES.WHATSAPP,
            lopd_options=LOPD_OPTION_CHOICES.FOTODEPILACION,
            notes='Test'
        )


    def test_api_can_create_a_client(self):
        """Test the API has Client creation capability."""
        response = self.api_client.post(
            reverse('client-create'),
            self.client_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Client.objects.get(pk=response.json().get('id'))


    def test_api_can_get_a_client(self):
        """Test the API can get a given Client."""
        response = self.api_client.get(
            reverse('client-details',
            kwargs={'pk': self.client.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Client.objects.get(pk=response.json().get('id'))


    def test_api_can_update_a_client(self):
        """Test the API can update a given Client."""
        response = self.api_client.put(
            reverse('client-details',
            kwargs={'pk': self.client.id}),
            self.client_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Client.objects.get(pk=response.json().get('id'))
        self.assertEqual(response.json().get('dni'), self.client_data.get('dni'))
        self.assertEqual(response.json().get('name'), self.client_data.get('name'))
        self.assertEqual(response.json().get('surname'), self.client_data.get('surname'))
        self.assertEqual(response.json().get('second_surname'), self.client_data.get('second_surname'))
        self.assertEqual(response.json().get('birthdate'), self.client_data.get('birthdate'))
        self.assertEqual(response.json().get('phone_number'), self.client_data.get('phone_number'))
        self.assertEqual(response.json().get('address'), self.client_data.get('address'))
        self.assertEqual(response.json().get('postal_code'), self.client_data.get('postal_code'))
        self.assertEqual(response.json().get('city'), self.client_data.get('city'))
        self.assertEqual(response.json().get('province'), self.client_data.get('province'))
        self.assertEqual(response.json().get('email'), self.client_data.get('email'))
        self.assertEqual(response.json().get('release_date'), self.client_data.get('release_date'))
        self.assertEqual(response.json().get('partner'), self.client_data.get('partner'))
        self.assertEqual(response.json().get('partner_release_date'), self.client_data.get('partner_release_date'))
        self.assertEqual(response.json().get('known_for'), self.client_data.get('known_for'))
        self.assertEqual(response.json().get('lopd'), self.client_data.get('lopd'))
        self.assertEqual(response.json().get('lopd_channel'), self.client_data.get('lopd_channel'))
        self.assertEqual(response.json().get('lopd_options'), self.client_data.get('lopd_options'))
        self.assertEqual(response.json().get('notes'), self.client_data.get('notes'))


    def test_api_can_delete_a_client(self):
        """Test the API can delete a Client."""
        response = self.api_client.delete(
            reverse('client-details',
            kwargs={'pk': self.client.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
