from rest_framework import serializers
from .models import Booking, BusBooking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BusBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusBooking
        fields = '__all__'