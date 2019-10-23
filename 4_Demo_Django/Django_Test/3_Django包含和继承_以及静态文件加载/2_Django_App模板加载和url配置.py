#####Django_App中的模板文件加载
'''
    模板文件加载步骤：
        1、生成App文件
        2、在settins.py文件的INSTALL_APP中添加App的名字（方便mro模板映射，但是采用Django项目创建时创建App不用）
        3、在总路由（也就是项目的文件夹下）urls.py文件中配置url，让程序能够通过url找到这个App
        4、配置App中的views.py只向已生成的HTML模板
'''

#####Django_App中的模板文件加载实际操作步骤
'''
    1、生成App文件（在pycharm创建Django项目时创建）
'''

'''
    2、在settins.py文件的INSTALL_APP中添加App的名字（在pycharm创建Django项目时创建后自动加入）
'''

'''
    3、在App文件夹下自己新建一个url.py文件
'''

'''
     4、在总路由urls.py（也就是项目根目录的文件夹下）文件中配置url，让程序能够通过url找到这个App
        在urls.py文件中写入：
            from django.conf.urls import include
            
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('z_article/',include('DsApp.url'))
            ]
            
            path('z_article/',include('DsApp.url'))各参数解释：
                z_article是一会儿访问时链接地址后面的第一个参数
                include()是导入include模块的固定方法
                DsApp.url是App的名字点上了App中url.py文件
'''

'''
    5、在App文件夹中views.py的文件，写入
        from django.shortcuts import HttpResponse
        def dsapp_views(request):
            return HttpResponse('兄弟，你好呀')
'''

'''
    6、配置App的url.py，写入：
        from django.urls import path
        # 导入App中的view，不是根目录下的
        from DsApp import views
        urlpatterns=[
        # 这样就可以通过urls.py文件中include前面的那个参数去访问多个App的path中第一个参数
            path('DsApp_url/',views.dsapp_views)
        ]
'''

'''
    7、拼接浏览器的地址栏进行访问App文件中编写的页面响应函数dsapp
        浏览器地址：http://127.0.0.1:8000/z_article/DsApp_url/
        
        浏览器地址的参数解释：
            z_article是来自于项目根目录urls中的path('z_article/',include('DsApp.url'))后的第一个参数
            DsApp_url是来自于App文件夹url中的path('DsApp_url/',views.dsapp_views)后的第一个参数
'''










































