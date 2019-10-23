from django.shortcuts import render
from django.shortcuts import HttpResponse
# 页面响应字符串视图函数
def func_str(request):
    return HttpResponse('页面响应字符串')

# 页面响应模板试图函数
def func_templates(request):
    return render(request,'index.html')