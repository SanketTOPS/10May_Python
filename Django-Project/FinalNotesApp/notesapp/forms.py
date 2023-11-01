from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'


class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','state','city','mobile']
    

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'