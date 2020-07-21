from django.shortcuts import render,redirect
from order.models import Order
# Create your views here.

def deliverystaff(request):
    if request.user.is_authenticated and request.user.is_staff==True:
        
        obj = Order.objects.filter(order_pending = True)
        return render(request,'deliverystaff_index.html',{'orders':obj})

    else:
        return redirect('index')    