from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientCreateView, ClientDetailsView

urlpatterns = {
    url(r'^clients/$', ClientCreateView.as_view(), name="client-create"),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailsView.as_view(), name="client-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)