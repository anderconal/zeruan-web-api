# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Product
from .models import PrepaidCard

class ProductModelTestCase(TestCase):
    """This class defines the test suite for the Product model."""


    def setUp(self):
        """Define the test Product and other test variables."""
        self.test_product = Product.objects.create(

        )


    def test_string_representation(self):
        """String representation of Product model should be: name (white space) surname (white space) second_surname."""

        self.assertEqual(str(self.test_product), self.test_product.name + ' ' +
                         self.test_product.surname + ' ' +
                         self.test_product.second_surname)


    def test_verbose_name_plural(self):
        """The pluralization of Product should be Products."""
        self.assertEqual(str(Product._meta.verbose_name_plural), 'products')