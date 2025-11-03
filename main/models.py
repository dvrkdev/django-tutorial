from django.db import models


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
