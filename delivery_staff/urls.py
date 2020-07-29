from django.urls import path
from . import views


urlpatterns = [
   path('index',views.deliverystaff,name='deliverystaff_index'),
   path('view_request/<int:order_id>',views.view_request,name='view_request'),
   path('accept_order/<int:order_id>',views.accept_order,name='accept_order'),
]