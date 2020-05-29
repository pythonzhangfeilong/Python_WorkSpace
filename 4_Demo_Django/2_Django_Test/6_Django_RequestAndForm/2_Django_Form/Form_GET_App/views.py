from django.shortcuts import render
from Form_GET_App import models
def func_reqform(request):
    return render(request,'reqform.html')

def func_get_form(request):
    # GET必须大写
    if request.method=='GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        # 在服务器输出，也可以不写
        print(username, password, email, phone)
        # 保存到数据库
        models.Index.objects.create(
            # models.py中的变量名=views.py中的变量名
            Username=username,
            Password=password,
            Email=email,
            Phone=phone,
        )
    return render(request,'GET_form.html')