from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models
# Create your views here.


@login_required(login_url='login')
def home(request):
    sports = models.Sport.objects.all()  
    return render(request, 'home/home.html', {'sports': sports})
