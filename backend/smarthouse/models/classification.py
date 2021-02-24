from django.db import models


class Classification(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title
