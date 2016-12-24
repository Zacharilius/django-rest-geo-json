from django.contrib.gis.db import models


# Create your models here.
class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = models.PointField()
