"""Django_Hello URL Configuration

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
# 导入App中的视图文件
from App_Hello import views
# 配置url
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    # path后面的第一个参数也就是url127.0.0.1:8000后的第一个参数，也就是访问函数的名字，views.func_hello就是执行的函数
    path('hello/',views.func_hello),
    url(r'page/(\d+)',views.func_page)
]
