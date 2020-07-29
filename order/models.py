from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone

# Create your models here.

class Order(models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    
    u_name = models.CharField(max_length=50)
    u_phone_no = models.CharField(max_length=10)
    u_delivery_address = models.CharField(max_length=350)
    u_pincode=models.CharField(max_length=6)
    u_delivery_note = models.CharField(max_length=300 , blank=True)

    product_list = models.CharField(max_length=350)
    shop_address = models.CharField(max_length=350 )
    shop_pincode = models.CharField(max_length=6)

    order_date = models.DateTimeField(auto_now_add=True )
    order_pending = models.BooleanField(default=True) 
    order_picked = models.BooleanField(default=False)
    order_delivered = models.BooleanField(default=False)
    order_cancelled = models.BooleanField(default=False)

    delivery_staff = models.CharField(max_length=20 , default="null" )
    







