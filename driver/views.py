from rest_framework import generics

from .models import Truck, Driver
from .serializers import TruckSerializer, DriverSerializer

# Return a list of available drivers, allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate
class DriverList(generics.ListAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        driver = self.request.query_params.get('driver')
        if driver is not None:
            queryset = queryset.filter(driverName=driver)
        return queryset

# Return a single driver, added feature to update and delete
class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

# Create a single driver
class DriverCreate(generics.CreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

# Create a single truck
class TruckCreate(generics.CreateAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

# Return single truck, added feature to update and delete
class TruckDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

# Return list of trucks
class TruckList(generics.ListAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()