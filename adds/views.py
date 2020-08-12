from django.shortcuts import render
from .models import Adds , Category ,Position
# Create your views here.

def category(request,cat):
    cat_data_crousal = Adds.objects.filter(positions='top_of_page_in_crousal' , category = cat)
    cat_data_card = Adds.objects.filter(positions='at_card' , category = cat)

    return render(request,'category_view.html',{'crousal_adds':cat_data_crousal,'card_adds':cat_data_card})



def visitus(request,id):
    current_adds = Adds.objects.get(id=id)
    cat=current_adds.category
    similar_adds=Adds.objects.filter(category=cat)

    return render(request,'adds_visitus.html',{'current_add':current_adds,'card_adds':similar_adds})