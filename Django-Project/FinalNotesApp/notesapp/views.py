from django.shortcuts import render,redirect
from.forms import *
from .models import *
from django.contrib import messages

# Create your views here.

status=False
def index(request):
    global status
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                status=True
                print("Current Status:",status)
                messages.success(request,"Signup Successfully!")
            else:
                print(newuser.errors)
                status=False
                messages.error(request,"Error!Something went wrong...Try again!")
        elif request.POST.get('signin')=='signin':

            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error!Login fail...try again!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')