from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/category/', views.CategoryList.as_view()),
    path('api/location/', views.LocationList.as_view()),
    path('api/bus/', views.BusList.as_view()),
    path('api/schedule/', views.ScheduleList.as_view()),
    path('api/booking/', views.BookingList.as_view()),
]

