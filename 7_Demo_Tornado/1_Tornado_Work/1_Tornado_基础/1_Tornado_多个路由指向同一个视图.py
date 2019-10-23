#####多个路由，指向同一个views，也就是视图views
"""
1、创建视图处理器
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello Word</h1>")


2、在下面的代码中找到 创建路由表 ,写入：
    urls = [
        (r"/", MainHandler)，
        (r"/index", MainHandler)
    ]

3、参数解释：
    urls是创建url的固定写法，后面的跟的是一个列表
    列表里括号中的第一个参数  r"/"  是访问时ip地址后面的第一个参数
    列表里括号中的第二个参数  MainHandler  就是视图views

4、启动Tornado服务：访问下面的俩个地址，响应的是同一个视图views
    127.0.0.1:8080
    127.0.0.1:8080/index
"""

# Tornado代码
import tornado.ioloop       # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
import tornado.web          # tornado的基础web框架
import tornado.httpserver   # httpserver监听端口
import tornado.options
from tornado.options import define, options

#定义端口配置
define('port', type=int, default=8089)

#创建视图
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>hello，world</h1>")

#创建路由表
urls = [
    (r"/", MainHandler),
    (r'/index',MainHandler)
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













