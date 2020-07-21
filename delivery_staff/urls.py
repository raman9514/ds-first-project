from django.urls import path
from . import views


urlpatterns = [
   path('deliverystaff_index',views.deliverystaff,name='deliverystaff_index'),
]