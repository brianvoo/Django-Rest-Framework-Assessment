from django.urls import path
from .views import DriverList, DriverDetail, DriverCreate, TruckCreate, TruckList, TruckDetail

urlpatterns = [
    # Return a list of available drivers, allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate
    path('driver/', DriverList.as_view()),

    # Return a single driver
    path('driver/<int:pk>/', DriverDetail.as_view()),

    # Create a single driver
    path('driver/create/', DriverCreate.as_view()),

    # Create a single truck
    path('truck/create/', TruckCreate.as_view()),

    # View truck ID
    path('truck/<int:pk>/', TruckDetail.as_view()),

    # Return list of trucks
    path('truck/', TruckList.as_view()),
]