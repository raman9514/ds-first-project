from django.urls import path
from . import views


urlpatterns = [
    path('TakeOrder' , views.TakeOrder,name='TakeOrder'),
    path('myorder' , views.myorder,name='myorder'),
    path('cancleorder/<int:id>',views.cancleorder,name='cancleorder'),
   path('editorder/<int:id>',views.editorder,name='editorder'),

]