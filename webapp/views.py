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
	print(dic)
	return render(request, 'index.html',dic)
def verified(request):
	return render(request, 'verified.html',{})
def register(request):

	return render(request, 'register.html',{})
def dashbord(request):
	dic={'checksession':checksession(request)}
	return render(request,'dashbord.html',{})
def quizregistration(request):
	return render(request,'quizregistration.html',{})


	dic={'checksession':checksession(request)}
	return render(request, 'register.html',dic)


@csrf_exempt
def OrgSave(request):
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

	if request.method=='POST':
		uotp=request.POST.get('otp')
		orgid=request.POST.get('id')
		sotp=request.session['OTP']
		if uotp==sotp:
			OrganizerData.objects.filter(Org_ID=orgid).update(Status='Active')
			request.session['org_id'] = orgid
			return redirect('/index/')
		else:
			dic={'id':orgid,'msg':'Incorrect OTP'}
			return render(request, 'verified.html',dic)
def resendotp(request):
	orgid=request.GET.get('orgid')
	orgobj=OrganizerData.objects.filter(Org_ID=orgid)[0]
	otp=request.session['OTP']
	sub='QuizAPP OTP'
	msg='''Your OTP is '''+otp+''',

Thanks!'''
	email=EmailMessage(sub,msg,to=[orgobj.Org_Email])
	email.send()
	dic={'id':orgid}
	return render(request, 'verified.html',dic)

@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		if OrganizerData.objects.filter(Org_Email=email,Org_Password=password).exists():
			if OrganizerData.objects.filter(Org_Email=email,Status='Active').exists():
				request.session['org_id']=OrganizerData.objects.filter(Org_Email=email)[0].Org_ID
				return redirect("/index/")
			else:

				org_obj=OrganizerData.objects.filter(Org_Email=email)[0]
				otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+org_obj.Org_ID+org_obj.Org_Name+org_obj.Org_Password).int

				orgobj=OrganizerData.objects.filter(Org_Email=email)[0]
				otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+orgobj.Org_ID+orgobj.Org_Name+orgobj.Org_Email+orgobj.Org_Password).int

				otp=str(otp)
				otp=otp.upper()[0:6]
				request.session['OTP']=otp#Make Session
				sub='QuizAPP OTP'
				msg='''Your OTP is '''+otp+''',

Thanks!'''

				email=EmailMessage(sub,msg,to=[e])
				email.send()
				msg="Registered Success! Now Verify Your Email"
				dic={'msg':msg,'id':org_obj.Org_ID}#JSON
				return render(request, 'verified.html',dic)

		else:
			dic={'msg':'Incorrect Email/Password'}
			return render(request,'login.html',dic)

def logout(request):
	del request.session['org_id']
	return redirect('/index/')

def login(request):
	return render(request, 'login.html',{})
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
def createquiz(request):
	dic={'checksession':checksession(request)}
	return render(request,'createquiz.html',dic)
	@csrf_exempt
def QZSave(request):
	if request.method=='POST':
		qn=request.POST.get("Quiz Name")
		qc=request.POST.get("Quiz Category")
		nq=request.POST.get("No of Quiestions in Quiz")
		mpq=request.POST.get("Marks Per Quiestion ")
		QuizData.objects.all().delete()
		#to generate the ID
		q="QZ00"
		x=1
		qid=c+str(x)
		while QuizData.objects.filter(QZ_ID=qid).exists():
			x=x+1 #2
			qid=q+str(x)
		x=int(x)
		else:
			QuizData(
				QZ_ID=qid,
				QZ_Name=qn,
				QZ_Questions=nq,
                QZ_Marks=mpq,
				).save()


def sendmail():
	sub='Test QuizAPP otp'
	msg=''' OTP Success
Thanks'''
	email=EmailMessage(sub,msg,to=['tpratiksha692@gmail.com'])
	email.send()

def hello(request):
	return render(request,'hello.html',{})