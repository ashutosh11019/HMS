from django.shortcuts import render


def home(request):
    return render(request, 'default/home.html', {})

def contact(request):
    return render(request, 'default/contact-us.html', {})

def register(request):
    return render(request, 'default/register.html', {})

def login(request):
    return render(request, 'default/login.html', {})
