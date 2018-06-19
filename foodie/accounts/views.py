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
<<<<<<< HEAD
import time
import calendar

    # FACEBOOK LOGIN API
=======

# fb keys
>>>>>>> d3258e0e9d8ccaa19a5ade6fd757bea2cbec884c
# be236d1e9948c7a867d2afd92e0b400a secret key
# 592084927852037 app id

    # SAFARICOM MPESA API
#Consumer Key	I0wWQjGA6V8SDyZiAlgKmeFz3cKMp7nM
#Consumer Secret	nWDVI12ltFdJaobx


# Create your views here.

class UserCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)

class OrgCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrgCreateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Organization.objects.all()

    def post(self, request, format=None):
        serializer = OrgCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)



class OrgRetrieveAPIView(generics.ListCreateAPIView):
    serializer_class = OrgCreateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Organization.objects.all()

    def get(self, request, format=None):
        org = Organization.objects.all().values("id","name","email","admin_id__username","admin_id")
        return Response(data={"Organizations":org}, status=status.HTTP_200_OK)


class MakeSafPaymentAPIView(APIView):
    serializer_class = MpesaOauthSerializer
    permission_classes = [permissions.AllowAny]
    queryset = MpesaOauth.objects.all()

    def get(self, request, format=None):
        consumer_key = "I0wWQjGA6V8SDyZiAlgKmeFz3cKMp7nM"
        consumer_secret = "nWDVI12ltFdJaobx"
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        res = r.json()
        expires_in = res["expires_in"]
        access_token = res["access_token"]

        oauth_obj = MpesaOauth(
            access_token=access_token,
            expires_in=expires_in,
        )
        oauth_obj.save()

        return Response(data=res,status=status.HTTP_200_OK)


class GetSafPaymentTokenAPIView(generics.ListAPIView):
    serializer_class = MpesaOauthSerializer
    permission_classes = [permissions.AllowAny]
    queryset = MpesaOauth.objects.all()

    def get(self, request, format=None):
        credentials = MpesaOauth.objects.all().values("id","expires_in","access_token")
        return Response(data={"Credentials":credentials}, status=status.HTTP_200_OK)

class PaymentsApiView(APIView):
    # serializer_class = MpesaOauthSerializer
    permission_classes = [permissions.AllowAny]
    queryset = MpesaOauth.objects.all()

    def get(self,request,format=None):
        credentials = MpesaOauth.objects.filter(id=4).values("id","expires_in","access_token")
        print(credentials[0]["access_token"])
        access_token = credentials[0]["access_token"]
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        # timestamp start with year month date
        # time_stamp =  datetime.datetime.now().timestamp()
        time_stamp = calendar.timegm(time.gmtime())
        time_stamp = str(time_stamp)
        # time_stamp = str(datetime.datetime.now())
        password = str(access_token+time_stamp)
        # print(password)
        # password = base64.urlsafe_b64encode()
        # print(password)

        # request = {
        #   "BusinessShortCode": "174379",
        #   "Password": password;
        #   # "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNTE1MjIzNDEy",
        #   "Timestamp": "20180515223412",
        #   # "Timestamp": "20180515223412",
        #   "TransactionType": "CustomerPayBillOnline",
        #   "Amount": "34",
        #   "PartyA": "254722241161",
        #   "PartyB": "174379",
        #   "PhoneNumber": "254722241161",
        #   "CallBackURL": "https://121a0a23.ngrok.io/",
        #   "AccountReference": "BOCHIE LTD",
        #   "TransactionDesc": "Payment"
        # }
        #
        # response = requests.post(api_url, json = request, headers=headers)
        #
        # print (response.json())
        return Response(data=password, status=status.HTTP_200_OK)


        # access_token = credentials[0]["access_token"]
        # api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        # headers = {"Authorization": "Bearer %s" % access_token}
        # request = { "ShortCode": "600729",
        #     "ResponseType": "Application/json",
        #     "ConfirmationURL": "https://121a0a23.ngrok.io/",
        #     "ValidationURL": "https://121a0a23.ngrok.io/"}
        #
        # response = requests.post(api_url, json = request, headers=headers)
        #
        # print (response.json())
        # return Response(data=response.json(),status=status.HTTP_200_OK)
