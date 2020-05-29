# 1、Django安装：直接采用的是pip install Django
'''
    1、如果之前安装的Django版本较低，可以采用pip uninstall Django卸载，再重新安装
    2、安装过程中出现问题是，要记得更新pip，更新命令python -m pip install --upgrade pip
    3、pip安装时要使用系统的最高管理员权限，否则会出错
'''

# 2、使用pycharm创建项目时，注意在More Settings中加上app的名字，这样的项目直接就有app，不用再次命令行创建
'''
    1、创建好Diango文件后，个文件夹的名字含义：
        __init__        空文件
        settings        主配置文件
        urls            主路由文件
        wsgi            网关接口
        templates       HTML文件编辑目录
        manage          项目个管理脚本(也就是使用命令行的时候会用到)
        
        注意：如果在写前端时，一些导入性的文件要自己新建一个static的文件夹，把他们放进去
        
    2、创建APP时在More Settings编写后就不用管了，但是没有编写就要采用下面命令行的模式去创建
        创建app的命令行python manage.py startapp login    (这样就是创建了一个叫login的文件夹，文件夹中有各个相关联的文件)
        
'''

# 3、路由编写urls
'''
    1、路由是浏览器输入url，在Django服务器响应url的转发中心。
        路由都写在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑也就是视图
    2、要在urls中导入APP中的views文件，from APP import views
    3、接下来就是在urlpatterns中写path('index/',views.index)    最重要的是视图后面的函数 
'''

# 4、编写视图函数views，路由转发用户请求到视图函数。视图函数处理用户请求，也就是编写业务处理逻辑，一般都在views.py文件里
'''
    1、首先要导入一个HTTP模块，也就是from django.shortcuts import HttpResponse
    
    注意：函数的名字要与urls中的名字一样，第一个参数最好是使用request
    def index(request):
        不能直接返回字符串，必须要由HttpResponse封装起来，才能被HTTP识别到
        return HttpResponse('Hello world')
    
    ###通过上面的操作将index这个url指向了views里的index()视图函数，它接收用户请求，并返回一个“hello world”字符串。
'''

# 5、运行web服务
'''
    1、采用命令行运行是 python manage.py runserver 127.0.0.1:8000
    2、在pycharm中直接在右上角有个类似播放的绿箭头，运行就行
    3、或者点击向下的箭头，在Edit Configurations中编辑运行的内容
    4、运行时出现404报错，在url后面拼接执行的文件刷新就好，https://127.0.0.1:8000/index
'''

# 6、返回HTML文件操作
'''
    1、首先在templates中创建一个index.html文件
    2、然后再在views中导入from django.shortcuts import render
    def index(request):
        render方法使用数据字典和请求元数据，渲染一个指定的HTML模板，其中多个参数，第一个参数必须是request，第二个参数是HTML
        return render(request,'index.html')
        
    3、为了让Django知道HTML文件在哪里，需要在settings中设置
    在settings中找到TEMPLATES=[{
        'DIRS':[os.path.join(BASE_DIR,'templates')]
    }]
'''

# 7、使用静态文件
'''
    1、将HTML文件返还给用户了，但是这还不够，前端三大块HTML、CSS、JavaScript，还有各种插件，它们齐全才是一个完整的页面。
        在Django中，创建一个static目录，将这些静态文件放在static目录中。
    2、为了让Django找到static这个目录，需要在settings中，
    找到STATIC_URL='/static/'下面编写         STATIC_URL='/static/'的作用是浏览器访问静态文件时加载的前缀部分，比如https://127.0.0.1:8000/static/login.jpg
        STATICFILES_DIRS=[
            os.path.join(BASE_DIR,'static')
        ]
    3、上面的bain写好就可以在template文件夹的index.html文件中引用静态文件了
    <script src='/static/js/jquery-3.2.1.min.js'></script>
'''

# 8、接受用户发送的数据
'''
    将一个要素齐全的HTML文件返还给了用户浏览器。但这还不够，因为web服务器和用户之间没有动态交互。
    下面设计一个表单，让用户输入用户名和密码，提交给index这个url，服务器将接收到这些数据
    1、首先修改index.html，修改时注意action是html的名字，不带后缀名
        <h1>兄弟，你好</h1>
        <form action="/index/" method="post">
            {% csrf_token %}
            <div>
                <p>用户名:<input type="text" name="username" title="请输入用户名"></p>
                <p>密码:<input type="text" name="password" title="请输入密码"></p>
                <p><button type="submit">提交</button></p>
            </div>
        </form>
    2、修改完html后是不能直接输入信息的，这时需要修改views
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password)
        return render(request,'index.html')
    3、这是刷新页面是会报403错误的，因为Django有一个跨站请求保护机制，要在html的form表单中加入{%csrf_token%}
'''

# 9、返回动态页面，收到了用户的数据，但是返回给用户依然是一个静态页面，通常会根据用户的数据，进行处理后再返回给用户
'''
    1、先修改views
        # 创建一个空列表
        user_list=[]
        def index(request):
            if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')
                print(username,password)
        
            # 将用户发送过来的数据，构建成一个字典
            temp={'user':username,'pwd':password}
            # 将字典内容添加到列表中
            user_list.append(temp)
            # 将用户的数据返回给html
            return render(request,'index.html',{'date':user_list})
    再修改index.html
        <div class="bk">
            <h1>用户输入</h1>
            <form action="/index/" method="post">
                {% csrf_token %}
                <div>
                    <p>用户名:<input type="text" name="username" title="请输入用户名"></p>
                    <p>密码:<input type="text" name="password" title="请输入密码"></p>
                    <p><button type="submit">提交</button></p>
                </div>
            </form>
        </div>

        <div class="bk">
            <h1>用户展示</h1>
            <table>
                <thead>
                    <tr>用户名</tr>
                    <tr>密码</tr>
                </thead>
    
                <tbody>
                    {% for item in date %}
                        <tr>
                            <td>{{ item.user }}</td>
                            <td>{{ item.pwd }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>   
'''

# 10、 数据库的使用，使用数据库的需求是毫无疑问的，Django通过自带的ORM框架操作数据库，并且原生支持轻量级的sqlite3数据库。
'''
    1、在使用个数据库的时候，首先要在settings中的INSTALLED_APPS添加自己的app名字,不注册它，数据库就不知道给那个app创建数据库
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'APP.apps.AppConfig',
        'APP',
        ]
    2、在settings中的DATABASES配置，默认的是sqlite3
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_database',
            'USER':'root',
            'PASSWORD':'',
            'HOST':'127.0.0.1',
            'PORT':'3306',
            }
        }
    3、再编辑models
        #首先要继承这个类是固定的写法
            class UserInfo(models.Model):
                user=models.CharField(max_length=32)
                pwd=models.CharField(max_length=32)
        # 创建上面的俩个字段，用来保存用户名和密码
            1、在pycharm的Terminal中输入python manage.py makemigrations，
              会在login目录中的migrations目录中生成一个0001_initial.py迁移记录文件。
            2、再输入python manage.py migrate,执行成功就会创建好数据库表
    4、再编辑views
        # 将提交的用户名和密码保存在数据库中
            from APP import models
            def index(request):
                if request.method=='POST':
                    username=request.POST.get('username')
                    password=request.POST.get('password')
                    # 将数据保存在数据库中
                    models.UserInfo.objects.create(user=username,pwd=password)
            
                # 从数据库中读取所有的数据
                user_list=models.UserInfo.objects.all()
                return render(request,'index.html',{'date':user_list})
    
    
    
    
    
    
'''
































