from django.contrib import admin

from .models import Car, Owner

admin.site.register(Car)
admin.site.register(Owner)