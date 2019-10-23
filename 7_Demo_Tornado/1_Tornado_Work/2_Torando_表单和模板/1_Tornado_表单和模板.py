#####表单和模板
'''
1、导入固定使用的模块
2、定义端口和提示信息
3、创建视图views，固定继承tornado.web.RequestHandler，在这里在页面展示的是后不再是使用return去使用，而是经典
    的类方法self.render('模板')，传参的时候，先写模板，然后直接就是 变量=传递的值
4、创建路由列表，首先urls是一个列表，列表中的url是一个元组的形式，第一个参数是url，第二个参数是视图views
5、在出现错误的时候为了在页面直观的显示，就采用configs=dict(debug=True)
6、自定义应用是固定的写法
7、创建服务器是固定写法
8、启动服务也是固定
'''
# 1、导入使用的模块
import tornado
import os.path
from tornado import httpserver  # httpserver监听端口
from tornado import ioloop  # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
from tornado import options
from tornado import web  # tornado的基础web框架

# 2、定义端口配置
from tornado.options import define,options
# port是端口，default是设置的端口，help是提示信息运行指定的端口，type是类型
define('port',default=8086,help='run on the given port',type=int)

# 3、创建视图views,固定继承tornado.web.RequestHandler
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        self.render('poem.html', username=username, password=password, email=email,phone=phone)

# 4、创建路由
urls=[
    (r'/index',IndexHandler),
    (r'/poem',PoemPageHandler)
]

# 5、#创建配置-开启调试模式
configs=dict(debug=True)

# 6、#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls,config):
        super(MyApplication, self).__init__(
            handlers=urls,
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )

# 7、创建服务器
def make_app():
    tornado.options.parse_command_line()
    httpserver=tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

# 8、运行服务器
if __name__ == '__main__':
    make_app()































