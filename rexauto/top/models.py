from django.db import models

# Create your models here.

class Station(models.Model):
    StationNumber = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.StationNumber
