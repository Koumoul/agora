import sqlite3

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    sport = models.CharField(max_length=30)
