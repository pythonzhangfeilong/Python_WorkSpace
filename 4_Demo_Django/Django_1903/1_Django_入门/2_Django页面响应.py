###### 1、页面响应字符串Hello Word
'''
    1、首先在App文件夹下找到views.py文件，编写将要在页面响应的内容
        导入：from django.shortcuts import HttpResponse，页面响应字符串的模块
        编写响应函数:
            # 注意：第一个函数的参数默认的是request
            def index(request):
                return HttpResponse('Hello Word')
    2、编写好views.py中响应内容后，接下来就是在项目的文件夹中找到urls.py来编写url
        导入刚才在App文件夹中写好views
        from Apps import views
        编写url地址：
            from django.contrib import admin
            from django.urls import path
            from Apps import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                # 注意：这俩个index必须要与项目文件夹中views.py中响应函数的名称一样
                path('index/',views.index)
            ]
    3、启动Django项目后，在浏览器的地址中输入本机的地址和访问的端口，/加上相应的函数名称就会响应出想要的内容
'''

##### 2、页面响应json字符串
'''
    1、首先在App文件夹下找到views.py文件，编写将要在页面响应的内容
        导入：from django.http import JsonResponse，页面响应Json的模块
        编写响应函数：
            # 注意第一个函数的参数默认的是request
            def index(request):
                return JsonResponse({'Hello':'Word'})
    2、编写好views.py中响应内容后，接下来就是在项目的文件夹中找到urls.py来编写url
        导入刚才在App文件夹中写好views
        from Apps import views
        编写url地址：
            from django.contrib import admin
            from django.urls import path
            from Apps import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                # 注意：这俩个index必须要与项目文件夹中views.py中响应函数的名称一样
                path('index/',views.index)
            ]
    3、启动Django项目后，在浏览器的地址中输入本机的地址和访问的端口，/加上相应的函数名称就会响应出想要的内容
'''

##### 3、在页面响应一个HTML
'''
    1、首先在App文件夹下找到views.py文件，编写将要在页面响应的内容
        导入：from django.shortcuts import render，页面响应HTML的模块
        编写响应函数：
        # 注意第一个函数的参数默认的是request
        def index(request):
            return render(request,'index.html')
    2、编写好views.py中响应内容后，接下来就是在项目的文件夹中找到urls.py来编写url
        导入刚才在App文件夹中写好views
        from Apps import views
        编写url地址：
            from django.contrib import admin
            from django.urls import path
            from Apps import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                # 注意：这俩个index必须要与项目文件夹中views.py中响应函数的名称一样，包括与响应的HTML的名称也一致
                path('index/',views.index)
            ]
    3、启动Django项目后，在浏览器的地址中输入本机的地址和访问的端口，/加上相应的函数名称就会响应出想要的内容
'''

##### 4、拼接响应地址，并且给拼接的内容赋值（拼接赋值方式一）
'''
    1、首先在App文件夹下找到views.py文件，编写将要在页面响应的内容
        导入：from django.shortcuts import HttpResponse，页面响应字符串的模块
        编写响应函数:
            # 注意：第一个函数的参数默认的是request
            def page_index(request,data):
                return HttpResponse('Response de data is %s'%data)
    2、编写好views.py中响应内容后，接下来就是在项目的文件夹中找到urls.py来编写url
        导入刚才在App文件夹中写好views
        from Apps import views
        导入from django.conf.urls import url，进行地址的匹配
        编写url地址：
            from django.conf.urls import url
            from django.urls import re_path
            urlpatterns = [
                path('admin/', admin.site.urls),
                # 注意：这俩个index必须要与项目文件夹中views.py中响应函数的名称一样
                url(r'page_index/(\d+)',views.page_index),
            ]
    3、启动Django项目后，在浏览器的地址中输入本机的地址和访问的端口，/加上相应的函数名称就会响应出想要的内容
'''

##### 5、 拼接响应地址，并且给拼接的内容赋值（拼接赋值方式二）
'''
    1、首先在App文件夹下找到views.py文件，编写将要在页面响应的内容
        导入：from django.shortcuts import HttpResponse，页面响应字符串的模块
        编写响应函数:
            # 注意：第一个函数的参数默认的是request
            def page_index(request,test):
                return HttpResponse('Response de data is %s'%test)
    2、 编写好views.py中响应内容后，接下来就是在项目的文件夹中找到urls.py来编写url
        导入刚才在App文件夹中写好views
        from Apps import views
        导入from django.conf.urls import url，进行地址的匹配
        编写url地址：
            from django.conf.urls import url
            from django.urls import re_path
            urlpatterns = [
                path('admin/', admin.site.urls),
                # 注意：这俩个index必须要与项目文件夹中views.py中响应函数的名称一样
                url(r'page_index/(?P<test>.*)',views.page_index),
            ]            
    3、启动Django项目后，在浏览器的地址中输入本机的地址和访问的端口，/加上相应的函数名称就会响应出想要的内容                          
'''


















































