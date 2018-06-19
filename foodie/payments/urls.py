from django.conf.urls import url
from django.contrib import admin
from .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^mpesa_token/$', alance.as_view(), name='get_token'),
    # url(r'^token_refresh/$', RefreshTokenAPIView.as_view(), name='refresh_token'),
    url(r'^mpesa/stk/$', STKPayAPIView.as_view(), name='stk_push'),
    # url(r'^mpesa/stk_query/$', STKQueryAPIView.as_view(), name='stk_push_query'),
    # url(r'^mpesa/consumer_to_business/$', C2BPayAPIView.as_view(), name='c2b'),
    # url(r'^mpesa/business_to_consumer/$', B2CPayAPIView.as_view(), name='btc'),
    # url(r'^mpesa/business_to_business/$', B2BPayAPIView.as_view(), name='btb'),
    # url(r'^mpesa/reversal/$', ReverseAPIView.as_view(), name='reversal'),
    # url(r'^mpesa/balance/$', BalancesAPIView.as_view(), name='balance'),






]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
