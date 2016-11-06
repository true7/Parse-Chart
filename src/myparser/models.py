from django.db import models


class ParsedData(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.region

