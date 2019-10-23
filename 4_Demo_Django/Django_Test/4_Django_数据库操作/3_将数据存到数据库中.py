'''
1、将数据存到数据的时候需要注意:
    settings.py文件中INSTALLED_APPS里面有App的名字
    数据库服务已经启动
接下来就是settings.py文件中DATABASE的配置：
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_datagodatabase',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}
'''

'''
2、在models.py文件中写入：
from django.db import models

# 创建的这个类名就是表名，必须继承models.Model
class UserData(models.Model):
    # 变量名username是表中的字段名
    username=models.CharField(max_length=32,verbose_name='用户名')
    # 变量名password是表中的字段名
    password=models.CharField(max_length=32,verbose_name='密码')
    
    # 凡是打印类的实例，都会显示出返回这个参数
    def __str__(self):
        return '用户名：%s'%self.username
'''

'''
3、在pycharm中Terminal中输入：
python manage.py makemigrations     在App文件夹中的migrations目录中生成一个0001_initial.py迁移记录文件
python manage.py migrate            在数据库中创建App的表
'''

'''
4、在views.py中写入：
from django.shortcuts import render
# 导入models文件
from GoDatabase_App import models
def func_index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库,userData折models中的类名，也就是标名因为models中变量名设置的是username和password所以就出现了下面的情况
        models.UserData.objects.create(username=username,password=password)
    # 从数据库中读取所有的数据
    # user_Data_list=models.UserData.objects.all()
    return render(request, 'index.html')# {'data': user_Data_list}
'''

'''
    5、在templates文件夹中创建index.html写入
    <h1>用户输入</h1>
    <form action="/index/" method="post">
        {% csrf_token %}
        用户名:<input type="text" name="username"/>
        <br>
        密码:<input type="password" name="password"/>
        <br>
        <button type="submit">提交</button>
    </form>
'''


'''
6、在urls.py文件中写入：
from GoDatabase_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.func_index),
]
'''









