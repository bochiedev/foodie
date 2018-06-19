from django.conf.urls import url
from django.contrib import admin
from .views import *

# for images
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^org/register/$', OrgCreateAPIView.as_view(), name='register_org'),
    url(r'^org/list/$', OrgRetrieveAPIView.as_view(), name='view_org'),
    url(r'^payment/pay/$', PayAPIView.as_view(), name='pay'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
