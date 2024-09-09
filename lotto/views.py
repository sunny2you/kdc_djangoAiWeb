from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos=GuessNumbers.objects.all()
    print(lottos)
    return render(request,'lotto/default.html',{'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
# Create your views here.

def post(request):
    form=PostForm()
    return render(request,"lotto/form.html",{"form":form})


