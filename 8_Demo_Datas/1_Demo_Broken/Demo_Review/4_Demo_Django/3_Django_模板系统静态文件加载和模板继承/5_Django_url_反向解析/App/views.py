from django.shortcuts import render
from django.shortcuts import HttpResponse
# 页面响应视图函数字符串
def func_str(request):
    return HttpResponse('你好呀')

# 页面响应视图函数模板
def func_html(request):
    return render(request,'index.html')






















