"""6_Django_static URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from DsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('z_article/',include('DsApp.url',namespace='z_article')),
    path('index/', views.dsapp_url)
]
'''
    path('z_article/',include('DsApp.url'))各参数解释：
        z_article是一会儿访问时链接地址后面的第一个参数
        include()是导入include模块的固定方法
        DsApp.url是App的名字点上了App中url.py文件
'''

