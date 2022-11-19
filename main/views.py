from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    
    return render(request, "main.html")
def signup(request):
    
    
    
    
    
    
    
    return render(request,"signup.html")
def signin(request):
    return render(request,"signin.html")
 
def signout(request):
    return render(request,"signout.html")
 