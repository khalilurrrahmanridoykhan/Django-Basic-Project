from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peopol =[
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 24},
        {'name': 'Joe', 'age': 26},
        {'name': 'Jill', 'age': 27},
        {'name': 'Jack', 'age': 28},
    ]
    page = "Home Page"
    return render(request, 'index.html', context={'peopol': peopol, 'page': page})

def about(request):
    page = "About Page"
    return render(request, 'about.html', context={'page': page})

def contact(request):
    page = "Contact Page"
    return render(request, 'contact.html',context={'page': page})

def services(request):
    page = "Services Page"
    return render(request, 'services.html',context={'page': page})