from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
