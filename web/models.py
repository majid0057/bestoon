from django.db import models

# Create your models here.

class expense(models.Model):
    text = models.CharField(max_length = 255)
    date = models.DateTimeField()