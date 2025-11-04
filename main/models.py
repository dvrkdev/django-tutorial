from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ok = models.BooleanField(default=False)  # user is OK!
    bio = models.TextField(max_length=300, blank=True, null=True)  # user bio

    def __str__(self):
        return f"{self.username} {self.ok}"


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.price}"


class Reservation(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    guest_count = models.PositiveIntegerField(default=0)
    reservation_time = models.DateField(auto_now=True)
    comments = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title[:50]} ..."
