from django.db import models

# Create your models here.


# Add a model to accept text
class post(models.Model):
    text = models.TextField()
