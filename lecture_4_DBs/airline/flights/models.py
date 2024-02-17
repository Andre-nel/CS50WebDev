from django.db import models


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} to {self.code}"


# python manage.py makemigrations
# python manage.py migrate
class Flight(models.Model):
    # related_name when you want to access the flight information from the Airport class
    origin = models.ForeignKey(to=Airport, on_delete=models.CASCADE,
                               related_name="departures")
    destination = models.ForeignKey(to=Airport, on_delete=models.CASCADE,
                                    related_name="arrivals")
    duration = models.IntegerField()

    # Returns a string representation of the object
    def __str__(self) -> str:
        return f"{self.id}: {self.origin} to {self.destination}"
