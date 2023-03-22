from rest_framework import serializers
from .models import Truck, Driver

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('__all__')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('__all__')