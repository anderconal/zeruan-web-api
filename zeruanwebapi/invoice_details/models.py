# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from services.models import Service
from products.models import Product
from products.models import PrepaidCard
from invoices.models import Invoice
from model_utils import Choices

VAT_CHOICES = Choices(
    (21, 'GENERAL', _('GENERAL')),
    (10, 'REDUCIDO', _('REDUCIDO')),
    (4, 'SUPERREDUCIDO', _('SUPERREDUCIDO')),
    (0, 'EXENTO', _('EXENTO'))
)

PAYMENT_METHODS = Choices(
    ('CASH', 'Metálico'),
    ('CREDIT_CARD', 'Tarjeta de crédito'),
    ('PREPAID_CARD', 'Bono')
)


class InvoiceDetail(models.Model):
    """ InvoiceDetail model. """
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product")
    prepaid_card = models.ForeignKey(
        PrepaidCard,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="prepaid_card")
    quantity = models.IntegerField(default=1)
    vat = models.IntegerField(
        choices=VAT_CHOICES,
        default=VAT_CHOICES.GENERAL
    )
    discount = models.IntegerField(default=0)
    payment_method = models.CharField(
        choices=PAYMENT_METHODS,
        default=PAYMENT_METHODS.CASH,
        max_length=255
    )

    class Meta:
        """ No InvoiceDetail with same Invoice.id. """
        unique_together = ['invoice', 'id']

    def __unicode__(self):
        return 'Invoice: ' + str(self.invoice.id) + ' Invoice detail: ' + str(self.id)
