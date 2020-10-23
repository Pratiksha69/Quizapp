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
def candidatelogin(request):
	return render(request,'candidatelogin.html',{})

	dic={'checksession':checksession(request)}
	return render(request, 'register.html',dic)


@csrf_exempt
def OrgSave(request):
	if request.method=='POST':
		f=request.POST.get("Fullname")
		e=request.POST.get("Email")
		p=request.POST.get("Password")
		#OrganizerData.objects.all().delete()
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

def createquiz(request):
	dic={'checksession':checksession(request)}
	return render(request,'createquiz.html',dic)

@csrf_exempt
def savequiz(request):
	if request.method=='POST':
		name = request.POST.get("name")
		category = request.POST.get("category")
		quesno = request.POST.get("quesno")
		marks = request.POST.get("marks")
		time = request.POST.get("time")
		#uizData.objects.all().delete()
		#to generate the ID
		q="QZ00"
		x=1
		qid=q+str(x)
		while QuizData.objects.filter(Quiz_ID=qid).exists():
			x=x+1 #2
			qid=q+str(x)
		x=int(x)
		if not QuizData.objects.filter(Quiz_Name=name).exists():
			QuizData(
				Quiz_ID=qid,
				Org_ID=request.session['org_id'],
				Quiz_Name=name,
				Quiz_Category=category,
				Question_Count=quesno,
				Marks_Per_Ques=marks,
				Maximum_Time=time
				).save()
			return redirect('/organizerdashboard/')
		else:
			dic={'checksession':checksession(request), 'msg':'Choose a different Name of Quiz....'}
			return render(request,'createquiz.html',dic)
	else:
		return HttpResponse('Error 404 Not Found')

def organizerdashboard(request):
	dic={'checksession':checksession(request),
		'data':QuizData.objects.filter(Org_ID=request.session['org_id'])}
	return render(request,'organizerdashboard.html',dic)

def quizdash(request):
	quizid = request.GET.get('id')
	request.session['quiz_id'] = quizid
	dic={'checksession':checksession(request),
		'data':QuizData.objects.filter(Quiz_ID=quizid)[0],
		'questions':QuestionData.objects.filter(Quiz_ID=quizid)}
	return render(request,'quizdash.html',dic)
def candidatelist(request):
	return render(request,'candidatelist.html',{})
def result(request):
	return render(request,'result.html',{})

@csrf_exempt
def savequestion(request):
	if request.method=='POST':
		ques = request.POST.get('question')
		option_a = request.POST.get('a')
		option_b = request.POST.get('b')
		option_c = request.POST.get('c')
		option_d = request.POST.get('d')
		answer = request.POST.get('answer')
		q="QUES00"
		x=1
		qid=q+str(x)
		while QuestionData.objects.filter(Question_ID=qid).exists():
			x=x+1 #2
			qid=q+str(x)
		x=int(x)
		QuestionData(
			Question_ID=qid,
			Quiz_ID=request.session['quiz_id'],
			Question=ques,
			Option_A=option_a,
			Option_B=option_b,
			Option_C=option_c,
			Option_D=option_d,
			Answer=answer
			).save()
		return redirect('/quizdash/?id='+request.session['quiz_id'])
	else:
		return HttpResponse('Error 404 Not Found')

def deleteques(request):
	id_=request.GET.get('id')
	QuestionData.objects.filter(Question_ID=id_).delete()
	return redirect('/quizdash/')
def candidatelist(request):
	return render(request,'candidatelist.html',{})
def candidateregistration(request):
	return render(request,'candidateregistration.html',{})
def questionpaper(request):
	return render(request,'questionpaper.html',{})
