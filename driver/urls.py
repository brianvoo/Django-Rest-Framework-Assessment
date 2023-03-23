from django.urls import path
from .views import DriverList, DriverDetail, DriverCreate, TruckCreate, TruckList, TruckDetail, DriverUpdateDelete, TruckUpdateDelete

urlpatterns = [
    # Driver
    # Create a single driver
    path('driver/create/', DriverCreate.as_view()),

    # Return a single driver
    path('driver/<int:pk>/', DriverDetail.as_view()),

    # Return a list of available drivers, allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate
    path('driver/', DriverList.as_view()),

    # Update single driver
    path('driver/<int:pk>/update/', DriverUpdateDelete.as_view()),


    # Truck
    # Create a single truck
    path('truck/create/', TruckCreate.as_view()),

    # View single truck
    path('truck/<int:pk>/', TruckDetail.as_view()),

    # Return list of trucks
    path('truck/', TruckList.as_view()),

    # Update single truck
    path('truck/<int:pk>/update/', TruckUpdateDelete.as_view()),
]