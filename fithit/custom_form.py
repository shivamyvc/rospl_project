from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your tests here.

###Form Validators
def pass_lenth(value):
    if len(value)<8:
        raise forms.ValidationError("the Password is too short")
    return value

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':_('Name')})
        self.fields['username'].widget.attrs.update({'placeholder':_('Username')})
        self.fields['email'].widget.attrs.update({'placeholder':_('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':_('Repeat password')})
   
