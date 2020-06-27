from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'register.html')    

def login(request):
    return render(request,'login.html')    