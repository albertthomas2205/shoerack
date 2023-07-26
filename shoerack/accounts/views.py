from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
# from app.models import CustomUser
from app.models import CustomUser




# Create your views here.

# def adminsignup(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone_number = request.POST['phone_number']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
        
#         if pass1 == pass2 and len(pass1) > 4 and pass1 != name:
#             if CustomUser.objects.filter(email=email).exists():
#                 # messages.error(request, "Email already exists")
#                 return redirect('account')
            
#             # Create the user
#             user = CustomUser.objects.create_superuser(name=name, email=email,phone_number=phone_number,password = pass1)
#             user.save()
            
            
#             return redirect('signin')
        
#         else:
#             messages.error(request, "Invalid credentials")
#             return redirect('account')
    
#     return render(request, 'account/signup.html')

   
def signinn(request):
    return render(request,'account/signin.html')

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
    return render(request,'account/adminhome.html')

