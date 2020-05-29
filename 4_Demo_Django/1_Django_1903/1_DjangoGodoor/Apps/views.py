from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# 注意第一个函数的参数默认的是request
def index(request):
    # return HttpResponse('Hello Word')
    # return JsonResponse({'Hello':'Word'})
    return render(request,'index.html')
def func():
    return render_to_response('index.html')
# def page_index(request,data):
#     return HttpResponse('Response de data is %s'%data)

def page_index(request,test):
    return HttpResponse('Response de data is %s'%test)