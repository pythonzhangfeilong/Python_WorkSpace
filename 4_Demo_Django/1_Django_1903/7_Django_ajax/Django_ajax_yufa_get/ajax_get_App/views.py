from django.shortcuts import render
from ajax_get_App import models

def func_ajax_get(request):
    if request.method == 'GET':
        # get后面小括号中的内容一定要与html中name属性的值一致
        username = request.GET.get('username')
        password = request.GET.get('password')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        # 在服务器输出，也可以不写
        print(username, password, email, phone)

        # 保存到数据库
        models.Ajax_get.objects.create(
            # models中的变量名=views中的变量名
            Username=username,
            Password=password,
            Email=email,
            Phone=phone,
        )
    return render(request,'ajax_get.html')


