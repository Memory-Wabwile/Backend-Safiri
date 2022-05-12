from django import forms
from django.contrib.auth.forms import UserCreationForm
from customers.models import Booking, BusBooking


class BusBookingForm(forms.ModelForm):
    class Meta:
        model = BusBooking
        
        fields ='__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
       
        fields ='__all__'