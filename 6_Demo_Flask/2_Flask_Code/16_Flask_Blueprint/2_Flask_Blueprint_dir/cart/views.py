# 导入__init__文件中的蓝图对象
from cart import app_cart
#创建试图路由
@app_cart.route('/get_cart')
def get_cart():
    return 'get_cart'























