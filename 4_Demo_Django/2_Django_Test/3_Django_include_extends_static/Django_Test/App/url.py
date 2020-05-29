from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from App import views
app_name='App'
urlpatterns = [
    path('admin/', admin.site.urls),
    # Appurl配置使用
    path('func_app/',views.func_AppProject_views),
    # url反向解析使用
    path('url_fanxiang/',views.func_AppProject_views,name='url_fanxiangjiexi')

]