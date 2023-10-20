from django.shortcuts import render,redirect
from.forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import logout

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
            userid=userSignup.objects.get(username=unm)
            print("UserID:",userid.id)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                request.session['userid']=userid.id
                return redirect('notes')
            else:
                print("Error!Login fail...try again!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=userSignup.objects.get(id=userid)
    return render(request,'profile.html',{'user':user,'userid':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")
