from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # Returns a string representation of the object
    def __str__(self) -> str:
        return f"{self.id}: {self.origin} to {self.destination}"
