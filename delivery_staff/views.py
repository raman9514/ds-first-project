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



def view_request(request,order_id):
    if request.user.is_authenticated and request.user.is_staff==True:
        
        obj = Order.objects.get(id = order_id)
        fm=OrderForm(instance=obj)
        return render(request,'view_request.html',{'form':fm})

    else:
        return redirect('index')   
    


def accept_order(request,order_id):
    if request.user.is_authenticated and request.user.is_staff==True:
        
        obj = Order.objects.filter(id = order_id)
        obj.update(order_cancelled=False,order_pending=False,order_picked=True,order_delivered=False) 
        messages.success(request, 'Order Accepted')
        return redirect('deliverystaff_index')

    else:
        return redirect('index')   
    