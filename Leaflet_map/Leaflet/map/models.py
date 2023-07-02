from django.db import models
from django.contrib.gis.db import models

class Node(models.Model):
    location = models.PointField()

class Poly(models.Model):
    location = models.PolygonField()