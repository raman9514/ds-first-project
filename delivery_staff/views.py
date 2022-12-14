from django.shortcuts import render,redirect
from order.models import Order
from order.forms import OrderForm
from django.contrib import messages
# Create your views here.

def deliverystaff(request):
    if request.user.is_authenticated and request.user.is_staff==True:
        
        obj = Order.objects.filter(order_pending = True).order_by('order_date').reverse()
        return render(request,'deliverystaff_index.html',{'obj':obj})

    else:
        return redirect('index')    


    


def accept_order(request,order_id):
    if request.user.is_authenticated and request.user.is_staff==True:
        user = request.user.id
        obj = Order.objects.filter(id = order_id)
        obj.update(order_cancelled=False,order_pending=False,order_picked=True,order_delivered=False,delivery_staff=user) 
        messages.success(request, 'Order Accepted')
        return redirect('accepted_order')

    else:
        return redirect('index')   
    

def accepted_order(request):
        if request.user.is_authenticated and request.user.is_staff==True:
            user = request.user.id
            obj = Order.objects.filter( delivery_staff = user ).order_by('-id')
            return render(request,'accepted_order.html',{'obj':obj})

        else:
            return redirect('index')    