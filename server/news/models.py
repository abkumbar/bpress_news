from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=500)
    headline = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
    date_published = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField(help_text='Main article text')
