from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AppointmentCreateView, AppointmentDetailsView

urlpatterns = {
    url(r'^appointments/$', AppointmentCreateView.as_view(), name="appointment-create"),
    url(r'^appointments/(?P<pk>[0-9]+)/$', AppointmentDetailsView.as_view(), name="appointment-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)