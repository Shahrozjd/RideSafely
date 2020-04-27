from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='media/default.jpg')
    address = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=31, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
