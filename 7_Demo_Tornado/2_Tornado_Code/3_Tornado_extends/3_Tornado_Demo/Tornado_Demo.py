# 1、导入使用的模块
import tornado
from tornado import web
from tornado import httpserver
from tornado import ioloop
from tornado import options
import os.path

# 2、设置默认端口
from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)

# 3、编写views时固定继承tornado.web.RequestHandler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Burt's Books | Home",
            header_text = "Welcome to Burt's Books!",
        )

# 自定义应用，固定继承tornado.web.Application
class MyApplication(tornado.web.Application):
    def __init__(self):
        # url
        handlers = [
            (r"/index", MainHandler),
        ]
        # 配置信息
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        # 初始化配置信息
        tornado.web.Application.__init__(self, handlers, **settings)

# 创建服务器
def make_app():
    tornado.options.parse_command_line()
    httpserver = tornado.httpserver.HTTPServer(MyApplication())
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
# 启动服务
    make_app()