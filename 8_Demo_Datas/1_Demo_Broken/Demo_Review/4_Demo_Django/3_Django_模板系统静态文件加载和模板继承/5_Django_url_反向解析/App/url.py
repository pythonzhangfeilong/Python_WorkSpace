from django.urls import path
from App import views
# app_name就是App文件夹的名字
app_name='App'
# 页面响应字符串
urlpatterns = [
    # name就是反向解析时用的名字
    path('func_str/',views.func_str,name='test')
]