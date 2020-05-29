#####form表单的定义：
'''
    在开发的过程中向服务器提交数据保存在数据库的操作是必不可少的，而常用的方式就是前端的form表单提交数据到服务器
'''


# 1、form表单的定义：
'''
    1、首先在templates文件夹中创建reqform.html文件，写入：
        <form action="/reqform/" method="post">
            {% csrf_token %}
            姓名:<input type="text" name="username"><br>
            密码:<input type="password" name="password"><br>
            邮箱:<input type="email" name="email"><br>
            电话:<input type="text" name="phone"><br>
            <input type="submit" value="提交">
        </form>
        参数解释:action="/reqform/"是提交页面的地址
                method="post"是请求的方式
                {% csrf_token %}跨域请求
    2、在Form_GET_App文件夹里的views.py中编写页面响应函数,写入：
        def func_reqform(request):
            return render(request,'reqform.html')
    3、在项目的根目录中配置urls.py文件，写入：
        from Form_App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('reqform/',views.func_reqform)
        ]
    4、启动Django服务，在浏览器的地址栏中输入：http://127.0.0.1:8000/reqform/
'''

# 2、form表单的属性：
'''
action 提交的路径，我们要把数据提交到哪里，如果不行，默认提交到当前url指定的视图上method 提交的方式，request常见的方式
get  GET请求会向数据库发索取数据的请求，从而来获取信息，该请求就像数据库的select操作一样，只是用来查询一下数据，不会修
    改、增加数据，不会影响资源的内容，即该请求不会产生副作用。无论进行多少次操作，结果都是一样的。
Post 向服务器端发送数据的，但是该请求会改变数据的种类等资源，就像数据库的insert操作一样，会创建新的内容。几乎目前所有的
    提交操作都是用POST请求的。
Put PUT请求是向服务器端发送数据的，从而改变信息，该请求就像数据库的update操作一样，用来修改数据的内容，但是不会增加数据
    的种类等，也就是说无论进行多少次PUT操作，其结果并没有不同。
Delete 请求顾名思义，就是用来删除某一个资源的，该请求就像数据库的delete操作。
'''

# 3、form表单的input类型和关键参数
'''
    input类型:
        button 按钮；
        checkbox 选择框；
        file 文件；
        hidden 隐藏域；
        image 图片；
        password 密码域
        radio 单选框；
        submit 提交按钮；
        text  文本域
        
    数据提交过程当中，对于input最为重要的参数:
        name 决定提交数据的结构；
        value 提交数据的值
        submit是最为传统的一种提交方式，它会将表单当中所有的input提交到action指定的路径上。
    
    1、数据的发送：
        数据发送是通过html中的submit来提交进行发送
    2、数据的接收：
        前段数据提交后，可以通过视图函数对应的方法进行接收和判断
        
        常用的request方法：
            request.GET	Get请求的数据字典
            request.POST	POST请求的数据字典
            request.method	请求的方法
    3、Csrf（Cross-site request forgery）
        跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。
            Django中crsf跨域请求伪造有俩种处理方式：
                1、直接在settings.py文件中的MIDDLEWARE里，直接注销'django.middleware.csrf.CsrfViewMiddleware'
                2、在每一个form表单里插入{% csrf_token %}        注意：推荐使用这种，注销settings.py文件中的内容不安全
'''

