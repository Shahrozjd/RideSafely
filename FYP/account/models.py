from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    challans = models.PositiveIntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.challans)