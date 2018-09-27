from django.db import models
from django.contrib.auth.models import User


class Rooms(models.Model):
    name = models.CharField(max_length=255)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
