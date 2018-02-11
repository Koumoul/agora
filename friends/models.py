from django.db import models
from user_app.models import MyUser
# Create your models here.

class Friends(models.Model):
    source = models.OneToOneField(MyUser, related_name='source', on_delete=models.PROTECT)
    followedBy = models.OneToOneField(MyUser, related_name='followedBy', on_delete=models.PROTECT) 
