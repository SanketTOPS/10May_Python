from django.shortcuts import render
from.forms import *
from django.contrib import messages

# Create your views here.

status=False
def index(request):
    global status
    if request.method=='POST':
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
    return render(request,'index.html',{'status':status})

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')