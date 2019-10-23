from django.shortcuts import render
from django.shortcuts import HttpResponse
# 模板加载和url地址配置使用的函数
def dsapp_views(request):
    return HttpResponse('兄弟，你好呀')

# 浏览器中url反向解析使用的函数
def dsapp_url(request):
    return render(request,'index.html')
