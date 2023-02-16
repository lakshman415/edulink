from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    # image = models.ImageField(upload_to='media/resources/')



