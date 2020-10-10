from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import uuid
import datetime
from webapp.myutil import *
# Create your views here.
def index(request):
	dic={'checksession':checksession(request)}
	return render(request, 'index.html',dic)
def verified(request):
	dic={'checksession':checksession(request)}
	return render(request, 'verified.html',dic)
def register(request):
	dic={'checksession':checksession(request)}
	return render(request, 'register.html',dic)
@csrf_exempt
def OrgSave(request):
	dic={'checksession':checksession(request)}
	if request.method=='POST':
		f=request.POST.get("Fullname")
		e=request.POST.get("Email")
		p=request.POST.get("Password")
		OrganizerData.objects.all().delete()
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
		if OrganizerData.objects.filter(Org_Email=e).exists():
			dic={'msg':'Already Exists'}
			return render(request, 'register.html',dic)
		else:
			OrganizerData(
				Org_ID=cid,
				Org_Name=f,
				Org_Email=e,
				Org_Password=p,
				).save()
			sub='QuizAPP OTP'
			msg='''Your OTP is '''+otp+''',

Thanks!'''
			email=EmailMessage(sub,msg,to=[e])
			email.send()
			msg="Registered Success! Now Verify Your Email"
			dic={'msg':msg,'id':cid}#JSON
			return render(request, 'verified.html',dic)
@csrf_exempt
def verify_user(request):
	dic={'checksession':checksession(request)}
	if request.method=='POST':
		uotp=request.POST.get('otp')
		orgid=request.POST.get('id')
		sotp=request.session['OTP']
		if uotp==sotp:
			OrganizerData.objects.filter(Org_ID=orgid).update(Status='Active')
			return redirect('/index/')
		else:
			dic={'id':orgid
			,'msg':'Incorrect OTP'}
			return render(request, 'verified.html',dic)
		email=EmailMessage(sub,msg,to=[e])
		email.send()
		msg=" verified Email! Now login"
		dic={'msg':msg,'id':orgid}#JSON
		return render(request, 'login.html',dic)
@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		if OrganizerData.objects.filter(Org_Email=email,Org_Password=password).exists():
			if OrganizerData.objects.filter(Org_Email=email,Status='Active').exists():
				request.session['orgid']=OrganizerData.objects.filter(Org_Email=email)[0].Org_ID
				return redirect("/index/")
			else:
				otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+cid+f+e+p).int
				otp=str(otp)
				otp=otp.upper()[0:6]
				request.session['OTP']=otp#Make Session
				sub='QuizAPP OTP'
				msg='''Your OTP is '''+otp+''',

Thanks!'''
			email=EmailMessage(sub,msg,to=[e])
			email.send()

		else:
			dic={'msg':'Incorrect Email/Password'}
			return render(request,'login.html',dic)
def login(request):
	dic={'checksession':checksession(request)}
	return render(request, 'login.html',dic)
def elements(request):
	dic={'checksession':checksession(request)}
	return render(request, 'elements.html',dic)
def courses(request):
	dic={'checksession':checksession(request)}
	return render(request, 'courses.html',dic)
def contact(request):
	dic={'checksession':checksession(request)}
	return render(request, 'contact.html',dic)
def blog_details(request):
	dic={'checksession':checksession(request)}
	return render(request, 'blog_details.html',dic)
def blog(request):
	dic={'checksession':checksession(request)}
	return render(request, 'blog.html',dic)
def about(request):
	dic={'checksession':checksession(request)}
	return render(request, 'about.html',dic)
def login2(request):
	dic={'checksession':checksession(request)}
	return render(request, 'login2.html',dic)

def sendmail():
	sub='Test QuizAPP otp'
	msg=''' OTP Success
Thanks'''
	email=EmailMessage(sub,msg,to=['tpratiksha692@gmail.com'])
	email.send()

def hello(request):
	return render(request,'hello.html',{})