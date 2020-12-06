from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'accounts/login.html')

def accounts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if(password1 == password2):
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=name, email=email, password=password1)
                user.save()
                print('User created')
                return redirect('/login')
        else:
            messages.info(request, "Password not matching")
            return redirect('/register')
        return redirect('/')
    else:
        return render(request, "accounts/register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')