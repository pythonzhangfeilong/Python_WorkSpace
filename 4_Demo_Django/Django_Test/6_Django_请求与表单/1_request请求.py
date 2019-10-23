#####Request请求：
'''
    1、web开发是在http协议的基础上处理各种各样的请求，用户的访问叫做请求（request），服务器的回复叫做响应（response）
'''

'''
    2、Django中的views.py文件里面放的是视图函数也就是业务逻辑，而视图函数就是用来处理响应请求的,Django给每一个函数都添加
        了一个参数用来接收请求，这个参数约定俗称的被写为request。
        在App文件夹里views.py文件中添加一个index函数，写入默认的参数request
        def index(request):
            return render(request,'index.html')
'''

'''
    3、request参数是接受的哪一些参数，采用context将获取的信息传输显示在index.html页面上，接着在views.py文件中的
        index函数中写入:(注意：context是用来把信息参数传递给html页面的，传参形式是以字典的形式)
        def index(request):
            return render(request,'index.html',context={'req':request})
'''

'''
    4、在template的文件夹下创建一个index.html并且写入：（{{ }}是用来获取接受传来的参数的，{% %}是用来写逻辑判断的）
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>index</title>
        </head>
        <body>
            {{ req }}
        </body>
        </html>
'''

'''
    5、在项目的根目录中找到urls.py文件写入：
        (注意：path后面的第一个参数是浏览器地址栏中输入127.0.0.1:8000后的第一个参数，views.index是views.py文件夹执行的函数)
        先导入App文件夹中的vies.py文件    from Request_App import views
        在urlpatterns中添加path，        path('index/',views.index)
'''

'''
    6、启动Django服务，在浏览器中输入url地址：http://127.0.0.1:8000/index/ ，就会查看到request是一个wsgi的请求对象
'''

'''
    7、查看request的请求对象中具体包含的方法，修改views.py文件中的context参数，修改为：
        注意：dir()是列出属性所包含的方法
        def index(request):
            return render(request,'index.html',context={'req':dir(request)})
'''

'''
    8、刷新页面就会看到request的所有方法
'''

'''
    9、为了减轻前段html的处理压力，采用后端逻辑处理，前端直接展示的方式，首先在views.py文件中调整index函数
        def index(request):
            return render(request,'index.html',context={'request':request})
'''

'''
    10、在index.html中写入：
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>index</title>
    </head>
    <body>
    {#查看request中包含的方法#}
    {#<p>--------------------------------</p>#}
    {#    {{ req }}#}
    {#<p>--------------------------------</p>#}
    
    {#
        request.cookies是用来存储请求的cookie的，通常我们在编写网站的时候进行cookie的校验，就是从这里校验
        request.FILES 是用来接收客户端提交的文件的数据的，比如用户上传的图片和文件.
        request.GET是用来接收客户端提交的get数据
        request.POST是用来接收客户端提交的post数据
        request.REQUEST是用来接收存储跳转的容器
        META，这个是一个字典对象
    #}
    <p>+++++++++++++++++++++++++++request COOKIES+++++++++++++++++++++++++++++++++++++++++</p>
    {{ request.COOKIES }}
    <p>+++++++++++++++++++++++++++request FILES+++++++++++++++++++++++++++++++++++++++++</p>
    {{ request.FILES }}
    <p>+++++++++++++++++++++++++++request GET+++++++++++++++++++++++++++++++++++++++++</p>
    {{ request.GET }}
    <p>+++++++++++++++++++++++++++request POST+++++++++++++++++++++++++++++++++++++++++</p>
    {{ request.POST }}
    <p>+++++++++++++++++++++++++++request REQUEST+++++++++++++++++++++++++++++++++++++++++</p>
    {{ request.REQUEST }}
    <p>+++++++++++++++++++++++++++request META+++++++++++++++++++++++++++++++++++++++++</p>

    <table border="1" bordercolor="#000000" width="1px" cellpadding = "0" cellspacing = "0">
        {% for keys,values in request.META.items %}
            <tr>
                <td>{{ keys }}:</td>
                <td>{{ values }}a</td>
            </tr>
        {% endfor %}
    </table>
    
    </body>
    </html>
'''

'''
    11、刷新页面就会将后端处理好的逻辑数据直接展示在前段html中
'''







