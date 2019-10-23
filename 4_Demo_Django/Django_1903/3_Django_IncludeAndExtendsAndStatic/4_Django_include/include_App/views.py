#####render和render_to_response的区别
'''
    render是需要request参数的
    render_to_response不需要request参数
'''
from django.shortcuts import render
from django.shortcuts import render_to_response

def func_yuanwork(request):
    return render(request,'yuanwork.html')