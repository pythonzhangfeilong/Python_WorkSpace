#####Django_App中url地址的反向解析

# 1、正常的HTML中a标签href的操作
'''
    1、在App的文件夹中的views.py中，写入：
        def func_html_a(request):
            return render(request,'html_a.html')
    2、在项目的templates文件夹中创建html_a.html,并且写入：
        <a href="/z_urls_App/App_url">点击以下就会执行views.py中的func_App函数</a>
    3、在项目的根目录文件夹中找到urls.py写入：
        from App import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('z_urls_App/',include('App.url')),
                path('func_html/',views.func_html_a)
            ]
    4、在浏览器的地址栏中输入：
        http://127.0.0.1:8000/func_html/
    # 其实逻辑就是，通过浏览器访问urls.py文件中配置path('func_html/',views.func_html_a)里面的func_html函数，访问到htlm
        文件，在浏览器显示的信息点击，就会自动拼接<a href="/z_urls_App/App_url">点击以下就会执行views.py中的func_App函数</a>
        里面的/z_urls_App/App_url，而App_url中的执行函数是func_App函数，所以就会显示出views.py中func_App函数的结果
'''

# 2、生产环境中url的反向解析
'''
    1、首先在上面编写代码的中的总路由也就是urls.py文件，include后面添加一个参数namespace
        from django.conf.urls import include
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('z_urls_App/',include('App.url',namespace='z_urls_App')),
            path('func_html/',views.func_html_a)
        ]
        
        path('z_urls_App/',include('App.url',namespace='z_urls_App'))中的参数解释及注意事项：
            namespace='z_urls_App'后面的参数值一定要是path后面的第一个参数
            namespace一定要写在include的括号里面，作为第二个参数，也就是一会儿HTML中冒号前的参数
    2、在App文件夹中的url.py文件中，写入：
        from App import views
        from django.urls import path
        app_name='App'
        urlpatterns = [
            path('App_url/',views.func_App,name='App_url_fanxiangjiexi')
        ]
        
        参数解释及注意事项：
            一定要在urlpatterns的上面一行中添加app_name=自己App的名字
            path中的那么也就是一会反向解析时HTML中冒号后面的参数
    3、在templates文件夹中href_a的html文件中写入：
        <a href="{% url 'z_urls_App:App_url_fanxiangjiexi' %}">点击一下就会执行views.py中的func_App函数</a>
    
    其实逻辑就是,通过浏览器访问urls.py文件中配置path('func_html/',views.func_html_a)里面的func_html函数，访问到htlm
        文件，在浏览器显示的信息点击,就会自动拼接 <a href="{% url 'z_urls_App:App_url_fanxiangjiexi' %}">点击一下就会执行views.py中的func_App函数</a>
        里面的z_urls_App:App_url_fanxiangjiexi，而App_url_fanxiangjiexi是重新给App_url创建的名字,所以执行函数是func_App函数，
        所以就会显示出views.py中func_App函数的结果
'''




























