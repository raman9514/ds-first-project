from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm,SetPasswordForm
import re


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            
            
        }



class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'password',}))
        

class EditUserForm(UserChangeForm):
    password=None

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control text-primary'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control text-primary'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control text-primary'}),
            'email':forms.EmailInput(attrs={'class': 'form-control text-primary'}),   
            }


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1= forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2= forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PasswordForgotValidate(forms.Form):
    user_name = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))            
   
class SetPasswordForm1(SetPasswordForm):
    user_name = forms.CharField(widget=forms.HiddenInput())
    email = forms.CharField(widget=forms.HiddenInput())
    new_password1= forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2= forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    # def clean_password1(self):
    #     value = self.cleaned_data['password1']

    #     if len(value)>=8:
    #         pass
    #     else:
    #         raise forms.ValidationError('password must contin number , special character , upercase character')
        

    # def clean_password2(self):
    #     value = self.cleaned_data['password2']
    #     value1 = self.cleaned_data['password1']
    #     if value != value1:
    #         raise forms.ValidationError('password must be same')
    #     return value
        
        

            


