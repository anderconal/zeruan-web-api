from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductCreateView, PrepaidCardCreateView, ProductDetailsView, PrepaidCardDetailsView

urlpatterns = {
    url(r'^products/$', ProductCreateView.as_view(), name="product-create"),
    url(r'^prepaid-cards/$', PrepaidCardCreateView.as_view(), name="prepaid-card-create"),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailsView.as_view(), name="product-details"),
    url(r'^prepaid-cards/(?P<pk>[0-9]+)/$', PrepaidCardDetailsView.as_view(), name="prepaid-card-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)