from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # location of the uploaded image will be in MEDIA_ROOT/images
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username
