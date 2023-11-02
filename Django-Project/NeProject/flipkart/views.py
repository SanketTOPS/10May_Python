from django.shortcuts import render

# Create your views here.
n=0
def index(request):
    global n
    n+=1
    return render(request,'index.html',{'nm':n})