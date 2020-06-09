from django.db import models
from django.urls import reverse

# Create your models here.
class Testing(models.Model):
    title = models.CharField(max_length=120)
    info = models.TextField()
    coolStuff = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("testing-detail", kwargs={"id": self.id})