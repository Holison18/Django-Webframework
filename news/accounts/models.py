from django.contrib.auth.models import AbstractUser
from django.db import models


# create custome user model
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
