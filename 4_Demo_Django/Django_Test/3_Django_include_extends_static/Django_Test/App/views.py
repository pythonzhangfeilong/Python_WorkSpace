from django.shortcuts import render
from django.shortcuts import HttpResponse

# App的url配置使用
def func_AppProject_views(request):
    return HttpResponse('兄弟，你好呀')
# 在HTML中通过a标签中的href引用，可以直接跳转的其他网站
def func_href(request):
    return render(request,'href.html')
# 继承使用
def func_exteds(request):
    return render(request,'extends_base.html')
