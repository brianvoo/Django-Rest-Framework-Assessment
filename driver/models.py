from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Validator
alpha_validator = RegexValidator(regex='^[a-zA-Z]+([-][a-zA-Z]+)?$', message='Only alphabets allowed.')
truck_validator = RegexValidator(regex='^[a-zA-Z0-9]+$', message='Please enter valid format.')
phone_validator = RegexValidator(regex='^[0-9]{10,11}$', message='Please input digits only.')

class Truck(models.Model):
    number_plate = models.CharField(max_length=50, unique=True, verbose_name="Number Plate", validators=[truck_validator])
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="Registration Number", validators=[truck_validator])
    truck_added = models.DateField(auto_now_add=True, verbose_name="Truck Added")

    def __str__(self):
        return self.number_plate
    
def get_default_status():
    """ get a default value; create if not available """
    return Truck.objects.get_or_create(number_plate="Not Assigned", registration_number="Not Assigned")[0]

class Driver(models.Model):
    # Field Choices
    LANGUAGES = (
        ('EN', 'English'),
        ('MS', 'Malay'),
        ('ZH', 'Chinese'),
        ('OTHER', 'Other'),
    )
    # City and District choice

    # Fields
    driverName = models.CharField(max_length=100, verbose_name="Driver Name", validators=[alpha_validator])
    mobile_number = models.CharField(max_length=20, verbose_name="Mobile Number", validators=[phone_validator])
    email = models.EmailField(verbose_name="Email", unique=True)
    city = models.CharField(max_length=50, verbose_name="City", validators=[alpha_validator])
    district = models.CharField(max_length=50, verbose_name="District", validators=[alpha_validator])
    language = models.CharField(max_length=50, verbose_name="Language", choices=LANGUAGES)
    assigned_truck = models.ForeignKey(Truck, default=get_default_status, on_delete=models.SET_DEFAULT, verbose_name="Assigned Truck")
    driver_added = models.DateField(auto_now_add=True, verbose_name="Driver Added")

    def __str__(self):
        return self.driverName