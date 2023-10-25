from django.contrib import admin
from .models import *

# Register your models here.

class notesAdmin(admin.ModelAdmin):
    list_display=['title','option','file','comment']

admin.site.register(userSignup)
admin.site.register(notes,notesAdmin)
