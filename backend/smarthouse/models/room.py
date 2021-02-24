from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title
