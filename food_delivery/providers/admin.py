from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Restaurants)
admin.site.register(Delivery_partners)