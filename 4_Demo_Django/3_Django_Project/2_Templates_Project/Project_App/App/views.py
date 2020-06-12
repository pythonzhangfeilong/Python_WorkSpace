from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.loader import get_template

# Create your views here.

# 数据在页面的响应
def App_views(request):
    templates=get_template('index.html')
    context={
        'name':'zhang',
        'addr':'呼和浩特',
        'phone':'15288888888'
    }
    return HttpResponse(templates.render(context))

# 包含include
from django.shortcuts import render
def framework_page(request):
    return render(request, 'framework.html')

# 继承extends
def extends(request):
    return render(request,'extends_base.html')

# 静态文件加载
def ststic(request):
    return render(request,'news.html')













