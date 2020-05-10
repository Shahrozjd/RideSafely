from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    challans = models.PositiveIntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.challans)

class due(models.Model):
    months= models.CharField(max_length=30)
    paid = models.PositiveIntegerField()
    unpaid = models.PositiveIntegerField()
    def __str__(self):
        return "{}-{}".format(self.months, self.paid,self.unpaid)