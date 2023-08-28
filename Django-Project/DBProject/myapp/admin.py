from django.contrib import admin
from .models import signup

# Register your models here.
class SignupData(admin.ModelAdmin):
    #ordering=['id']
    list_display=['id','name','email','dob','mobile','address']

admin.site.register(signup,SignupData)