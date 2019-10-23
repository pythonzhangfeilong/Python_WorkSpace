from django.shortcuts import render
# HttpResponse在页面直接响应字符串使用
from django.shortcuts import HttpResponse
# 第一个相应函数的参数必须是request
def func_http(request):
    # 响应字符串的时候不需要加上request参数，响应页面模板的时候就需要加上request
    return HttpResponse('你好呀')

