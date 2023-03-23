from django.db import models

class Truck(models.Model):
    number_plate = models.CharField(max_length=50, unique=True)
    registration_plate = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.number_plate
    
def get_default_status():
    """ get a default value for action status; create new status if not available """
    return Truck.objects.get_or_create(number_plate="Not Assigned", registration_plate="Not Assigned")[0]

class Driver(models.Model):
    driverName = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    assigned_truck = models.ForeignKey(Truck, default=get_default_status, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.driverName