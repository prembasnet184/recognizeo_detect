from http.client import HTTPResponse
from operator import imod
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request,"authentication/index.html")
    
def signup(request):
    return render(request,"authentication/signup.html")
    
def signin(request):
    return render(request,"authentication/signin.html")
    
def signout(request):
    pass
def test(request):
    return render(request,"authentication/test.html")
