from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def mentions(request):
    return render(request, 'pages/mentions.html')
