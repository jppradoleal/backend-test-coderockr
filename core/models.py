from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
  ...


class Investment(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  amount = models.FloatField()
  active = models.BooleanField(default=True, null=False)
  created_at = models.DateTimeField()