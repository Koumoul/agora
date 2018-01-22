from django.shortcuts import render
from django.view import View
from .forms import UserPostForm

# Create your views here.

def wall(request):

    return render(request, 'wall/wall.html', {"a": 3,})

