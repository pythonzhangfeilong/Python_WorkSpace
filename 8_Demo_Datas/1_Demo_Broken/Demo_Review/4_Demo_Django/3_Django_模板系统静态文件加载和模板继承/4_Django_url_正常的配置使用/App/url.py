from django.urls import path
from App import views
urlpatterns = [
    # 页面响应字符串视图函数的路由
    path('App_url/',views.func)
]