from django.urls import path
from accounts import views

urlpatterns = [
   
    # path('account',views.adminsignup,name='account'),
    path('signin/',views.signin,name = 'signin'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('user/',views.user,name = 'user'),
    path('block/<int:id>',views.block_user_view,name= 'block')

   
]
