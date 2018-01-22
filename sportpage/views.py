from django.shortcuts import render
from django.views import View
from .forms import UserPostForm
from wall.models import UserBrick
# Create your views here.

class SportView(View):

    form_class = UserPostForm
    initial = {'text':'',}


    def get(self, request, sport_name):
        form = self.form_class(initial=self.initial)
        bricks = UserBrick.objects.filter(sport_name=sport_name)
        return render(request, 'sportpage/sport.html', {'sport_name': sport_name, 'form': form, 'bricks': bricks,})

    def post(self, request, sport_name):
        form = self.form_class(request.POST)
        bricks = UserBrick.objects.filter(sport_name=sport_name)
        if form.is_valid():
            text = form.cleaned_data['text']

            userbrick = UserBrick(
                                text=text,
                                autor='test',
                                sport_name = sport_name,
                                )
            userbrick.save()
            
            return render(request, 'sportpage/sport.html', {'sport_name': sport_name, 'form': form, 'bricks': bricks,})

            

