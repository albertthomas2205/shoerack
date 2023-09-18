from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
class CustomUserManager(BaseUserManager):
    def create_user(self,name,phone_number, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(name=name,phone_number=phone_number,email=email,**extra_fields)
        extra_fields.setdefault('is_verified', False)
        user.set_password(password)
        user.save(using=self._db)
        return user
  
    def create_superuser(self,name, phone_number,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(name,phone_number,email, password, **extra_fields)
  
        
    def send_otp_email(self,request,email):
        otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
        message = f'Your OTP for verification: {otp}'
        request.session['gmail']=email
        request.session['otp'] = otp
        request.session.save()
        
        send_mail(
            'OTP Verification',
            message,
            'shoerack2205@gmail.com',  # Sender's email address
            [email],  # Recipient's email address
            fail_silently=False,
        )

        return otp
        
    def send_otp_emailll(self, request, email):
        otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
        message = f'Your OTP for verification: {otp}'
        request.session['gmail'] = email
        request.session['otp'] = otp
        request.session.save()

        send_mail(
            'OTP Verification',
            message,
            'shoerack2205@gmail.com',  # Sender's email address
            [email],  # Recipient's email address
            fail_silently=False,
        )

        return otp
        
# from django.contrib.auth.models import BaseUserManager

# class CustomUserManagerr(BaseUserManager):
#     def create_user(self, name, phone_number, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(name=name, phone_number=phone_number, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, name, phone_number, email,password ,**extra_fields):
#         extra_fields.setdefault('is_verified', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_admin', True)
#         # user.set_password(password)

#         return self.create_user(name, phone_number, email, password, **extra_fields)


