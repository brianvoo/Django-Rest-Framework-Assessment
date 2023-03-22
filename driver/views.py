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

# Return a single driver
class DriverDetail(generics.RetrieveAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


# Create a single driver
class DriverCreate(generics.UpdateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

# RetrieveUpdateDestroyAPIVIew Used for read-write-delete endpoints to represent a single model instance.
# class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = DriverSerializer
#     queryset = Driver.objects.all()

# ListCreateAPIView Used for read-write endpoints to represent a collection of model instances.
# class DriverCreate(generics.ListCreateAPIView):
#     serializer_class = DriverSerializer

#     def get_queryset(self):
#         queryset = Driver.objects.all()
#         driver = self.request.query_params.get('driver')
#         if driver is not None:
#             queryset = queryset.filter(driverName=driver)
#         return queryset