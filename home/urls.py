from django.conf.urls import url
from . import views
from sportpage.views import SportView
from .models import Sport

# put all the sport name in the list sport_name

sport_name = []
sports = Sport.objects.all()
for sport in sports:
    sport_name.append(sport.name)

# translate the list in regular expression / P<sport_name> pass a variable for the view sport
sport_name_re = '(?P<sport_name>' + '|'.join(sport_name) + ')'

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^' + sport_name_re + '$', SportView.as_view(), name='sport'),
        ]
