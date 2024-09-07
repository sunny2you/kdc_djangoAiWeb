from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>lotto</h1>')

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
# Create your views here.
