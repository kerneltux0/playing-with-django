from django.db import models

# Create your models here.
class Testing(models.Model):
    title = models.TextField()
    info = models.TimeField()