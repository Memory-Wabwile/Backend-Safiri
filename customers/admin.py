from django.contrib import admin
from customers.models import Booking, BusBooking

# Register your models here.

admin.site.register(Booking)
admin.site.register(BusBooking)

