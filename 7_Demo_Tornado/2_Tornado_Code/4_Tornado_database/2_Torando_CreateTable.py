# 1、导入应用模块
import os.path                      # 导入os模块，生命路径文件夹的时候使用，例如：static、templates
import tornado                      # 导入tornado模块
from tornado import httpserver      # httpserver监听端口
from tornado import ioloop          # 核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
from tornado import options
from tornado import web             # tornado的基础web框架
import pymysql                      # 导入数据库操作模块
from tornado.options import define,options  # 导入define设置连接端口使用
# 2、设置连接和端口
define('port',default=8001,type=int,help='请连接指定端口')

# 3、创建数据库链接对象
db=pymysql.Connection(host='127.0.0.1',database='tornado_database',user='root',password='',charset='utf8')

# 4、编写views
class HouseHandler(tornado.web.RequestHandler):
    # 创建数据库对象不能够直接是连接对象，要使用self方法实现
    def create_db(self, db):
        self.db = db
    try:
        cursor = db.cursor()
        cursor.execute("create table userinfo(id int primary key auto_increment,username varchar(30),password varchar(30))")
    except Exception as e:
        print('出现错误%s'%e)
    print('创建数据库成功%s'% ('success'))

# 5、自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self):
        settings=dict(
            debug=True,
            db=db
        )
        tornado.web.Application.__init__(self,**settings)

# 6、创建服务器
def make_app():
    tornado.options.parse_command_line()
    httpserver = tornado.httpserver.HTTPServer(MyApplication())
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
# 7、启动服务
    make_app()

































