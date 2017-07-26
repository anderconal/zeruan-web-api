from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientCreateView, ClientDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^clients/$', ClientCreateView.as_view(), name="client-create"),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailsView.as_view(), name="client-details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)