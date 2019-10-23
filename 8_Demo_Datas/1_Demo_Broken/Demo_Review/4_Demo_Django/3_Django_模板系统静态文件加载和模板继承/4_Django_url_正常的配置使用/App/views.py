from django.shortcuts import render
from django.shortcuts import HttpResponse
# 页面响应字符串函数
def func(request):
    return HttpResponse('你好')
# 页面响应模板函数
def func_f(request):
    return render(request,'index.html')

