from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from authentication.models import AbstractUser
from django.contrib.auth import authenticate
from rest_framework.response import Response


class DriverCustomRegistrationSerializer(RegisterSerializer):
   
    def get_cleaned_data(self):
            data = super(DriverCustomRegistrationSerializer, self).get_cleaned_data()
            return data

    def save(self, request):
        user = super(DriverCustomRegistrationSerializer, self).save(request)
        user.is_driver = True
        user.save()
        return user

class CustomerCustomRegistrationSerializer(RegisterSerializer):
    def get_cleaned_data(self):
            data = super(CustomerCustomRegistrationSerializer, self).get_cleaned_data()
            return data

    def save(self, request):
        user = super(CustomerCustomRegistrationSerializer, self).save(request)
        user.is_customer = True
        user.save()
        return user  

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128)
