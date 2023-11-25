from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



def home(request):
    return render(request,"index.html")

def signup(request):
    return render (request,"signup.html")

def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    
    else:
        if request.method == "POST":
            email1 = request.POST['email']
            passwd1 = request.POST['psw']

            user = authenticate(request, username=email1, password=passwd1)
            
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                messages.error(request, "User not found.")
                return HttpResponseRedirect("/login/")

        
    
        return render(request, 'login.html')
    