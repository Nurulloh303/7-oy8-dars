from django.db import models
from django.core.validators import MinValueValidator

class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="Color")
    def __str__(self):
        return f"{self.name}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('petrol', 'Benzin'),
            ('diesel', 'Dizel'),
            ('electric', 'Elektro'),
            ('hybrid', 'Gibrid'),
        ]
    )
    mileage = models.IntegerField(validators=[MinValueValidator(0)])
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} {self.brand}"

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    phone_number = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

