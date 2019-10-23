"""Django_url_反向解析 URL Configuration

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
# 导入include方便关联App中url.py
from django.conf.urls import include
# 导入App中的视图
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 首先访问的页面
    path('index/',views.func_html),
    # 关联App中的url.py，并且设置反向代理时的名字
    path('include_index/',include('App.url',namespace='app')),

]