# 4、form表单的get请求，并且提交给数据库：
'''
    get请求是将参数包含在了url中进行传递，这样的传递方式不保密，而且还有大小限制
    
    1、在templates文件夹中创建GET_form.html，写入：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>GET_form</title>
        </head>
        <body>
            <form action="/reqform/" method="get">
                {% csrf_token %}
                姓名:<input type="text" name="username"><br>
                密码:<input type="password" name="password"><br>
                邮箱:<input type="email" name="email"><br>
                电话:<input type="text" name="phone"><br>
                <input type="submit" value="提交">
            </form>
        </body>
        </html>
    2、在Form_GET_App文件夹views.py文件中写入：
        def func_get_form(request):
            # GET必须大写
            if request.method=='GET':
                try:
                    username = request.GET.get('username')
                    password = request.GET.get('password')
                    email = request.GET.get('email')
                    phone = request.GET.get('phone')
                    # 在服务器中输出，也可以不写
                    print(username, password, email, phone)
                except:
                    pass
            return render(request,'reqform.html')
    3、在urls.py里的urlpatterns中写入：
        path('get_form/',views.func_get_form)
    4、在浏览器的地址栏中输入：http://127.0.0.1:8000/reqform，在页面的输入框填写信息，点击提交，地址里就会变为
    http://127.0.0.1:8000/reqform/?csrfmiddlewaretoken=T380ybYr3SApnbnrPfzDSnm3GLaarW6kjg7ysMoURun4cahfIEUZTVq5vNWMHqcN&username=zhang&password=123&email=163%40qq.com&phone=15248152303
    网站地址参数详解：
        ？ 网站地址和传递参数分割符
        & 参数的链接符
    5、在settings.py中配置数据库
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'database_get_form',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD': '',
            }
        }
    6、在Form_GET_App文件夹models.py中创建数据库表和字段，写入：
        from django.db import models
        class Index(models.Model):
            username = models.CharField(max_length=12,verbose_name='用户名')
            password = models.CharField(max_length=12,verbose_name='密码')
            email = models.EmailField(max_length=12,verbose_name='邮箱')
            phone = models.CharField(max_length=12,verbose_name='手机号')
        
            class Meta():
                verbose_name='用户名'
                verbose_name_plural=verbose_name
    7、在pycharm的Terminal中写入：
        python manage.py makemigrations 生成数据库表
        python manage.py migrate 迁移数据库   
    8、在Form_GET_App文件夹views.py中写入：
    from django.shortcuts import render
    from Form_App import models
    def func_reqform(request):
        return render(request,'GET_form.html')
    
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
    9、在templates文件中创建一个GET_gorm.html,写入：
    注意：action后面写的是urls.py中path后面的第一个参数
    <form action="/get_form/" method="get">
        姓名:<input type="text" name="username"><br>
        密码:<input type="password" name="password"><br>
        邮箱:<input type="email" name="email"><br>
        电话:<input type="text" name="phone"><br>
        <input type="submit" value="提交">
    </form>
'''

# 4、form表单的post请求并且提交给数据库
'''
    post请求是将参数利用form表单提交，这种方式保密性更好，没有大小限制

    1、在templates文件夹中创建GET_form.html，写入：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>POST_form</title>
        </head>
        <body>
            <form action="/post_form/" method="post">
                姓名:<input type="text" name="username"><br>
                密码:<input type="password" name="password"><br>
                邮箱:<input type="email" name="email"><br>
                电话:<input type="text" name="phone"><br>
                <input type="submit" value="提交">
            </form>
        </body>
        </html>
    2、在Form_POST_App文件夹views.py文件中写入：
        from django.shortcuts import render
        from Form_POST_App import models 
        def func_post_form(request):
            # GET必须大写
            if request.method=='POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                # 在服务器输出，也可以不写
                print(username, password, email, phone)
                # 保存到数据库
                models.Getform.objects.create(
                    # models.py中的变量名=views.py中的变量名
                    Username=username,
                    Password=password,
                    Email=email,
                    Phone=phone,
                )
            return render(request,'POST_form.html')
    3、在Form_POST_App文件夹urls.py里的urlpatterns中写入：
        path('post_form/',views.func_post_form)
    4、在settings.py中配置数据库和添加APP
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'database_post_form',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD': '',
            }
        }
        INSTALL_APP=['Form_POST_App',]
    5、在Form_POST_App文件夹models.py中创建数据库表和字段，写入：
        from django.db import models
        class Index(models.Model):
            username = models.CharField(max_length=12,verbose_name='用户名')
            password = models.CharField(max_length=12,verbose_name='密码')
            email = models.EmailField(max_length=12,verbose_name='邮箱')
            phone = models.CharField(max_length=12,verbose_name='手机号')

            class Meta():
                verbose_name='用户名'
                verbose_name_plural=verbose_name
    7、在pycharm的Terminal中写入：
        python manage.py makemigrations 生成数据库表
        python manage.py migrate 迁移数据库   
    8、在Form_POST_App文件夹views.py中写入：
    from django.shortcuts import render
    from Form_POST_App import models
    def func_post_form(request):
        # POST必须大写
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            # 在服务器输出，也可以不写
            print(username, password, email, phone)
            # 保存到数据库
            models.Postform.objects.create(
                # models.py中的变量名=views.py中的变量名
                Username=username,
                Password=password,
                Email=email,
                Phone=phone,
            )
        return render(request,'POST_form.html')
    9、在templates文件中创建一个GET_gorm.html,写入：
    注意：action后面写的是urls.py中path后面的第一个参数
    <form action="/post_form/" method="post">
        姓名:<input type="text" name="username"><br>
        密码:<input type="password" name="password"><br>
        邮箱:<input type="email" name="email"><br>
        电话:<input type="text" name="phone"><br>
        <input type="submit" value="提交">
    </form>
'''

#POST请求方式与get一样，只是把请求的参数更改一下就好






