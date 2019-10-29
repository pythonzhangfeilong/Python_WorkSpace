from django.shortcuts import render
from .models import Proxy
# Create your views here.

def index(request):
    p=Proxy.objects.all()
    return render(request,'index.html',locals())