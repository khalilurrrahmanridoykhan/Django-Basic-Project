from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

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

# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    # sourcery skip: inline-variable, last-if-guard, move-assign-in-block
    page = "Contact Page"
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        print(name, email, subject, message)

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Add a success message
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('contact')  # Redirect to clear the form and display the message

    return render(request, 'contact.html', context={'page': page})


def services(request):
    page = "Services Page"
    return render(request, 'services.html',context={'page': page})