from django.db import models

# Create your models here.


# Add a model to accept text
class Post(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]
