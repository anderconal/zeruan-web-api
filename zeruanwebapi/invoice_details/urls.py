from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InvoiceDetailCreateView, InvoiceDetailDetailsView

urlpatterns = {
    url(r'^invoice-details/$', InvoiceDetailCreateView.as_view(), name="invoice-detail-create"),
    url(r'^invoice-details/(?P<pk>[0-9]+)/$', InvoiceDetailDetailsView.as_view(), name="invoice-detail-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
