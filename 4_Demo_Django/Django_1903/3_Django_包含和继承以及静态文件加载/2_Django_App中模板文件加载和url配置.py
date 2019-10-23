#####Django中App模板文件的加载
'''
    采用命令的方式创建Django项目的App时是需要的settings.py文件的INSTALLED_APP=[]的最后添加App文件，而pycharm在
        Applocaltion name添加App是不要在settings.py文件的INSTALLED_APP=[]的最后添加App文件的，所以采用pycahrm创建
'''
# 1、在App文件夹中新建一个url.py

# 2、配置总路由，也就是项目文件夹中的urls.py文件，写入：
'''
    from django.conf.urls import include
    urlpatterns = [
        path('z_urls_App/',include('App.url'))
    ]
    参数解释：z_urls_App/就是在地址栏访问App中的内容的第一个参数
             App.url也就是App的名字点上创建的url，是为了让Django能够找到App
        
'''

# 3、在App的文件夹中找到views.py文件，写入：
'''
    from django.shortcuts import HttpResponse
    def func_App(request):
        return HttpResponse('兄弟，你好呀！')
'''

# 4、在App的url中配置路由
'''
    from django.urls import path
    from App import views
    urlpatterns = [
        path('App_url/',views.func_App)
    ]
'''

# 5、在pycharm启动Django项目，打开浏览器在地址栏中输入：http://127.0.0.1:8000/z_urls_App/App_url/
'''
    访问地址：http://127.0.0.1:8000/z_urls_App/App_url/
    参数解释：
        z_urls_App是项目的总路由urls.py文件中path后面的第一个参数
        App_url是App文件夹url.py文件中path后面的第一个参数
'''














