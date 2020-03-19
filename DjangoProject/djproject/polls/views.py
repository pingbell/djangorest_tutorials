# views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
	return render(request,"templates/base.html")

def list(request):
	return render(request,"templates/list.html")

def home(request):
	return render( request , "templates/home.html")

def default_method(request) :
    return HttpResponse("This is default method!!")


def index(request) :
    return HttpResponse("This is index method!!")

