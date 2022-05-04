from django.contrib import admin
from driver.models import Schedule,Category, Location, Bus

# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Schedule)

