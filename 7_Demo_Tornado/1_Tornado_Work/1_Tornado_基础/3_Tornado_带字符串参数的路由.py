#####带字符串参数的路由
'''
1、创建视图views
class CourseHandler2(tornado.web.RequestHandler):
    def get(self,name ):
        self.write('<h1>Hello Word：%s</h1>'%(name))

注意：在这个视图函数中加入name参数，可以取到地址中除了固定地址外的其他参数

2、编写urls路由
urls = [
    (r"/course2/([a-zA-Z]+)", CourseHandler2),
]

3、启动Tornado服务，在地址栏中访问
http://127.0.0.1:8080/course2/qwertyui

注意：course2后面的这个参数是随意输入的
'''

import tornado.ioloop       # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
import tornado.web          # tornado的基础web框架
import tornado.httpserver   # httpserver监听端口
import tornado.options
from tornado.options import define, options

#定义端口配置
define('port', type=int, default=8080)

#创建视图
class CourseHandler2(tornado.web.RequestHandler):
    def get(self,name ):
        self.write('<h1>Hello Word：%s</h1>'%(name))

#创建路由表
urls = [
    (r"/course2/([a-zA-Z]+)", CourseHandler2),
]

#创建配置-开启调试模式
configs = dict(debug=True)

#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls, **configs)

#创建服务器
def make_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#启动服务器
if __name__ == '__main__':
    make_app()
