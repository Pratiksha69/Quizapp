"""Quiztech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('register/',register),
    path('login/',login),
    path('elements/',elements),
    path('courses/',courses),
    path('contact/',contact),
    path('blog_details/',blog_details),
    path('blog/',blog),
    path('about/',about),
<<<<<<< HEAD
    path('verified/',verified),
    path('customer/',customer),
    
=======
    path('login2/',login2),
    path('OrgSave/',OrgSave),
>>>>>>> 8ebfcadf263ce7bba3020ede9751cf29cbc7171b
]
