from flask import Flask
from orders import app_orders
app = Flask(__name__)

# 注册蓝图
app.register_blueprint(app_orders)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
