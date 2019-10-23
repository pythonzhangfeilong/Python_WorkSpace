# 1、什么是Tornado:
'''
    Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，由FriendFeed公司在自己
        的网站FriendFeed中使用，被Facebook收购以后框架在2009年9月以开源软件形式开放给大众。
'''

# 2、Tornado的优点：
'''
    轻量级Web框架
    异步非阻塞IO处理方式
    出色的抗负载能力
    优异的处理性能，不依赖多进程/多线程，一定程度上解决C10K问题
    WSGI全栈替代产品，推荐同时使用其web框架和HTTP服务器
'''

# 3、Tornado对Django：
'''
    Django：
        Django是走大而全的方向，注重的是高效开发，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简
    单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。
        Django提供的方便，也意味着Django内置的ORM跟框架内的其他模块耦合程度高，应用程序必须使用Django内置
    的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利。

    重量级web框架，功能大而全，注重高效开发 
    内置管理后台 
    内置封装完善的ORM操作 
    session功能 
    后台管理 
    缺陷：高耦合
    
    Tornado：Tornado走的是少而精的方向，注重的是性能优越，它最出名的是异步非阻塞的设计方式。
    轻量级web框架，功能少而精，注重性能优越 
    HTTP服务器 
    异步编程 
    WebSocket 
    缺陷：入门门槛较高
'''

# 4、Tornado的安装
'''
pip install Tornado
'''

# 5、在页面响应Hello Word
import tornado.ioloop       # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
import tornado.web          # tornado的基础web框架
import tornado.httpserver   # httpserver监听端口
import tornado.options
from tornado.options import define, options

#定义端口配置
define('port', type=int, default=8080)

#创建视图
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>hello，world</h1>")

#创建路由
urls = [(r"/", MainHandler),]

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

'''
注意：启动服务器的时候直接是执行这个py文件即可
'''

# 6、Tornado中的关键代码解析
'''
tornado.web：tornado的基础web框架
    RequestHandler：封装对请求处理的所有信息和处理方法
    get/post/：封装对应的请求方式
    write()：封装响应信息，写响应信息的一个方法

tornado.ioloop：核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
    current()：返回当前线程的IOLoop实例对象
    start()：启动IOLoop实力对象的IO循环，开启监听
'''

# 7、Tornado特点
'''
作为Web框架，是一个轻量级的Web框架，类似于另一个Python web框架Web.py，其拥有异步非阻塞IO的处理方式。
作为Web服务器，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和其它Python web应用框
    架进行对比，结果最大浏览量超过第二名近40%。
'''

# 8、性能：
'''
Tornado有着优异的性能。它试图解决C10k问题，即处理大于或等于一万的并发
Tornado框架和服务器一起组成一个WSGI的全栈替代品。单独在WSGI容器中使用tornado网络框架或者tornaod http服务
    器，有一定的局限性，为了最大化的利用tornado的性能，推荐同时使用tornaod的网络框架和HTTP服务器
'''













