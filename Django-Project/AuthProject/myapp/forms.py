from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'