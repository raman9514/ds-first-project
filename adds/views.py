from django.shortcuts import render
from .models import Adds , Category ,Position
# Create your views here.

def category(request,cat):
    cat_data_crousal = Adds.objects.filter(positions='top_of_page_in_crousal' , category = cat)
    cat_data_card = Adds.objects.filter(positions='at_card' , category = cat)

    return render(request,'category_view.html',{'crousal_adds':cat_data_crousal,'card_adds':cat_data_card})