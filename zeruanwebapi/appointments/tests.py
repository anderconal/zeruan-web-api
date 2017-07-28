# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from services.models import Service, CATEGORIES
from invoices.models import Invoice
from .models import Appointment, APPOINTMENT_STATES
from datetime import datetime
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from my_user.models import User

class AppointmentModelTestCase(TestCase):
    """This class defines the test suite for the Appointment model."""
    def setUp(self):
        """Defines needed test variables for the Appointment model."""
        self.test_service = Service.objects.create(
            name='Manicura Flash',
            price=11.00,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

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
            client=self.test_client
        )

        self.test_appointment = Appointment.objects.create(
            date=timezone.now(),
            client=self.test_client,
            invoice=self.test_invoice,
            notes=''
        )

        self.test_appointment.service.add(self.test_service)
        self.test_appointment.save()


    def test_string_representation(self):
        """String representation of Appointment model should be: Appointment: (white space) id."""
        self.assertEqual(str(self.test_appointment), 'Appointment: ' + str(self.test_appointment.id))


    def test_verbose_name_plural(self):
        """The pluralization of Appointment should be Appointments."""
        self.assertEqual(str(Appointment._meta.verbose_name_plural), 'appointments')


    def test_model_can_create_an_appointment(self):
        """Test the Appointment model can create a Appointment."""
        old_count = Appointment.objects.count()

        new_invoice = Invoice.objects.create(
            issueDate=timezone.now(),
            client=self.test_client
        )

        new_appointment = Appointment.objects.create(
            date=timezone.now(),
            client=self.test_client,
            invoice=new_invoice,
            notes=''
        )

        new_appointment.service.add(self.test_service)
        new_appointment.save()

        new_count = Appointment.objects.count()

        self.assertNotEqual(old_count, new_count)


class AppointmentViewTestCase(TestCase):
    """Test suite for the Appointment views."""
    def setUp(self):
        """Defines the test client and other test variables."""
        token = self.getToken()
        self.api_client = APIClient()
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        self.test_service = Service.objects.create(
            name='Manicura Flash',
            price=11.00,
            category=CATEGORIES.MANICURA,
            description='Test description'
        )

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
            client=self.test_client
        )

        self.another_test_invoice = Invoice.objects.create(
            issueDate=timezone.now(),
            client=self.test_client
        )

        self.appointment_data = {
            "service": [self.test_service.id],
            "date": timezone.now(),
            "client": self.test_client.id,
            "invoice": self.another_test_invoice.id,
            "notes": "Newly created notes."
        }

        self.test_appointment = Appointment.objects.create(
            date=timezone.now(),
            client=self.test_client,
            invoice=self.test_invoice,
            notes=''
        )

        self.test_appointment.service.add(self.test_service)
        self.test_appointment.save()


    def getToken(self):
        user = User.objects.create_user(username='testusername', password='testpassword', email='testemail@test.es')
        token = Token.objects.get_or_create(user=user)
        return token[0].key


    def test_api_can_create_an_appointment(self):
        """Test the API has Appointment creation capability."""
        response = self.api_client.post(
            reverse('appointment-create'),
            self.appointment_data,
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Appointment.objects.get(pk=response.json().get('id'))


    def test_default_state(self):
        """Test the default state is PENDING."""
        response = self.api_client.post(
            reverse('appointment-create'),
            self.appointment_data,
            format="json")

        self.assertEqual(response.json().get('state'), APPOINTMENT_STATES.PENDING)


    def test_api_can_get_an_appointment(self):
        """Test the API can get a given Appointment."""
        response = self.api_client.get(
            reverse('appointment-details',
            kwargs={'pk': self.test_appointment.id}),
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Appointment.objects.get(pk=response.json().get('id'))


    def test_api_can_update_an_appointment(self):
        """Test the API can update a given Appointment."""
        response = self.api_client.put(
            reverse('appointment-details',
            kwargs={'pk': self.test_appointment.id}),
            self.appointment_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Appointment.objects.get(pk=response.json().get('id'))
        self.assertEqual(response.json().get('notes'), self.appointment_data.get('notes'))


    def test_api_can_delete_an_appointment(self):
        """Test the API can delete a given Appointment."""
        response = self.api_client.delete(
            reverse('appointment-details',
            kwargs={'pk': self.test_appointment.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
