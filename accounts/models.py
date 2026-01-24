from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    location = models.CharField(max_length=200, null=True, blank=True)
    github_link = models.URLField(max_length=500, null=True, blank=True)
    linkedin_link = models.URLField(max_length=500, null=True, blank=True)
    x_link = models.URLField(max_length=500, null=True, blank=True)
    website_link = models.URLField(max_length=500, null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
