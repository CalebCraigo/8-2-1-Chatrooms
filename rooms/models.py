from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rooms:list')


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('rooms:detail')
