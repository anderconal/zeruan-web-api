# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from clients.models import Client, PARTNER_OPTIONS, KNOWN_FOR_CHOICES, LOPD_CHANNEL_CHOICES, LOPD_OPTION_CHOICES
from services.models import Service, CATEGORIES
from invoices.models import Invoice
from .models import Appointment, APPOINTMENT_STATES
from datetime import datetime
from django.utils import timezone

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
