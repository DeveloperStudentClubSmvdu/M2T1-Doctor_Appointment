from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):

    username=None
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=14)
    city=models.CharField(max_length=100)


    objects=UserManager()
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]

# Create your models here.
