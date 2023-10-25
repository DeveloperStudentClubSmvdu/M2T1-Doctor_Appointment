from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



def home(request):
    return render(request,"index.html")

def signup(request):
    return render (request,"signup.html")

def login(request):
    return render (request,"login.html")