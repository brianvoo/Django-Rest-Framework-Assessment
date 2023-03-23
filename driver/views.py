from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Truck, Driver
from .serializers import TruckSerializer, DriverSerializer

# Driver
# Create a single driver
class DriverCreate(generics.CreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

# Return a single driver
class DriverDetail(generics.RetrieveAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

# Return a list of available drivers, allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate
class DriverList(generics.ListAPIView):
    serializer_class = DriverSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    def get_queryset(self):
        queryset = Driver.objects.all()
        
        driver = self.request.query_params.get('driver')
        if driver is not None:
            queryset = queryset.filter(driverName=driver)
        return queryset

    filterset_fields = (
        'driverName',
        'mobile_number',
        'email',
        'language',
        'driver_added',
    )

# Update or delete single driver
class DriverUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


# Truck
# Create a single truck
class TruckCreate(generics.CreateAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

# Return single truck
class TruckDetail(generics.RetrieveAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

# Return list of trucks
class TruckList(generics.ListAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'truck_added',
    )

# Update or delete single truck
class TruckUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()