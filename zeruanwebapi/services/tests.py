# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Service, CATEGORIES
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from my_user.models import User

class ServiceModelTestCase(TestCase):
    """This class defines the test suite for the Service model."""
    def setUp(self):
        """Defines needed test variables for the Service model."""
        self.test_service = Service.objects.create(
            name='Manicura Flash',
            price=11.00,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )


    def test_string_representation(self):
        """String representation of Service model should be: category: (white space) name."""
        self.assertEqual(str(self.test_service), self.test_service.category + ': ' + self.test_service.name)


    def test_verbose_name_plural(self):
        """The pluralization of Service should be Services."""
        self.assertEqual(str(Service._meta.verbose_name_plural), 'services')


    def test_model_can_create_a_service(self):
        """Test the Service model can create a Service."""
        old_count = Service.objects.count()

        Service.objects.create(
            name='Manicura Zeruan',
            price=15.50,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

        new_count = Service.objects.count()

        self.assertNotEqual(old_count, new_count)


    def test_default_duration_on_model_create(self):
        """The default duration should be 900."""
        new_service = Service.objects.create(
            name='Manicura Zeruan',
            price=15.50,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

        self.assertEqual(new_service.duration, 900)


class ServiceViewTestCase(TestCase):
    """Test suite for the Service view."""
    def setUp(self):
        """Defines the test API client and other test variables."""
        token = self.getToken()
        self.api_client = APIClient()
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.service_data = {
            "name": "Pedicura Zeruan",
            "price": "22.50",
            "category": "PEDICURA",
            "description": "Description"
        }

        self.service = Service.objects.create(
            name='Manicura Zeruan',
            price=15.50,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )


    def getToken(self):
        user = User.objects.create_user(username='testusername', password='testpassword', email='testemail@test.es')
        token = Token.objects.get_or_create(user=user)
        return token[0].key


    def test_api_can_create_a_service(self):
        """Test the API has Client creation capability."""
        response = self.api_client.post(
            reverse('service-create'),
            self.service_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Service.objects.get(pk=response.json().get('id'))


    def test_default_duration_on_api_create(self):
        """The default duration should be 900."""
        response = self.api_client.post(
            reverse('service-create'),
            self.service_data,
            format="json"
        )

        self.assertEqual(response.json().get('duration'), 900)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Service.objects.get(pk=response.json().get('id'))


    def test_api_can_get_a_service(self):
        """Test the API can get a given Service."""
        response = self.api_client.get(
            reverse('service-details',
            kwargs={'pk': self.service.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Service.objects.get(pk=response.json().get('id'))


    def test_api_can_updte_a_service(self):
        """Test the API can update a given Service."""
        response = self.api_client.put(
            reverse('service-details',
            kwargs={'pk': self.service.id}),
            self.service_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Service.objects.get(pk=response.json().get('id'))
        self.assertEqual(response.json().get('name'), self.service_data.get('name'))
        self.assertEqual(response.json().get('price'), self.service_data.get('price'))
        self.assertEqual(response.json().get('duration'), 900)
        self.assertEqual(response.json().get('category'), self.service_data.get('category'))
        self.assertEqual(response.json().get('description'), self.service_data.get('description'))


    def test_api_can_delete_a_service(self):
        """Test the API can delete a Service."""
        response = self.api_client.delete(
            reverse('service-details',
            kwargs={'pk': self.service.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
