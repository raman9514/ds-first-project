from django.urls import path
from . import views


urlpatterns = [
    path('TakeOrder' , views.TakeOrder,name='TakeOrder'),
    path('myorder' , views.myorder,name='myorder')

]