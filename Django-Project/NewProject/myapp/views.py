from django.shortcuts import render
from .forms import userForm


def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid():
            user.save()
            print("Record Inserted!")
        else:
            print(user.errors)
    return render(request,'index.html')