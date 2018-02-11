from django.shortcuts import render
from django.contrib.auth.models import User
from user_app import models

# Create your views here.

def friends(request):
    users = User.objects.all()
    return render(request, 'friends/friends.html', {'users': users})
