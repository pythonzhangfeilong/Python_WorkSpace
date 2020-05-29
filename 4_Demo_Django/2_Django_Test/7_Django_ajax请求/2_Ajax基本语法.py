#####Ajax基本语法：
'''
1、ajax语法格式：
jQuery.ajax( url [, settings ] )

参数解释：
    url ：类型: String ，一个用来包含发送请求的URL字符串。
    settings ：类型: PlainObject 一个以"{键:值}"组成的AJAX 请求设置。所有选项都是可选的。可以使用$.ajaxSetup()设置
        任何默认参数。看jQuery.ajax( settings )下所有设置的完整列表。

2、常用setting配置介绍：
method :(default: 'GET') Type: String HTTP 请求方法 (比如："POST", "GET ", "PUT")。(添加版本: 1.9.0)。（手册网注：如果你使用jQuery 1.9.0 之前的版本，你需要使用type选项。）
success: Type: Function( Anything data, String textStatus, jqXHR jqXHR ) 请求成功后的回调函数。这个函数传递3个参数：从服务器返回的数据，并根据dataType参数进行处理后的数据或dataFilter回调函数，如果指定的话；一个描述状态的字符串;还有 jqXHR对象 。
type (默认: 'GET') :类型: String
method选项的别名。如果你使用jQuery 1.9.0 之前的版本，你需要使用type选项。
url (默认: 当前页面地址) 类型: String 发送请求的地址。
async (默认: true) 类型: Boolean 默认设置下，所有请求均为异步请求（也就是说这是默认设置为 true ）。如果需要发送同步请求，请将此选项设置为 false 。跨域请求和 dataType: "jsonp" 请求不支持同步操作。注意，同步请求将锁住浏览器，用户其它操作必须等待请求完成才可以执行
beforeSend 类型: Function( jqXHR jqXHR, PlainObject settings ) 请求发送前的回调函数，用来修改请求发送前jqXHR（在jQuery 1.4.x的中，XMLHttpRequest）对象，此功能用来设置自定义 HTTP 头信息，等等。该jqXHR和设置对象作为参数传递。这是一个Ajax事件 。在beforeSend函数中返回false将取消这个请求。
contents类型: PlainObject 一个以"{字符串/正则表达式}"配对的对象，根据给定的内容类型，解析请求的返回结果。
data 类型: PlainObject 或 String 或 Array 发送到服务器的数据。它被转换成一个查询字符串,如果已经是一个字符串的话就不会转换。查询字符串将被追加到GET请求的URL后面。对象必须为"{键:值}"格式。如果这个参数是一个数组，会自动转换成&name=for&user=if
dataType (default: Intelligent Guess (xml, json, script, or html)) Type: String 从服务器返回你期望的数据类型。 可用的类型（以及结果作为第一个参数传递给成功回调函数）有：
"xml": 返回 XML 文档，可以通过 jQuery 处理。
"html": 返回纯文本 HTML 文本；包含的script标签会在插入DOM时执行。
"script": 把响应的结果当作 JavaScript 执行，并将其当作纯文本返回。
"jsonp": 以 JSONP 的方式载入 JSON 数据块。
"text": 返回纯文本字符串。
'''

#####ajax搭建
'''
一、采用get请求的方式搭建ajax
1、配置settings.py文件中的DATABSE为下面的内容：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_ajax_yufa',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': ''
    }
}
2、在models.py文件中写入：
class Ajax(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')
    def __str__(self):
        return '用户名%s'%self.Username
3、在templates文件夹创建ajax.html,写入
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
    <script type="text/javascript" src="/static/js/jquery.js"></script>
</head>
<body>
<form action="/ajax/" method="get">
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
            {#url其实就是html中from标签中actions后面的参数#}
            url:'/ajax/',
            {#type请求的类型，默认的是GET#}
            type:'GET',
            {#async异步请求通过true和false来控制是否开启#}
            async:'true',
            {#data发送到服务器的数据#}
            data:{'username':username,'password':password,'email':email,'phone':phone},
            {#从服务器返回自己期望所需要的类型#}
            dataType:'json',
            {#请求成功之后的回掉函数#}
            success:function(data){
                console.log(data)
            },
            {#请求失败后的回掉函数#}
            error:function(data){
                console.log(data)
            }
            })
        })
    })
</script>
</body>
</html>

4、在views.py文件中写入：
from django.shortcuts import render
from ajax_App import models
def func_ajax(request):
   if request.method=='GET':
      username=request.GET.get('username')
      password=request.GET.get('password')
      emaile=request.GET.get('email')
      phone=request.GET.get('phone')
      print(username,password,emaile,phone)

      models.Ajax.objects.create(
         Username=username,
         Password=password,
         Email=emaile,
         Phone=phone
      )
   return render(request,'ajax.html')
5、在urls.py文件中写入：
from ajax_App import views
urlpatterns = [
    path('ajax/', views.func_ajax)
]
6、在pycharm的Terminal中写入python manage.py check检查有没有错误
   在pycharm的Terminal中写入python manage.py makemigrations生成数据库表
   在pycharm的Terminal中写入python manage.py migrate迁移数据库表
7、在settings.py中找到MIDDLEWARE将里面的跨域请求注释掉'django.middleware.csrf.CsrfViewMiddleware'
8、启动Django服务浏览器访问http://127.0.0.1:8000/ajax/



二、采用post请求的方式搭建ajax
1、配置settings.py文件中的DATABSE为下面的内容：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_ajax_yufa',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': ''
    }
}
2、在models.py文件中写入：
class Ajax(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')
    def __str__(self):
        return '用户名%s'%self.Username
3、在templates文件夹创建ajax.html,写入
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
    <script type="text/javascript" src="/static/js/jquery.js"></script>
</head>
<body>
<form action="/ajax/" method="post">
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
            {#url其实就是html中from标签中actions后面的参数#}
            url:'/ajax/',
            {#type请求的类型#}
            type:'POST',
            {#async异步请求通过true和false来控制是否开启#}
            async:'true',
            {#data发送到服务器的数据,将跨域请求伪造也一起发送#}
            data:{'username':username,'password':password,'email':email,'phone':phone,'csrfmiddlewaretoken':csrftoken},
            {#从服务器返回自己期望所需要的类型#}
            dataType:'json',
            {#请求成功之后的回掉函数#}
            success:function(data){
                console.log(data)
            },
            {#请求失败后的回掉函数#}
            error:function(data){
                console.log(data)
            }
            })
        })
    })
</script>
</body>
</html>

4、在views.py文件中写入：
from django.shortcuts import render
from ajax_App import models
def func_ajax(request):
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      emaile=request.POST.get('email')
      phone=request.POST.get('phone')
      print(username,password,emaile,phone)

      models.Ajax.objects.create(
         Username=username,
         Password=password,
         Email=emaile,
         Phone=phone
      )
   return render(request,'ajax.html')
5、在urls.py文件中写入：
from ajax_App import views
urlpatterns = [
    path('ajax/', views.func_ajax)
]
6、在pycharm的Terminal中写入python manage.py check检查有没有错误
   在pycharm的Terminal中写入python manage.py makemigrations生成数据库表
   在pycharm的Terminal中写入python manage.py migrate迁移数据库表
7、在settings.py中找到MIDDLEWARE将里面的跨域请求注释掉'django.middleware.csrf.CsrfViewMiddleware'
8、启动Django服务浏览器访问http://127.0.0.1:8000/ajax/
'''







