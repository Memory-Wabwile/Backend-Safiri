from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/busbooking/', views.BusBookingList.as_view()),
]
