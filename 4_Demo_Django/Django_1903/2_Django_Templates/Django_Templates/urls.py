"""Django_Templates URL Configuration

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
urlpatterns = [
    path('admin/', admin.site.urls),
    # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
    # path('index/',views.index)                  # 模板系统加载的url
    # path('index/',views.get_page)               # 给前端传递参数的url
    # path('for/',views.news)                     # 给前端传递参数的url
    # path('forloop/',views.forloop)              # 给前端传递参数的url
    path('modification/',views.navigation)      # 给前端传递url
]
