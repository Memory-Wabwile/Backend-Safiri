from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_driver = models.BooleanField(default=False)
  is_customer= models.BooleanField(default=False)

class Driver(models.Model):
    driver = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.driver.username

class Customer(models.Model):
    customer = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.customer.username  
