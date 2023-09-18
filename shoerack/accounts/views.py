from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
# from app.models import CustomUser
from app.models import CustomUser






from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model




def signinn(request):
    return render(request,'account/signin.html')

def user(request):
    data = CustomUser.objects.all()
    context={"data":data}
    return render(request,'html/sample-page.html',context)
    

def signin(request):
    # if request.user.is_authenticated:
    #         return redirect('adminhome')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, email=email,password=password)
        if user is not None and user.is_superuser:
            # custom_user_manager = CustomUserManager()
            # custom_user_manager.send_otp_email(request,email)
            login(request,user)
            return redirect('adminhome')
        else:
            messages.error(request, "Invalid credentials")
    return render(request,'account/signin.html')

    
def adminhome(request):
    return render(request,'html/index.html')


def block_user_view(request,id):
   
    if request.method == 'POST':
       
            
        user = CustomUser.objects.get(id=id)
        if user.is_active:
            
            user.is_active = False
        else:
            user.is_active=True
        user.save()
    # action = 'blocked' if not user.is_active else 'unblocked'
    # messages.success(request, f"{user.username} has been {action}.")
    # return render('html/sigle-page.html')
    return redirect('user')