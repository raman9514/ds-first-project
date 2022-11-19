from django.shortcuts import render
from adds.models import Adds
from order.models import Order

def index(request):
    crousal_adds = Adds.objects.filter(positions='top_of_page_in_crousal')
    card_adds = Adds.objects.filter(positions='at_card')
    if request.user.is_authenticated:
        current_order = Order.objects.filter(user_id=request.user.id,order_cancelled=False , order_delivered=False).reverse().first()
    else:
        current_order=None    

   
    return render(request,'index.html',{'crousal_adds':crousal_adds,'card_adds':card_adds,'current_order':current_order})


def about(request):
    return render(request,'about.html')

