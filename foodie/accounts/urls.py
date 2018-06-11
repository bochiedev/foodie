from django.conf.urls import url
from django.contrib import admin
from .views import *

# for images
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^organization/register/$', OrgCreateAPIView.as_view(), name='register_org'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
