from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^signin$', views.signinView, name='signin'),
        url(r'^login$', views.loginView, name='login'),
        url(r'^logout$', views.logoutView, name='logout'),
]

