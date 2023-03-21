from django.db import models

# Create your models here.
class Airport(models.Model):
    #properties here
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    #properties here
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # return the string representation of the object
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    #properties here
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    #representation string of passenger
    def __str__(self):
        return f"{self.first} {self.last}"




