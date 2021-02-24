from django.db import models

from smarthouse.models.classification import Classification
from smarthouse.models.room import Room


class Sensor(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='sensors')
    classification = models.ForeignKey(Classification, on_delete=models.SET_NULL, null=True, related_name='sensors')
    model = models.CharField(max_length=8)
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=8)

    def __str__(self):
        return self.title
