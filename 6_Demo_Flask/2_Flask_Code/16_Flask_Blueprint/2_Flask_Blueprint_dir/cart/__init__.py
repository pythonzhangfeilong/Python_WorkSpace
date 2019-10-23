from flask import Blueprint

# 创建了一个蓝图对象
app_cart=Blueprint('app_cart',__name__)

# 在__init__文件执行的时候，把试图加载进来，让蓝图与应用程序知道视图的存在(可有可无)
from .views import get_cart


































