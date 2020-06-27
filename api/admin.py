from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)
admin.site.register(models.Restaurant)
admin.site.register(models.Reservation)
admin.site.register(models.Invoice)
