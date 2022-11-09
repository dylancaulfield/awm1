import json

from django.contrib.gis.db import models
from django.conf import settings


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField()

    def __str__(self):
        return self.name
