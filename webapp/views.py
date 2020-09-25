from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
	return render(request, 'index.html',{})
def register(request):
	return render(request, 'register.html',{})
	def saveData(request):s
	s=register(Fullname="Pratiksha Tyagi",Email="tpratiksha692@gmail.com",Password="tyagi692@",ConfirmPassword="tyagi692@")
	s=register(Fullname="Rupali Agarwal",Email="agarwalrupali28@gmail.com",Password="agrawal1234",ConfirmPassword="agrawal1234")
	s.save()
	msg="record saved now"
	return HttpResponse(msg)
@csrf_exempt
def ShowData(request):
	obj=register.objects.all()
	res="Data is <BR>"
	for x in obj:
		res=res+x.Fullname+"<BR>"
		res=res+x.Email+"<BR>"
		res=res+x.Password+"<BR>"
		res=res+x.ConfirmPassword+"<BR>"

	return HttpResponse(res)
def inputData(request):
	return render(request,'register.html')
@csrf_exempt
def save(request):
	f=request.POST.get("Fullname")
	e=request.POST.get("Email")
	p=request.POST.get("Password")
	c=request.POST.get("ConfirmPassword")

	s=CustomerDetails(Fullname=f,Email=e,Password=p,ConfirmPassword=c)
	s.save()
	msg="<h1> record saved</h1>"
	return HttpResponse(msg)

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