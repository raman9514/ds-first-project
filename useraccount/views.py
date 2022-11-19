from django.shortcuts import render,redirect
from django.contrib.auth.forms import SetPasswordForm
from .forms import SignUpForm,LoginForm,EditUserForm,PasswordChangeForm,PasswordForgotValidate,SetPasswordForm1
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import auth
from django.shortcuts import HttpResponse
from order.models import Order
from django.contrib.auth.models import User

# Create your views here.



def signup(request):
    if not request.user.is_authenticated:    
        if request.method=='POST':
            fm=SignUpForm(request.POST)

            if fm.is_valid():
                fm.save()
                messages.success(request, 'Account Created Success Fully')

        if request.method=='GET':
            fm=SignUpForm()
        return render(request,'register.html',{"reg_form":fm})    
    else:
        return HttpResponse("please Logout First  ")



def login(request):
    
    if not request.user.is_authenticated:

        if request.method=='POST':
            fm=LoginForm(request.POST)

            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username , password = password)
            print(user)
            if user is not None:
                print("login success");
                auth.login(request , user)
                if user.is_staff == True:
                    return redirect('deliverystaff_index')

                else:
                    return redirect('index')
            else:
                print("login faild")
                messages.error(request,'Invalid Details')


        if request.method == 'GET':
            fm=LoginForm
        return render(request,'login.html',{'login_form':fm})  
    else:
        return HttpResponse("You are not required ths action")


def logout(request):
    auth.logout(request)
    return redirect('index')


def edit_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=EditUserForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Details are Updated')
            else:
                messages.error(request,'User Name already exist choose another one')    
                
        else:
            
            fm=EditUserForm(instance=request.user)
        return render(request,'edit_user_details.html',{'form':fm})
    else:
        return redirect('login')    

  

def password_change(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
        else:
           fm=PasswordChangeForm(user=request.user)
        return render(request,'passwordch.html',{'form':fm})
    
    
def passworforgotvalidate(request):
    result=False
    if request.method == 'POST':
        print("HIIIII"*30)
        fm=PasswordForgotValidate(request.POST)
        if fm.is_valid():            
            username=request.POST['user_name']
            email=request.POST['email']
            result=User.objects.filter(username=username,email=email).exists()
            if result==False:
                messages.error(request,'Uable to Validate your account , please enter correct details')
            else:
                if request.user.is_authenticated:
                    fm=SetPasswordForm1(user=request.user,initial={'user_name':username,'email':email}) 
                else:
                    userobj=User.objects.get(username=username,email=email)
                    fm=SetPasswordForm1(user=userobj,initial={'user_name':username,'email':email})    
    else:
        fm=PasswordForgotValidate()
    return render(request,'forgot_validate.html',{'form':fm,'result':result})





def forgotpassword(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            fm=SetPasswordForm1(request.POST,user=request.user)
            
            # user.setpassword(request.POST)
        else:
            username=request.POST['user_name']
            email=request.POST['email']
            
            userobj=User.objects.get(username=username,email=email)
            fm=SetPasswordForm1(data=request.POST,user=userobj)
        
        if fm.is_valid():
            print(fm)
            fm.save()
            messages.success(request, ' Password Changed ')
            return redirect('login')
        else:

            return render(request,'forgot_validate.html',{'form':fm,'result':True})

            