from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    url(r'api-auth/', views.obtain_auth_token),
    url(r'^account/', include('accounts.urls', namespace='account')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', admin.site.urls),
]
