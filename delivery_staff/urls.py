from django.urls import path
from . import views


urlpatterns = [
   path('index',views.deliverystaff,name='deliverystaff_index'),
   
   path('accept_order/<int:order_id>',views.accept_order,name='accept_order'),
   path('accepted_order',views.accepted_order,name='accepted_order')
]