from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^friends$', views.friends, name='friends')
        ]
