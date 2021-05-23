from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=True)
class SearchResults(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "link"

    def __str__(self):
        return self.name