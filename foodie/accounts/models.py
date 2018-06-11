from __future__ import unicode_literals
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    PermissionsMixin,
    BaseUserManager,
    AbstractUser
)
from django.contrib.auth.models import UserManager
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True,max_length=25)
    email = models.EmailField(unique=True,max_length=254 )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def full_name(self):
        full_name = '%s %s' % (self.last_name.upper(), self.first_name)
        return full_name.strip()

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    postal_code = models.EmailField(max_length=255 )

class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
    message="Phone number must be entered in the format: '7543036718'. Up to 10 digits allowed.")
    phone = models.CharField(
    validators=[phone_regex], max_length=10)  # validators should be a list


class Organization(Group):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='org_admin')
    phone = models.ForeignKey(PhoneNumber, related_name='org_phone_number')
    email = models.EmailField(unique=True,max_length=255 )
    address = models.ForeignKey(Address, related_name='org_address')
    logo = models.ImageField(upload_to='organization/', blank=False )

    def __str__(self):
        return self.name

class Delivery(Group):
    member = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='delivery_member')
    phone = models.ForeignKey(PhoneNumber, related_name='delivery_phone_number')
    email = models.EmailField(unique=True,max_length=255 )
    address = models.ForeignKey(Address, related_name='delivery_address')
    logo = models.ImageField(upload_to='organization/', blank=False )

    def __str__(self):
        return self.name




# class OrganizationBio(models.Model):
#     member = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='org_member')
#     Phone = models.CharField(max_length=15)
#     email = models.EmailField(unique=True,max_length=255 )
#     address = models.CharField(max_length=255)
#     Logo = models.ImageField(upload_to='organization/', blank=False )


# class ClientBio(models.Model):
#     client = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='client')
#
# class DeliveryBio(models.Model):
#     delivery = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='delivery_member')
