# 导入path在配置路由的时候使用
from django.urls import path
# 导入App中views，编写路由
from App import views
urlpatterns = [
    # 响应函数的路由
    path('App_url/',views.func_http)
]