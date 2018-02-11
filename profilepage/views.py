from django.shortcuts import render
from wall.models import UserBrick

def profile(request):
    bricks = UserBrick.objects.filter(autor=request.user.username)

    return render(request, 'profilepage/profile.html', {'bricks': bricks,})
# Create your views here.
