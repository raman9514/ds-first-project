from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import auth
# Create your views here.



def signup(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)

        if fm.is_valid():
            #fm.save()
            messages.success(request, 'Account Created Success Fully')
           
    if request.method=='GET':
        fm=SignUpForm()
    return render(request,'register.html',{"reg_form":fm})    




def login(request):
    if request.method=='POST':
        fm=LoginForm(request.POST)
        user = fm.authenticate(request)

        if user is not None:
            #auth.login(request , user)
            return redirect('index')
        else:
            pass
            # messages.error(request,'Invalid Details')
        

    fm=LoginForm
    return render(request,'login.html',{'login_form':fm})  


