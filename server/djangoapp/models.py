# Uncomment the following imports before adding the Model code

from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_year(value: int):
    current_year = date.today().year
    if  (current_year - 100) < value <= (current_year + 100):
        raise ValidationError(
            _("The year %(value)s is not within the +/-100 range of the current year"),
            params={"value": value},
        )

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    # brand/manufacturer name
    name = models.CharField(max_length=200, unique=True) 
    description = models.TextField()
    country = models.CharField(max_length=150)
    founded_on = models.DateField(default=date.today)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    class CarType(models.TextChoices):
        SEDAN = "SEDAN", _("Sedan")
        SUV = "SUV", _("SUV")
        WAGON = "WAGON", _("Wagon")
        TRUCK = "TRUCK", _("Truck")
        VAN = "VAN", _("Van")
        HYBRID = "HYBRID", _("Hybrid")
        ELECTRIC = "ELECTRIC", _("Electric")

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Dealer Id (stored in Cloudant, but here as an Integer)
    dealer_id = models.IntegerField(blank=True, null=True, validators=[
        MinValueValidator(limit_value=1, message="Value must be greater than zero")])
    name = models.CharField(max_length=200, unique=True)
    car_type = models.CharField(max_length=50, choices=CarType.choices)
    year = models.IntegerField(validators=[validate_year]) # Manufacturing Year
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

