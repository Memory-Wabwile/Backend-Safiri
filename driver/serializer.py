from rest_framework import serializers
from .models import Category, Location, Bus, Schedule, Vehicle_owner

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class Vehicle_ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_owner
        fields = '__all__'
