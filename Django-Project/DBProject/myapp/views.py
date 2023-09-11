from django.shortcuts import render
from .forms import signupform
from .models import signup

# Create your views here.
def index(request):
    if request.method=='POST':
        newuser=signupform(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Signup successfully!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def alldata(request):
    data=signup.objects.all()
    return render(request,'alldata.html',{'data':data})