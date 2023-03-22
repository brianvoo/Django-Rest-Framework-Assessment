from django.urls import path
from .views import DriverList, DriverDetail, DriverCreate

urlpatterns = [
    # Return a list of available drivers, allow filtering using a driver's email, mobile_number, langeuage and his truck's number_plate
    path('', DriverList.as_view()),

    # Return a single driver
    path('<int:pk>/', DriverDetail.as_view()),

    # Create a single driver
    path('create/', DriverCreate.as_view()),
]