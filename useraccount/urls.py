from django.urls import path,include
from .import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('edit_user',views.edit_user,name='edit_user'),
    path('password_change',views.password_change,name='password_change'),
    path('passworforgotvalidate' , views.passworforgotvalidate,name='passworforgotvalidate'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    
    
   
]