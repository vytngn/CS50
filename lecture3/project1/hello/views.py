from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def banhmi(request):
    return HttpResponse("Hello, Banhmi!")

def photai(request):
    return HttpResponse("Hello, Photai!")

def greet(request, name):
    return render(request, "hello/greet.html", {
         "name": name.capitalize()         
    })