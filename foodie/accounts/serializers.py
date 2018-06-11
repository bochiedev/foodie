from rest_framework import serializers
from .models import *

from django.contrib.contenttypes.models import ContentType
from .models import *
from django.contrib.auth import get_user_model


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email field')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]


    extra_kwargs = {"password":
                    {"write_only": True}
                    }

    def validate(self, data):
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")

        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("This email is taken")

        return value

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get("username")

        username_exist = User.objects.filter(username=username)
        if username_exist.exists():
            raise serializers.ValidationError("This username is taken")

        return value

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }


class OrgCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email field')

    class Meta:
        model = Organization
        fields = [
            'id',
            'admin',
            'name',
            'email',
            'phone',
            'address',
            'logo'
        ]

    def validate(self, data):
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")

        org_qs = Organization.objects.filter(email=email)
        if org_qs.exists():
            raise serializers.ValidationError(
                "organization with this email exists")

        return value

    def validate_name(self, value):
        data = self.get_initial()
        name = data.get("name")

        name_exist = Organization.objects.filter(name=name)
        if name_exist.exists():
            raise serializers.ValidationError("This organization is exists")

        return value

    def create(self, validated_data):
        name = validated_data['name']
        admin = validated_data['admin']
        phone = validated_data['phone']
        email = validated_data['email']
        address = validated_data['address']
        logo = validated_data['logo']

        org_obj = Organization(
            name=name,
            admin=admin,
            phone=phone,
            email=email,
            logo=logo,
            address=address,
        )
        org_obj.save()
        return validated_data
