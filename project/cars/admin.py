from django.contrib import admin

from .models import Car, Owner, Color

admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Color)