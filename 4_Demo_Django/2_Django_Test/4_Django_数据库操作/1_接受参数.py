'''
1、创建index.html写入：
    <body>
        <h1>用户输入</h1>
        <form action="/index/" method="post">
            用户名:<input type="text" name="username"/>
            密码:<input type="password" name="password"/>
            <button type="submit">提交</button>
        </form>
    </body>
'''

'''
2、在views.py中写入：
    from django.shortcuts import render
    def func_index(request):
        return render(request,'index.html')
'''

'''
3、在urls.py中写入
    from Data_App import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/',views.func_index)
    ]
'''

'''
4、启动Django服务，在浏览器中输入地址：http://127.0.0.1:8000/index/就会查看到html中的内容
先不要在这里向html中添加数据
'''

'''
5、再次在views.py文件中完善刚才写入的内容
from django.shortcuts import render

def func_index(request):
    # 注意POST必须是大写
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
    return render(request,'index.html')
'''

'''
6、刷新页面之后随便添加点内容点击提交，会出现如下报错：
    Forbidden (403)
    CSRF verification failed. Request aborted.
上面的报错是因为Django中有一个跨站请求保护的机制，在index中form标签的最上面添加上一句{% csrf_token %}即可
'''







