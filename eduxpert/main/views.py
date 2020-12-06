from django.shortcuts import render, get_object_or_404, redirect
from .models import Main

# Create your views here.

def home(request):
    sitename = "Eduxpert | Home"

    return render(request, 'front/home.html', {'sitename':sitename})

def physics(request):
    sitename = "Eduxpert | Physics"

    return render(request, 'front/physics.html', {'sitename':sitename})

def chemistry(request):
    sitename = "Eduxpert | Chemistry"

    return render(request, 'front/chemistry.html', {'sitename':sitename})

def mathematics(request):
    sitename = "Eduxpert | Mathematics"

    return render(request, 'front/mathematics.html', {'sitename':sitename})

def panel(request):
    sitename = "Eduxpert | Panel"

    return render(request, 'back/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        print(name, email, text)
        msg = contact(name = name, email = email, text = text)
        msg.save()
    return render(request, 'front/contactUs.html')

def doubt(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        ask = request.POST['doubts']
        concept = doubt(name = name, email = email, subject=subject, doubt=doubts)
        concept.save()
    return render(request, 'front/doubt.html')