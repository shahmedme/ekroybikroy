from django.shortcuts import render, redirect, HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from account.models import *
from django.contrib import messages


def profile(request):
    person = Profile.objects.all()
    context = {'person': person}
    return render(request, 'account/profile.html', context)


def login_fn(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=userName, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(
                request, 'invalid info please make sure username & password')
            return redirect('/login')
    else:
        return render(request, 'account/login.html')


def signup(request):
    ''' This function creates an user account '''

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        print('sign up function is called')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')

            else:
                User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                return redirect('login-page')

        return redirect('signup-page')
    
    else:
        return render(request, 'account/signup.html')


def logout_fn(request):
    logout(request)
    return redirect('/')
