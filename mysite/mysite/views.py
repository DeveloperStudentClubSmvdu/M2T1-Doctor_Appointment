from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



def home(request):
    return render(request,"index.html")

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    else:
        if request.method == "POST": # To register users.
            try:
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')
                city = request.POST.get('city')
                mob = request.POST.get('mob')
                email = request.POST.get('email')
                cemail = request.POST.get('cemail')
                passwd = request.POST.get('passwd')
                cpasswd = request.POST.get('cpasswd')


                if email != cemail:
                    mstr1 = 'Email and Confirm Email are not same.'
                    messages.error(request, mstr1)
                    return HttpResponseRedirect('/register/')
                if passwd != passwd:
                    mstr2 = 'Email and Confirm Email are not same.'
                    messages.error(request, mstr2)
                    return HttpResponseRedirect('/register/')

                user = User.objects.create_user(username=cemail, email=cemail, password=cpasswd)
                user.first_name = fname
                user.last_name = lname
                user.save()
                mstr3 = 'You account has been successfully created.'
                messages.success(request, mstr3)
                return HttpResponseRedirect("/login/")

            except Exception as e:
                messages.error(request, e)
                return HttpResponseRedirect('/register/')
        
        return render(request, "register.html")

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
    