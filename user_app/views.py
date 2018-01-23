from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, SigninForm



# Create your views here.

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if user.is_authenticated:
                return redirect('home')

    else:
        
        form = LoginForm()

    return render(request, 'user_app/login.html', locals())

@login_required(login_url='login')
def signinView(request):

    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            family_name = form.cleaned_data["family_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            if password == password2:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                        last_name=family_name, email=email)
                user.save()
    else:
        form = SigninForm()

    return render(request, 'user_app/signin.html', locals())

def logoutView(request):

    logout(request)
    return redirect('login')
