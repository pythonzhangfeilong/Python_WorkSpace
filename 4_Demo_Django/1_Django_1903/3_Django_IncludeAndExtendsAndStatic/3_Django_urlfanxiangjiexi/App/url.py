from App import views
from django.urls import path
app_name='App'
urlpatterns = [
    path('App_url/',views.func_App,name='App_url_fanxiangjiexi')
]