from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {'name': 'John'})

def about(request):
    return HttpResponse("About Page")