from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import uuid
import datetime
# Create your views here.
def index(request):
	return render(request, 'index.html',{})

def register(request):
	return render(request, 'register.html',{})
@csrf_exempt
def OrgSave(request):
	if request.method=='POST':
		f=request.POST.get("Fullname")
		e=request.POST.get("Email")
		p=request.POST.get("Password")

		#to generate the ID
		c="ORG00"
		x=1
		cid=c+str(x)
		while OrganizerData.objects.filter(Org_ID=cid).exists():
			x=x+1 #2
			cid=c+str(x)
		x=int(x)

		#Generate OTP
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+cid+f+e+p).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['OTP']=otp#Make Session
		OrganizerData(
			Org_ID=cid,
			Org_Name=f,
			Org_Email=e,
			Org_Password=p,
			).save()

		msg="Registered Success! Now Verify Your Email"
		dic={'msg':msg}#JSON
		return render(request, 'register.html',dic)

def login(request):
	return render(request, 'login.html',{})
def elements(request):
	return render(request, 'elements.html',{})
def courses(request):
	return render(request, 'courses.html',{})
def contact(request):
	return render(request, 'contact.html',{})
def blog_details(request):
	return render(request, 'blog_details.html',{})
def blog(request):
	return render(request, 'blog.html',{})
def about(request):
	return render(request, 'about.html',{})
def login2(request):
	return render(request, 'login2.html',{})

def sendmail():
	sub='Test QuizAPP otp'
	msg=''' OTP Success
Thanks'''
	email=EmailMessage(sub,msg,to=['tpratiksha692@gmail.com'])
	email.send()

def hello(request):
	return render(request,'hello.html',{})