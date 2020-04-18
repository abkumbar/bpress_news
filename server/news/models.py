from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=500)
    headline = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
    datePublished = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200)
    body_text = models.TextField(help_text='Main article text')
    type = models.CharField(max_length=4,default="text",editable=False)
    
