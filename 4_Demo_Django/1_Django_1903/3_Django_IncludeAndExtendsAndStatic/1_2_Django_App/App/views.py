from django.shortcuts import render
from django.shortcuts import HttpResponse

def func_App(request):
    return HttpResponse('兄弟，你好呀！')

