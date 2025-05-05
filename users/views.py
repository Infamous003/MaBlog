from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
# Create your views here.


def user_register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        print(form.is_valid(), "-----------------------------")
        if form.is_valid():
            form.save()
            return redirect('/') #name of the app : url name
    else:
        form = CustomUserForm()
    return render(request, 'users/register.html', {'form': form})