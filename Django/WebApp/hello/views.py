from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ithri(request):
    return HttpResponse("Hello, Ithri!")

def ojnna(request):
    return HttpResponse("Hello, Ojnna!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

