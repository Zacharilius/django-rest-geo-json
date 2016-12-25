from django.contrib.gis.db import models


class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = models.PointField()


class Line(models.Model):
    """
    A model which holds information about a particular location
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    line = models.LineStringField()
