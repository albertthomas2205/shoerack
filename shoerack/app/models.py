from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    password=models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100,null = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Add any additional fields you want to store for the user, like name, date of birth, etc.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','name','phone_number']
    

    def __str__(self):
        return self.email

