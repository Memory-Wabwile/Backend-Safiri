from rest_framework import serializers
from .models import  Bus

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    bus_image = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Bus
        fields = '__all__'
        
    def get_image_url(self, obj):
        return obj.bus_image.url

# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = '__all__'

# class Vehicle_ownerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicle_owner
#         fields = '__all__'
