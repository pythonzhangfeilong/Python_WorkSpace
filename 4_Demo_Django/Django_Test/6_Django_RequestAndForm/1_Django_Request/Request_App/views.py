from django.shortcuts import render

# 查看request中包含的方法
# def index(request):
#     return render(request,'index.html',context={'req':dir(request)})

# 后端处理逻辑,前端直接显示
def index(request):
    return render(request,'index.html',context={'request':request})