from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ServiceCreateView, ServiceDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^services/$', ServiceCreateView.as_view(), name="service-create"),
    url(r'^services/(?P<pk>[0-9]+)/$', ServiceDetailsView.as_view(), name="service-details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)