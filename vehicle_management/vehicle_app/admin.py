from django.contrib import admin
from .models import User, Vehicle
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'user_type']


admin.site.register(User, UserAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']


admin.site.register(Vehicle, VehicleAdmin)
