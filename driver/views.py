from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Category, Location, Bus, Schedule
from .serializer import CategorySerializer, LocationSerializer, BusSerializer, ScheduleSerializer,Vehicle_ownerSerializer
from .permissions import IsAdminOrReadOnly
from .decorators import allowed_users

# Create your views here.

#........
class CategoryList(APIView):
    def get(self, request, format=None):
        all_category = Category.objects.all()
        serializers = CategorySerializer(all_category, many=True)
        return Response(serializers.data)

    @allowed_users(allowed_roles=['driver','admin'])
    def post(self, request, format=None):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationList(APIView):
    def get(self, request, format=None):
        all_location = Location.objects.all()
        serializers = LocationSerializer(all_location, many=True)
        return Response(serializers.data)

    @allowed_users(allowed_roles=['driver','admin'])
    def post(self, request, format=None):
        serializers = LocationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusList(APIView):
    def get(self, request, format=None):
        all_bus = Bus.objects.all()
        serializers = BusSerializer(all_bus, many=True)
        return Response(serializers.data)

    @allowed_users(allowed_roles=['driver','admin'])
    def post(self, request, format=None):
        serializers = BusSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ScheduleList(APIView):
    def get(self, request, format=None):
        all_schedule = Schedule.objects.all()
        serializers = ScheduleSerializer(all_schedule, many=True)
        return Response(serializers.data)

    @allowed_users(allowed_roles=['driver','admin'])
    def post(self, request, format=None):
        serializers = ScheduleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class Vehicle_ownerList(APIView):
    def get(self, request, format=None):
        all_schedule = Schedule.objects.all()
        serializers = Vehicle_ownerSerializer(all_schedule, many=True)
        return Response(serializers.data)

    @allowed_users(allowed_roles=['driver','admin'])
    def post(self, request, format=None):
        serializers = Vehicle_ownerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
