from django.contrib import admin
from .models import *

# Register your models here.
class studdata(admin.ModelAdmin):
    list_display=['name','email','city']

admin.site.register(studinfo,studdata)
