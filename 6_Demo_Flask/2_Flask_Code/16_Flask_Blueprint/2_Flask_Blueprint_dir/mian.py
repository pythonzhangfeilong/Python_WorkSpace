from flask import Flask
from cart import app_cart
app = Flask(__name__)

# 注册蓝图
'''
只要给main.py中注册蓝图函数时加上url_prefix,那么以后蓝图创建函数访问时都得加上url_prefix='/orders'前缀
'''
app.register_blueprint(app_cart,url_prefix='/cart')

if __name__ == '__main__':
    app.run()
