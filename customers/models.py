from unicodedata import category
from django.db import models, router
from django.utils import timezone
from django.db.models import Sum

from driver.models import Schedule


class Booking(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    seats = models.IntegerField()
    status = models.CharField(max_length=2, choices=(('1','Pending'),('2','Paid')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code + ' - ' + self.name)

    def total_payable(self):
        return self.seats * self.schedule.fare

    def count_available(self):
        booked = Booking.objects.filter(schedule=self).aggregate(Sum('seats'))['seats__sum']
        return self.bus.seats - booked

    @classmethod
    def update_booking(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def save_bus(self):
        self.save()

    @classmethod
    def delete_bus(cls, id):
        cls.objects.filter(id=id).delete()


class BusBooking(models.Model):
    user_name=models.CharField(max_length=100)
    phone_no=models.IntegerField(default=+254-700-000-000)
    user_id=models.IntegerField(default=0)
    departure_point = models.CharField(max_length=100)
    pick_up_station=models.CharField(max_length=100,default='Home station')
    destination=models.CharField(max_length=30)
    date=models.DateField()
    price=models.IntegerField()
    time=models.TimeField()
    no_of_seats=models.IntegerField(default=0)
    bus_name=models.CharField(max_length=20)
    bus_id=models.IntegerField()
    seat_numbers=models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.date)