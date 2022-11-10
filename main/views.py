from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    
    return render(request, "main.html")
def register(request):
    
   if request.method=='POST':
       fname=request.POST('fname')
       sname=request.POST('sname')
       email=request.POST('email')
       password1=request.POST('password')
       password2=request.POST('password2') 
       user=User.objects.create_user(password=password1,email=email,fname=fname,sname=sname)
       user.save()
       print('user created')
   return render(request,'register.html')
   
