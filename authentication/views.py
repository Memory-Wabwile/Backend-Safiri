from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from authentication.serializers import (
    DriverCustomRegistrationSerializer, CustomerCustomRegistrationSerializer,
     LoginSerializer
     
    )
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView  
from rest_framework.authtoken.models import Token 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User, Driver, Customer


#create your views here
class DriverRegistrationView(RegisterView):
    serializer_class = DriverCustomRegistrationSerializer


class CustomerRegistrationView(RegisterView):
    serializer_class = CustomerCustomRegistrationSerializer


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key

        else:
            data = serializer.errors

        return Response(data)

class LogoutView(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': ('User logged out.')}
        return Response(content)

class LogoutView(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': ('User logged out.')}
        return Response(content)