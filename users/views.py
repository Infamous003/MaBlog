from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm
# Create your views here.


def user_register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # form.save() # also returns the user value/object
            login(request, form.save())
            return redirect('/')
    else:
        form = CustomUserForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) # form.get_user() gets the user obviously
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')