# 1、使用蓝图之前是需要pip install flask_blueprint
from flask import Blueprint
# 2、创建蓝图对象,Blueprin后面的第一个参数是蓝图对象的名字
app_orders = Blueprint('app_orders', __name__)

# 3、在程序实例中注册该蓝图
'''
在main.py文件中导入编写的蓝图模块   from orders import app_orders
在main.py文件中注册蓝图app.register_blueprint(app_orders)
'''

# 4、编写蓝图路由
@app_orders.route("/get_order")
def get_orders():
    return 'Hello Word'
