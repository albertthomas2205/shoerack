
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('loginn',views.loginn,name = 'loginn'),
    path('register',views.register,name = 'register'),
    path('signout',views.signout,name = 'signout'),
    path('otp',views.otpp,name ='otp'),
    path('shop',views.shop,name = 'shop')
    
]
