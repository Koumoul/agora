from django.db import models
import uuid

# Create your models here.

class UserBrick(models.Model):
    
    #content
    text =  models.TextField(max_length=400, blank=True, null=True)
    url =   models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    
    #meta
    date =  models.DateField(auto_now_add=True, blank=True)
    time =  models.TimeField(auto_now_add=True, blank=True)
    uuid  =  models.UUIDField(default=uuid.uuid4, editable=False)
    autor = models.CharField(max_length=40)
    sport_name = models.CharField(max_length=40)
