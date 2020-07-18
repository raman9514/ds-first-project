from django import forms
from .models import Order

zip=[('110020','110020'),('110019','110019')]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =['product_list','shop_address','shop_pincode','u_name','u_phone_no','u_delivery_address','u_pincode','u_delivery_note','user_id']
        labels={
        'product_list':'Products ',
        'shop_address':'Shop Address ',
        'shop_pincode':'Zip Code ',
        'u_name':'Name ',
        'u_phone_no':'contact no. ',
        'u_delivery_address':'Address ',
        'u_pincode':'Zip Code ',
        'u_delivery_note':'Add Delivery Note ',
        'user_id':'' }

        widgets={
        'product_list':forms.TextInput(attrs={"class":"form-control"}),
        'shop_address':forms.TextInput(attrs={"class":"form-control"}) ,
        'shop_pincode':forms.Select(choices=zip ,attrs={"class":"form-control"}) ,
        'u_name':forms.TextInput(attrs={"class":"form-control"}),
        'u_phone_no':forms.TextInput(attrs={"class":"form-control"}),
        'u_delivery_address':forms.TextInput(attrs={"class":"form-control"}),
        'u_pincode':forms.Select(choices=zip , attrs={"class":"form-control"}),
        'u_delivery_note':forms.TextInput(attrs={"class":"form-control"}),
        'user_id': forms.HiddenInput()}
        


