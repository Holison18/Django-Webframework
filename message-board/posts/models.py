from django.db import models

# Create your models here.


# Add a model to accept text
class posts(models.Model):
    text = models.TextField()
