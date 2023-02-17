from django.shortcuts import render
from . models import User, Vehicle
from . serializers import UserSerializer, VehicleSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import RoleBasedPermission
# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VehicleView(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated and RoleBasedPermission]






