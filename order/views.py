from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
# Create your views here.

def TakeOrder(request):
    current_user=request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            fm=OrderForm(request.POST)
            if fm.is_valid():    
                # product = request.POST['product']
                # data=Order(user_id=user,product=product)
                fm.save()
                fm=OrderForm(initial={'user_id':current_user})
                messages.success(request, 'Order Placed successfully')

        else:
            fm=OrderForm(initial={'user_id':current_user})
        return render(request,'TakeOrder.html',{'form':fm})

    else:
        # return HttpResponse('Invalid request')
        return redirect('login')
            
