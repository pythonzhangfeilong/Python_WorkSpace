#一、采用get请求的方式搭建ajax
'''
1、创建Django项目之后找到settings.py文件中的DATABSASE，修改为下面的内容：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_ajax_get',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

2、在settings.py文件中找到MIDDLEWARE将'django.middleware.csrf.CsrfViewMiddleware'跨域请求验证注销

3、在settings.py文件中找到LANGUAGE_CODE和TIME_ZONE修改为下面的内容:
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

4、在models.py文件中写入：
from django.db import models
class Ajax_get(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')
    def __str__(self):
        return '用户名%s'%self.Username

5、由于ajax提交提交操作的是jquery，所以要在jquery官网复制源码，还需要在本地文件中配置静态文件夹
首先在项目的最外层目录下，创建一个static的文件夹
在settings.py的末尾加入：
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
在static文件夹下创建js文件夹，在js文件夹下创建jquery.js文件，将jquery官网复制的jquery文件放进去

6、在templates文件夹创建ajax_get.html,写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax_get</title>
</head>
<body>
<form action="/ajax_get/" method="get">
    姓名：<input type="text" id="username" name="username"><br>
    密码：<input type="password" id="paassword" name="password"><br>
    邮箱：<input type="email" id="email" name="email"><br>
    电话：<input type="text" id="phone" name="phone"><br>
    <button type="submit" id="tj">提交</button><br>
</form>
<script>
    $(function(){
        $('#tj').click(function(){
            var username=$('#username').val();
            var password=$('#password').val();
            var email=$('#email').val();
            var phone=$('#phone').val();
        $.ajax({
            {#url请求地址，其实就是html中from标签中actions后面的参数#}
            url:'/ajax_get/',
            {#type请求类型,默认的是GET#}
            type:'GET',
            {#async是异步请求通过true和false来控制是否开启#}
            async:'true',
            {#data发送到服务器的数据#}
            data:{'username':username,'password':password,'email':email,'phone':phone},
            {#dataType从服务器返回的数据#}
            dataType:'json',
            {#请求成功之后的回掉函数#}
            success:function (data) {
                console.log(data)
            },
            {#请求失败之后的回掉函数#}
            error:function (data) {
                console.log(data)
            }
        })
        })
    })
</script>
</body>
</html>

7、在views.py中写入：
from django.shortcuts import render
from ajax_get_App import models

def func_ajax_get(request):
    if request.method=='GET':
        # get后面小括号中的内容一定要与html中name属性的值一致
        username=request.GET.get('username')
        password=request.GET.get('password')
        email=request.GET.get('email')
        phone=request.GET.get('phone')
        # 在服务器输出，也可以不写
        print(username,password,email,phone)

        # 保存到数据库
        models.Ajax_get.objects.create(
            # models中的变量名=views中的变量名
            Username=username,
            Password=password,
            Email=email,
            Phone=phone,
        )
    return render(request,'ajax_get.html')

8、在urls.py中写入：
from ajax_get_App import views
urlpatterns = [
    path('ajax_get/',views.func_ajax_get)
]

9、在pycharm的Terminal中写入python manage.py check检查有没有错误,出现System check identified no issues (0 silenced).就是没错误
   在pycharm的Terminal中写入python manage.py makemigrations生成数据库表
   在pycharm的Terminal中写入python manage.py migrate迁移数据库表
10、启动Django服务浏览器访问http://127.0.0.1:8000/ajax_get/
'''

# 二、采用post方式搭建ajax
'''
1、创建Django项目之后找到settings.py文件中的DATABSASE，修改为下面的内容：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_ajax_get',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

2、在settings.py文件中找到MIDDLEWARE将'django.middleware.csrf.CsrfViewMiddleware'跨域请求验证注销

3、在settings.py文件中找到LANGUAGE_CODE和TIME_ZONE修改为下面的内容:
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

4、在models.py文件中写入：
from django.db import models
class Ajax_post(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')
    def __str__(self):
        return '用户名%s'%self.Username

5、由于ajax提交提交操作的是jquery，所以要在jquery官网复制源码，还需要在本地文件中配置静态文件夹
首先在项目的最外层目录下，创建一个static的文件夹
在settings.py的末尾加入：
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
在static文件夹下创建js文件夹，在js文件夹下创建jquery.js文件，将jquery官网复制的jquery文件放进去

6、在templates文件夹中创建ajax_post.html写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax_post</title>
    <script type="text/javascript" src="/static/js/jquery.js"></script>
</head>
<body>
<form action="/ajax_get/" method="post">
    姓名：<input type="text" id="username" name="username"><br>
    密码：<input type="password" id="paassword" name="password"><br>
    邮箱：<input type="email" id="email" name="email"><br>
    电话：<input type="text" id="phone" name="phone"><br>
    <button type="submit" id="tj">提交</button><br>
</form>
<script>
    $(function(){
        $('#tj').click(function(){
            var username=$('#username').val();
            var password=$('#password').val();
            var email=$('#email').val();
            var phone=$('#phone').val();
        $.ajax({
            {#url请求地址，其实就是html中from标签中actions后面的参数#}
            url:'/ajax_post/',
            {#type请求类型,默认的是GET#}
            type:'POST',
            {#async是异步请求通过true和false来控制是否开启#}
            async:'true',
            {#data发送到服务器的数据#}
            data:{'username':username,'password':password,'email':email,'phone':phone},
            {#dataType从服务器返回的数据#}
            dataType:'json',
            {#请求成功之后的回掉函数#}
            success:function (data) {
                console.log(data)
            },
            {#请求失败之后的回掉函数#}
            error:function (data) {
                console.log(data)
            }
        })
        })
    })
</script>
</body>
</html>

7、在views.py中写入：
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

8、在urls.py中写入：
from ajax_post_App import views
urlpatterns = [
    path('ajax_post/',views.func_ajax_get)
]

9、在pycharm的Terminal中写入python manage.py check检查有没有错误,出现System check identified no issues (0 silenced).就是没错误
   在pycharm的Terminal中写入python manage.py makemigrations生成数据库表
   在pycharm的Terminal中写入python manage.py migrate迁移数据库表
10、启动Django服务浏览器访问http://127.0.0.1:8000/ajax_post/
'''