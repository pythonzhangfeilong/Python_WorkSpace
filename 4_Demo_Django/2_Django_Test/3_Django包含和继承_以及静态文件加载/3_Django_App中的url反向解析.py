##### 在HTML中通过a标签中的href引用，可以直接跳转的其他网站
'''
    以下实例展示
'''
'''
    render和render_to_response的区别
        render返回是需要request
        render_to_response返回是不需要request的

    1、首先在App的文件夹中找到views.py文件，写入：
        def dsapp_url(request):
            return render(request,'index.html')
    2、在项目的根目录urls.py文件中写入：
        urlpatterns = [
            path('index/', views.dsapp_url)
        ]
    3、在tenplates创建一个index.html文件并且写入：
        <a href="/z_article/DsApp_url/">点击一下就会跳转App中views.py文件中的dsapp_views函数结果</a>  
'''

#####url的反向解析
'''
    在生产环境下往往会使用url的反向解析
    
    1、在项目的根目录下找到urls.py文件写入：
        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import include
        from DsApp import views
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            # 注意namespace要写在include的括号里面，作为include的参数，参数值最好用path后面的第一个参数
            path('z_article/',include('DsApp.url',namespace='z_article')),
            path('index/', views.dsapp_url)
        ]

    2、在App的url.py文件中urlpatterns上写app_name='DsApp'
    
    3、在App的url.py文件中配置name,写入：
        from django.urls import path
        # 导入App中的view，不是根目录下的
        from DsApp import views
        app_name='DsApp'
        urlpatterns=[
            # DsApp_url就是一个url地址访问的拼接参数
            path('DsApp_url/',views.dsapp_views),
            path('url/',views.dsapp_views,name='app_url')
        ]
    4、在templates文件夹中的index.html写入：        
        <a href="{% url 'z_article:app_url' %}">点击一下就会跳转App中views.py文件中的dsapp_views函数结果</a>
        
        参数解释：
            z_article是项目根目录中urls.py文件path('z_article/',include('DsApp.url',namespace='z_article')),中的namespace
            app_url是App文件夹中url.py文件path('url/',views.dsapp_views,name='app_url')中的name
'''





























