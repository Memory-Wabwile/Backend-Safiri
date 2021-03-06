from django.http import Http404
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import  BusBooking
from .serializer import  BusBookingSerializer
from .decorators import allowed_users


# Create your views here.

# @allowed_users(allowed_roles=['driver','admin', 'customer'])
class BusBookingList(APIView):
    def get(self, request, format=None):
        all_booking = BusBooking.objects.all()
        serializers = BusBookingSerializer(all_booking, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BusBookingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def get_single_item_busbooking(self, pk):
    #     try:
    #         return BusBooking.objects.get(pk=pk)
    #     except BusBooking.DoesNotExist:
    #         return Http404

    # def get(self, request, pk, format=None):
    #     merch = self.get_merch(pk)
    #     serializers = BusBookingSerializer(merch)
    #     return Response(serializers.data)
