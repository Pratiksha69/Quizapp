from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('',index),
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
    path('candidatelist/',candidatelist),
    path('result/',result),
    path('organizerdashboard/',organizerdashboard),

    path('dashbord/',dashbord),
    path('quizregistration/',quizregistration),

    path('verifyuser/',verify_user),
    path('checklogin/',checklogin),
    path('candidatelogin/',candidatelogin),
    path('candidateregistration/',candidateregistration),
    path('resendotp/',resendotp),
    path('logout/',logout),
    path('createquiz/',createquiz),
    path('savequiz/',savequiz),
    path('savequestion/',savequestion),
    path('deleteques/',deleteques),
    path('candidatelist/',candidatelist),
    path('savecandidate/',savecandidate),
    path('savecandidate/',savecandidate),
    path('candidatecheck/',candidatecheck),
    path('calculate_result/',calculate_result),

]
