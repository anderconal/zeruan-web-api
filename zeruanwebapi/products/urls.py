from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductCreateView, PrepaidCardCreateView

urlpatterns = {
    url(r'^products/$', ProductCreateView.as_view(), name="product-create"),
    url(r'^prepaid-cards/$', PrepaidCardCreateView.as_view(), name="prepaid-card-create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)