from django.db import models
from wall.models import UserBrick

# Create your models here.

class Sport(models.Model):
    name        = models.CharField(max_length=30)
    image_name  = models.CharField(max_length=50)

    def __str__(self):
        return self.name

