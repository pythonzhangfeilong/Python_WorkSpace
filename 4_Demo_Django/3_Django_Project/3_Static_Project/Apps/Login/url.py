"""
@File    : url.py
@Time    : 2020/5/29 3:36 下午
@Author  : FeiLong
@Software: PyCharm
"""
from Login import views
from django.urls import path

app_name='Login'

urlpatterns = [
    path('login/',views.login),

]