# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Service, CATEGORIES

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
