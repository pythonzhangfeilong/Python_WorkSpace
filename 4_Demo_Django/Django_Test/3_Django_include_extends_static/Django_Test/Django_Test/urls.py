"""Django_Test URL Configuration

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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # App的url配置使用
    path('AppProject_url/', include('App.url')),
    # 在HTML中通过a标签中的href引用，可以直接跳转的其他网站
    path('a_href/',views.func_href),
    # url的反向解析
    path('AppProject_url/', include('App.url',namespace='AppProject_url')),
    # 继承使用
    path('extends/',views.func_exteds)
]
