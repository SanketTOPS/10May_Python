from django.shortcuts import render,redirect
from .forms import signupform,updateform
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

def deletedata(request,id):
    stid=signup.objects.get(id=id)
    signup.delete(stid)
    return redirect('alldata')

def updatedata(request,id):
   stid=signup.objects.get(id=id)
   if request.method=='POST':
        newuser=updateform(request.POST,instance=stid)
        if newuser.is_valid(): #true
            newuser.save()
            print("Record updated successfully!")
            return redirect('alldata')
        else:
            print(newuser.errors)
   return render(request,'updatedata.html',{'cid':stid})