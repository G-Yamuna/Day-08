from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:white;background-color:lightblue;text-align:center;font-size:34px'>Welcome To Home Page</h2>")

def chk(request):
    return HttpResponse("<script>alert('hii good afternoon')</script><h2>welcome to python</h2>")	

def homepage(request):
	return render(request,'ht/homepage.html')

def login(r):
	return render(r,'ht/login.html')

def registration(re):
	return render(re,'ht/register.html')