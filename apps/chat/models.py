from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Rooms(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, default=None)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
