from django.urls import path
# 导入App中的view，不是根目录下的
from DsApp import views
app_name='DsApp'
urlpatterns=[
    # DsApp_url就是一个url地址访问的拼接参数
    path('DsApp_url/',views.dsapp_views),
    path('url/',views.dsapp_views,name='app_url')

]

