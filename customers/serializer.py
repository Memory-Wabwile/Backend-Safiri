from rest_framework import serializers
from .models import BusBooking

# class BookingSerializer(serializers.ModelSerializer):
#    
#         model = Booking
#         fields = '__all__'

class BusBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusBooking
        fields = '__all__'