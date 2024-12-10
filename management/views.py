from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as auth_logout
from .models import *
from django.contrib.auth.models import User
# Create your views here.




def home(request):

    return render(request, 'management/home.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use `auth_login` to avoid conflict with the view name
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Username and password are required")

    return render(request, 'management/login.html')




def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def superuser_list(request):
    
    superusers = User.objects.filter(is_superuser=True, is_active=True, is_staff=True)

    context ={
        "superusers" : superusers,
        
    }
    return render(request, 'management/superuser_list.html', context)


def staff_list(request):
    # print(request.club_id)
    staff_members = User.objects.filter(is_staff=True)  
    return render(request, 'management/staff_list.html', {'staff_members': staff_members})