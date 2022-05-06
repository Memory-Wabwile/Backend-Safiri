from unicodedata import category
from django.db import models, router
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import User

from driver.models import Bus, Schedule


class BusBooking(models.Model):
    user_name=models.CharField(max_length=100)
    phone_no=models.IntegerField(default=+254-700-000-000)
    departure_point = models.CharField(max_length=100)
    destination=models.CharField(max_length=30)
    date=models.DateField()
    price=models.IntegerField()
    time=models.TimeField()
    no_of_seats=models.IntegerField(default=0)
    bus_id=models.ForeignKey(Bus,on_delete=models.CASCADE, related_name="bus_id")

    def __str__(self):
        return str(self.date)
    
    @classmethod
    def add_busbooking(self):
        self.save()

    @classmethod
    def update_busbooking(cls, id):
        cls.objects.filter(id=id).update()
    
    @classmethod
    def delete_busbooking(cls, id):
        cls.objects.filter(id=id).delete()



# class Booking(models.Model):
#     code = models.CharField(max_length=100)
#     name = models.CharField(max_length=250)
#     schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
#     seats = models.IntegerField()
#     status = models.CharField(max_length=2, choices=(('1','Available'),('2','Not Available')), default=1)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.code + ' - ' + self.name)

#     def total_payable(self):
#         return self.seats * self.schedule.fare

#     def count_available(self):
#         booked = Booking.objects.filter(schedule=self).aggregate(Sum('seats'))['seats__sum']
#         return self.bus.seats - booked

#     @classmethod
#     def update_booking(cls, id):
#         cls.objects.filter(id=id).update()

#     @classmethod
#     def save_bus(self):
#         self.save()

#     @classmethod
#     def delete_bus(cls, id):
#         cls.objects.filter(id=id).delete()