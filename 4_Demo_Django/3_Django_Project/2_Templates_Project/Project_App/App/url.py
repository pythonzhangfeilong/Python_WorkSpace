"""
@File    : url.py
@Time    : 2020/5/29 11:41 上午
@Author  : FeiLong
@Software: PyCharm
"""

app_name='App'
from django.urls import path
# 导入App中的view，不是根目录下的
from App import views
urlpatterns=[
# 这样就可以通过urls.py文件中include前面的那个参数去访问多个App的path中第一个参数
    path('html_index/',views.App_views),
    path('framework/',views.framework_page),
    path('extends/',views.extends),
    path('news/',views.ststic)
]