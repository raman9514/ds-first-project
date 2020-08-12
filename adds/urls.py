from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('category/<str:cat>',views.category,name='category' ),
    path('visitus/<int:id>',views.visitus,name='visitus'),
    
]
