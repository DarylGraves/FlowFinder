from django.db import models

# Create your models here.
class Hydrant(models.Model):
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)


    def __str__(self):
        return self.name