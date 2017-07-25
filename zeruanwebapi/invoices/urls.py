from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InvoiceCreateView, InvoiceDetailsView

urlpatterns = {
    url(r'^invoices/$', InvoiceCreateView.as_view(), name="invoice-create"),
    url(r'^invoices/(?P<pk>[0-9]+)/$', InvoiceDetailsView.as_view(), name="invoice-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)