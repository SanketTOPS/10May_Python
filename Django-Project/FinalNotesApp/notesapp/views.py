from django.shortcuts import render,redirect
from.forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from FinalNotesApp import settings

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
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=userSignup.objects.get(id=userid)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print("Error!Something went wrong...")
    return render(request,'profile.html',{'user':user,'userid':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your FEEDBACK has been submitted!")

            #Email Send
            send_mail(subject="Thank you!",message=f"Dear User\n\nThanks for connecting with us!\nIf you have any queries regarding service, Please contact on\n\n+919724799469 | sanket.tops@gmail.com | www.tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['email']])

        else:
            print(newfeedback.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")
