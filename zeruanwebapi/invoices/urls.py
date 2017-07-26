from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InvoiceCreateView, InvoiceDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^invoices/$', InvoiceCreateView.as_view(), name="invoice-create"),
    url(r'^invoices/(?P<pk>[0-9]+)/$', InvoiceDetailsView.as_view(), name="invoice-details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)