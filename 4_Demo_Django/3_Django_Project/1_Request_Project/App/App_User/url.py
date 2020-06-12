"""
@File    : url.py
@Time    : 2020/5/28 4:42 下午
@Author  : FeiLong
@Software: PyCharm
"""
from django.urls import path

from App_User import views

app_name='App_USer'

urlpatterns=[
    # DsApp_url就是一个url地址访问的拼接参数
    path('get_page/',views.get_page),
    path('url/',views.get_page,name='app_url')

]