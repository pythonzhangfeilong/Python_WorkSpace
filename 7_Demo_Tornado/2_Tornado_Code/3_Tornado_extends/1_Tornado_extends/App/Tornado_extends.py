# 1、导入使用的模块
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# 2、定义端口配置
from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)

# 3、创建视图views
class sonHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Son.html')

# 4、创建路由
urls=[
    (r'/son',sonHandler),
]

# 5、#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls):
        super(MyApplication, self).__init__(
            debug=True,
            handlers=urls,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
        )

# 6、创建服务器
def make_app():
    tornado.options.parse_command_line()
    httpserver=tornado.httpserver.HTTPServer(MyApplication(urls))
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

# 7、运行服务器
if __name__ == '__main__':
    make_app()
