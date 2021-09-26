from django.shortcuts import render
from django.http import HttpResponse ##import django http response

##request. home. handle these things. return what users want to see

# Create your views here.
def home(request): ##handle the traffic
    return HttpResponse('</h1>Blog Home</h1>')
def about(request) :
    return HttpResponse('</h1>Blog About</h1>')
##we need url pattern! lets creat urls.py and map the url for each view function