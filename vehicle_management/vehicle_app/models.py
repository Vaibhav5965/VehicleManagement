from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import isalphavalidator
# Create your models here.


class User(AbstractUser):

    USER_TYPE_CHOICES = [
        ('SA', 'Super Admin'),
        ('AD', 'Admin'),
        ('SU', 'user')
    ]
    user_type = models.CharField(max_length=70, choices=USER_TYPE_CHOICES, null=True, default=None)


class Vehicle(models.Model):

    TYPE_OF_WHEELS = [
        (2, 'Two Wheeler'),
        (3, 'Three Wheeler'),
        (4, 'Four Wheeler')
    ]
    vehicle_number = models.CharField(max_length=70, validators=[isalphavalidator], blank=False, null=False)
    vehicle_type = models.IntegerField(choices=TYPE_OF_WHEELS, default=None)
    vehicle_model = models.CharField(max_length=70)
    vehicle_description = models.CharField(max_length=70)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False, null=False)
