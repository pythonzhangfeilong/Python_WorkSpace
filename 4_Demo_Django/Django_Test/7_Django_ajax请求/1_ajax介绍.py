#####ajax优缺点
'''
Ajax（Asynchronous Javascript And XML：异步 JavaScript 和 XML），是指一种在无需重新加载整个网页的情况下，能够
    更新部分网页的技术。
使用Ajax的最大优点，就是能在不更新整个页面的前提下维护数据。这使得Web应用程序更为迅捷地回应用户动作，并避免了在网络
    上发送那些没有改变的信息。
但是Ajax可能破坏浏览器的后退与加入收藏书签功能。在动态更新页面的情况下，用户无法回到前一个页面状态，这是因为浏览器仅
    能记下历史记录中的静态页面。
'''

#####ajax定义
'''
Ajax有最初是由js编写的，后来随着js框架的发展，jq，vue等大型框架都对ajax进行了封装,工作中最常用的是jquery的ajax请求
'''
# 把数据保存到数据库实例：
'''
1、创建一个django项目，在templates文件夹中创建一个ajax.html文件，写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
    <script type="text/javascript" src="/static/js/jquery.js"></script>
</head>
<body>
<form action="">
    姓名：<input type="text" id="username">
    密码：<input type="passsword" id="paassword">
    邮箱：<input type="email" id="email">
    电话：<input type="text" id="phone">
    <button type="submit" id="tj">提交</button>
</form>
</body>
</html>

2、在项目最外层文件夹创建static文件夹，在jquery的官网下载jquery，并且按照/static/js/jquery.js存放
3、在settings.py文件的最后加入STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
4、修改settings.py文件的LANGUAGE_CODE和TIME_ZONE为下面的内容
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
5、在urls.py中写入：
from ajax_App import  views
urlpatterns = [
    path('ajax/',views.func_ajax)
]
6、在views.py中写入:
def func_ajax(request):
    render(request,'ajax.html')
7、启动django服务，在浏览器中访问http://127.0.0.1:8000/ajax/

8、在models.py中写入数据库模型：
class Ajax(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')
    def __str__(self):
        return '用户名%s'%self.Username

9、生成数据库表：python manage.py makemigrations
   迁移数据库表：python manage.py migrate
   
10、编写views.py文件中的逻辑
from django.shortcuts import render
from ajax_App.models import Ajax
def func_ajax(request):
   # 注意if后面的写法固定格式
   if request.method=='POST':
      # get后面括号中的参数是与html中的那么一致
      username=request.POST.get('username')
      password=request.POST.get('password')
      emaile=request.POST.get('email')
      phone=request.POST.get('phone')
      print(username,password,emaile,phone)

      models.Ajax.objects.create(
        # models中的变量名=views中的变量名
         Username=username,
         Password=password,
         Email=emaile,
         Phone=phone
      )
   return render(request,'ajax.html')

11、刷新页面提交参数即可存入数据库
'''

























