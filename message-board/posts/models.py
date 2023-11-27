from django.db import models

# Create your models here.

class Post(models.Model):
    # create a text field
    text = models.TextField()

    # add __str__
    def __str__(self) -> str:
        return self.text[:50]
