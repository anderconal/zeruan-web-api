# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.test import TestCase
from .models import Client
from .models import PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES


class ClientTestCase(TestCase):
    """This class defines the test suite for the Client model."""
    def setUp(self):
        """Define the test Client and other test variables."""
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
