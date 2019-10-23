##### 蓝图里模板目录和静态文件的处理
'''
1、在项目的最外层目录下创建一个子项目文件夹cart，在里面创建static文件、templates文件，__init__.py文件，views.py文件
__init__.py文件中写入：
    from flask import Blueprint
    # 创建了一个蓝图对象
    app_cart=Blueprint('app_cart',__name__,template_folder='templates',static_folder='static')
    # 在__init__文件执行的时候，把试图加载进来，让蓝图与应用程序知道视图的存在(可有可无)
    from .views import get_cart

views.py文件中写入：
    # 导入响应模板方法
    from flask import render_template
    # 导入__init__文件中的蓝图对象
    from cart import app_cart
    #创建试图路由
    @app_cart.route('/get_cart')
    def get_cart():
        return render_template('cart.html')

templates文件夹中创建cart.html，写入：
    <h1>cart page</h1>
'''


'''
2、main.py文件中写入(main.py其实就是app.py改名的)：
from flask import Flask
from cart import app_cart
app = Flask(__name__)

# 注册蓝图
只要给main.py中注册蓝图函数时加上url_prefix,那么以后蓝图创建函数访问时都得加上url_prefix='/orders'前缀

app.register_blueprint(app_cart,url_prefix='/cart')

if __name__ == '__main__':
    app.run(debug=True)
'''

