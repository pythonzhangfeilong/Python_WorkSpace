import tornado.ioloop       # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
import tornado.web          # tornado的基础web框架
import tornado.httpserver   # httpserver监听端口
import tornado.options
from tornado.options import define, options

#定义端口配置
define('port', type=int, default=8081)

#创建视图
class Tornado_url_Chinese(tornado.web.RequestHandler):
    def get(self,name):
        self.write('<h1>Hello Word：%s</h1>'%(name))

#创建路由表
urls = [
    # . 是匹配除了换行符以外的其他内容，*是匹配前一个字符一次或者多次
    (r"/Chinese/(.*)", Tornado_url_Chinese),
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
