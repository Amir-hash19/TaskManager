from django.shortcuts import render, redirect
from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse("this is home page massage ")