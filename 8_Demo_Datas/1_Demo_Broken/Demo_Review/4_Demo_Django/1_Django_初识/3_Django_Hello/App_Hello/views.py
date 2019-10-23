from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

# 注意Django视图函数的第一个默认参数必须是request
def func_hello(request):
    return HttpResponse('Hello Word')


# 在函数的后面机上特定的参数就会访问到记录内容，比如：page（页）
def func_page(request,page):
    return HttpResponse('you look page %s'%page)