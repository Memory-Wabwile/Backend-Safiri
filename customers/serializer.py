from rest_framework import serializers
from .models import BusBooking

class BusBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusBooking
        fields = '__all__'