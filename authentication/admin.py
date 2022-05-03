from django.contrib import admin
from authentication.models import Driver, Customer, User

# Register your models here.
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Customer)