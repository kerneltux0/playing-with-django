from django.db import models

# Create your models here.
class Testing(models.Model):
    title = models.CharField(max_length=120)
    info = models.TextField()
    coolStuff = models.BooleanField(default=False)