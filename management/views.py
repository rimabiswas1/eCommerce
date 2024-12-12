from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as auth_logout
from .models import *
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import login
from django.urls import reverse





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
                return redirect('management:home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Username and password are required")

    return render(request, 'management/login.html')




def logout(request):
    auth_logout(request)
    return redirect('management:login')

@login_required(login_url='login')
def superuser_list(request):
    
    superusers = User.objects.filter(is_superuser=True, is_active=True, is_staff=True)

    context ={
        "superusers" : superusers,
        
    }
    return render(request, 'management/superuser_list.html', context)


def create_superuser(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username  = request.POST.get('username')
    

        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
       
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        nid = request.POST.get('nid')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')


        users = User.objects.create_superuser(
            username=username,  
            first_name=first_name,  
            last_name=last_name,   
            email = "abc@gmail.com",
            is_superuser = True
        )
        # user.save()
        # profile = user.profile
        profile = users.profile
        
        # Update the existing profile if necessary
        profile.father_name = father_name
        profile.mother_name = mother_name
        profile.phone = phone
        profile.nid = nid
        profile.gender = gender
        profile.blood_group = blood_group
        profile.address = address

        profile.save()

        return redirect('superuser_list')

    


    return render(request,'management/create_superuser.html')


def staff_list(request):
    # print(request.club_id)
    staff_members = User.objects.filter(is_staff=True)  
    return render(request, 'management/staff_list.html', {'staff_members': staff_members})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and first_name and last_name and email and password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already registered.")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                auth_login(request, user)  # Correctly use Django's built-in login
                return redirect(reverse('management:login'))
        else:
            messages.error(request, "All fields are required.")
    
    return render(request, 'management/signup.html')


def customer(request):

    return render(request, 'management/customer.html')

def product_view(request):

    return render(request, 'management/product_view.html')