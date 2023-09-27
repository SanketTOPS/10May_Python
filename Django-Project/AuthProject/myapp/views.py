from django.shortcuts import render,redirect
from .forms import signupForm
from .models import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=userSignup.objects.get(username=unm)
        print(f"Firstname:{fnm.firstname}")
        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfully!")
            #request.session['cuser']=unm #creating a session
            request.session['cuser']=fnm.firstname
            return redirect('home')
        else:
            print("Error!Login fail...")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('cuser')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
