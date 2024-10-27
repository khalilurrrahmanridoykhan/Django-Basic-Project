
from django.contrib import admin
from django.urls import path
from home.views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
