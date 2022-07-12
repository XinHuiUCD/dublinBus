from django.db import models

# Create your models here.

class Bus(models.Model):
    routeId = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.routeId
