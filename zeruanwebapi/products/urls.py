from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductCreateView, PrepaidCardCreateView, ProductDetailsView, PrepaidCardDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^products/$', ProductCreateView.as_view(), name="product-create"),
    url(r'^prepaid-cards/$', PrepaidCardCreateView.as_view(), name="prepaid-card-create"),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailsView.as_view(), name="product-details"),
    url(r'^prepaid-cards/(?P<pk>[0-9]+)/$', PrepaidCardDetailsView.as_view(), name="prepaid-card-details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)