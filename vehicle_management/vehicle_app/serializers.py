from rest_framework import serializers
from . models import User, Vehicle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'user_type']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


