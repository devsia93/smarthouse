from django.db import models

from smarthouse.models.sensor import Sensor


class Indication(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='indications')
    value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.sensor.title}:{self.value}'
