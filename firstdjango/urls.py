
from django.contrib import admin
from django.urls import path
from home.views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('admin/', admin.site.urls),
]
