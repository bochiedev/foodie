from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.mixins import *
from rest_framework.generics import *
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from requests.auth import HTTPBasicAuth
import base64
import datetime

# Create your views here.

class STKPayAPIView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self,request,format=None):

        consumer_key = "I0wWQjGA6V8SDyZiAlgKmeFz3cKMp7nM"
        consumer_secret = "nWDVI12ltFdJaobx"
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        print (r.json())

        access_token = r.json()['access_token']


class STKPayAPIView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self,request,format=None):

        consumer_key = "I0wWQjGA6V8SDyZiAlgKmeFz3cKMp7nM"
        consumer_secret = "nWDVI12ltFdJaobx"
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        print (r.json())

        access_token = r.json()['access_token']
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        business_short_code = "174379"
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        str = business_short_code + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"+ timestamp
        password = base64.b64encode(str.encode())

        request = {
          "BusinessShortCode": business_short_code,
          "Password": password,
          "Timestamp": timestamp,
          "TransactionType": "CustomerPayBillOnline",
          "Amount": "1",
          "PartyA": "254722241161",
          "PartyB": "174379",
          "PhoneNumber": "254722241161",
          "CallBackURL": "http://www.bochie.co.ke",
          "AccountReference": "bochie ltd",
          "TransactionDesc": "payment"
        }

        response = requests.post(api_url, json = request, headers=headers)

        print (response)
        return Response(data=response.json(), status=status.HTTP_200_OK)
        # return Response(data=password, status=status.HTTP_200_OK)
