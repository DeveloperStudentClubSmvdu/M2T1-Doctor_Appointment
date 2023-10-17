from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



def home(request):
    return render(request,"index.html")