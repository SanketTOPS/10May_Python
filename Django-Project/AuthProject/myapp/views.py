from django.shortcuts import render,redirect
from .forms import signupForm
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':

        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfully!")
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
    return render(request,'home.html')