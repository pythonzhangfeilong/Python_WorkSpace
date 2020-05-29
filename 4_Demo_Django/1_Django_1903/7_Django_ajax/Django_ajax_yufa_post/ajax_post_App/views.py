from django.shortcuts import render
from ajax_post_App import models

def func_ajax_post(request):
    if request.method=='POST':
        # get后面小括号中的内容一定要与html中name属性的值一致
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        # 在服务器输出，也可以不写
        print(username,password,email,phone)

        # 保存到数据库
        models.Ajax_post.objects.create(
            # models中的变量名=views中的变量名
            Username=username,
            Password=password,
            Email=email,
            Phone=phone,
        )
    return render(request,'ajax_post.html')
