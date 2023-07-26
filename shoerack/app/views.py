from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,validators
from .models import CustomUserManager
from django.contrib.sessions.models import Session


# Create your views here.
def index(request):
    return render(request,'index.html')



def register(request):
    if request.user.is_authenticated:
            return redirect('index')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 == pass2 and len(pass1) > 4 and pass1 != name:
            
            # if CustomUser.objects.filter(email=email).exists():
            #     messages.error(request, "Email already exists")
            #     return redirect('register')
           
                
            custom_user_manager = CustomUserManager()
            custom_user_manager.send_otp_email(request,email)
            myuser = CustomUser.objects.create_user(name=name, email=email,phone_number=phone_number,password = pass1)
            myuser.save()
            

            return redirect('otp')
        
        # else:
        #     messages.error(request, "Invalid credentials")
        #     return redirect('register')
    
    return render(request, 'register.html')

def Registerpage(request):
   
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone_number= request.POST.get('phone')
        pass1= request.POST.get('pass1')
        password= request.POST.get('pass2')
        if pass1!=password or pass1 is None or len(pass1)<3 :
            key='2'
            messages.error(request, f'Passwords are not matching or week. ({key})')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            key='2'
            messages.error(request, f'This email address is already registered. ({key})')
            return redirect('register')
        else:
            custom_user_manager = CustomUserManager()
            custom_user_manager.send_otp_email(request,email)
            my_user=CustomUser.objects.create_user(name=name,email=email,phone_number=phone_number,password=password,is_verified=False)
            my_user.save()
            my_user=authenticate(request, email=email,password=password)
            return redirect('otpp')
    return render(request,'register.html')


def loginn(request):
    if request.user.is_authenticated:
            return redirect('index')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, email=email,password=password)
        if user is not None:
            custom_user_manager = CustomUserManager()
            custom_user_manager.send_otp_email(request,email)
            login(request,user)
            return redirect('otp')
        else:
            messages.error(request, "Invalid credentials")
    return render(request,'login.html')


def signout(request):
    logout(request)
    return redirect('index')
   

def otpp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
     
        if user_otp == stored_otp:
           
            return redirect('index')
        else:
            return redirect('otp')
  
    return render(request,'otp.html')