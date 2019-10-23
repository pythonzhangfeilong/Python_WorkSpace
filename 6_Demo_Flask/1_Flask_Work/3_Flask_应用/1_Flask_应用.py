#####1、创建一个Flask项目找到app.py：
# 在项目中导入Flask模块
from flask import Flask
# Flask构造函数使用当前模块（__name __）的名称作为参数
app=Flask(__name__)

# Flask类的route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数，'/ ' URL与func_test_flask()函数绑定。因此，当在浏览器中打开web服务器的主页时，将呈现该函数的输出
'''
参数解释：route(rule, options)
rule 参数表示与该函数的URL绑定
options 是要转发给基础Rule对象的参数列表
'''
@app.route('/')
def func_test_flask():
    return 'Hello Word'

if __name__ == '__main__':
# Flask类的run()方法在本地开发服务器上运行应用程序
    app.run()
# app.run(host, port, debug, options)中包含的参数,参数解释：
'''
    1、host要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
    2、port默认值为5000
    3、debug默认为false。 如果设置为true，则提供调试信息
    4、options要转发到底层的Werkzeug服务器。
'''
##### 启动Flask服务
'''
    1、切换到1_Flask_应用.py文件所在的位置，打开cmd窗口，输入python 1_Flask_应用.py回车，下面这样就成功启动了Flask服务:
    D:\Program Files\PyCharm 2018.1.4\workspace\Demo_Flask\Flask_Work\3_Flask_应用>python 1_Flask_应用.py
     * Serving Flask app "1_Flask_应用" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    
    2、在浏览器地址栏中输入http://127.0.0.1:5000/，就会看到Hello Word
'''
