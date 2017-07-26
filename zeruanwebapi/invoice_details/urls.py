from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InvoiceDetailCreateView, InvoiceDetailDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^invoice-details/$', InvoiceDetailCreateView.as_view(), name="invoice-detail-create"),
    url(r'^invoice-details/(?P<pk>[0-9]+)/$', InvoiceDetailDetailsView.as_view(), name="invoice-detail-details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
