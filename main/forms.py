from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Accounts
from django.contrib.auth.models import User



class MyForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control border border-dark'}),label="Enter email")
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark'}),label="Enter username")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-dark'}),label="Set password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-dark'}),label="Confirm password")
    
    class Meta:
        model = Accounts
        fields=['email','username','password1','password2']    
        
    
    def clean(self):
        cleaned_data = super().clean()
        pw1=cleaned_data['password1']
        pw2 = cleaned_data['password2']
        if pw1 != pw2:
            raise ValidationError("Password must be same as a enter above!")
    
class LogForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-dark','name':'email'}),label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-dark','name':'password'}),label="Password")