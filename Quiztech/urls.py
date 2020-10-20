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
    path('courses/',courses),
    path('contact/',contact),
    path('blog_details/',blog_details),
    path('blog/',blog),
    path('about/',about),
    path('index/',index),
    path('verified/',verified),
    path('OrgSave/',OrgSave),
    path('quizdash/',quizdash),
    path('organizerdashboard/',organizerdashboard),

    path('dashbord/',dashbord),
    path('quizregistration/',quizregistration),

    path('verifyuser/',verify_user),
    path('checklogin/',checklogin),
    path('candidatelogin/',candidatelogin),
    

    path('resendotp/',resendotp),
    path('logout/',logout),
    path('createquiz/',createquiz),
    path('savequiz/',savequiz),
    path('savequestion/',savequestion)

]
