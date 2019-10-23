#####路由生成器
'''
1、首先导入：
from tornado.web import url,URLSpec

2、设置路由名称
urls = [
    # \d+是正则表达式，表示的是0-9
    url(r'/course/(\d+)',CourseHandler,name='course'),
]

3、创建视图views
class CourseHandler(tornado.web.RequestHandler):
    def get(self,cid ):
        self.write('<h1>Hello Word ID：%d</h1>'%(int(cid)))

注意：在这个视图函数中加入cid参数，可以取到地址中除了固定地址外的其他参数

4、创建路由
urls = [
    # d+是正则表达式，表示的是0-9
    url(r'/course/(d+)',CourseHandler,name='course'),
]

5、启动Tornado服务，访问下面的地址
http://127.0.0.1:8085/course/123
'''

# Tornado代码
import tornado.ioloop       # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
import tornado.web          # tornado的基础web框架
import tornado.httpserver   # httpserver监听端口
import tornado.options
from tornado.options import define, options
from tornado.web import url,URLSpec
#定义端口配置
define('port', type=int, default=8085)

#创建视图views
class CourseHandler(tornado.web.RequestHandler):
    def get(self,cid ):
        # 注意cid就是访问当前页面时最后加的数字
        self.write('<h1>Hello Word ID：%d</h1>'%(int(cid)))
        self.write(self.reverse_url('course',cid))

#创建路由表
urls = [
    # \d+是正则表达式，表示的是0-9
    url(r'/course/(\d+)',CourseHandler,name='course'),
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