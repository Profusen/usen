from django.shortcuts import render


def header(request):
    return render(request, 'header.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')