"""Django_url_正常的配置使用 URL Configuration

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
from App import views
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用include()方法，把App中url关联到总路由urls.py中
    path('index/',include('App.url')),
    # 编写页面响应模板的视图函数
    path('index/',views.func_f),
]
