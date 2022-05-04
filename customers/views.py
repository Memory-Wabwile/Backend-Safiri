from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, BusBooking
from .serializer import BookingSerializer, BusBookingSerializer

# Create your views here.

class BusBookingList(APIView):
    def get(self, request, format=None):
        all_booking = BusBooking.objects.all()
        serializers = BusBookingSerializer(all_booking, many=True)
        return Response(serializers.data)


    def get_single_item_busbooking(self, pk):
        try:
            return BusBooking.objects.get(pk=pk)
        except BusBooking.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = BusBookingSerializer(merch)
        return Response(serializers.data)
