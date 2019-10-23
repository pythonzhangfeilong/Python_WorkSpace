#####Torando继承：
'''
    Tornado通过extends和block语句支持模板继承，这就拥有了编写能够在合适的地方复用的流体模板的控制权和灵活性。

    为了在新模板中扩展一个父模板（在这里假设为main.html），可以这样使用：
        {% extends "main.html" %}
        这就使得新文件继承main.html的所有标签，并且覆写为期望的内容。
'''

#####在Torando_extends.py中写入：
# 1、导入使用的模块
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# 2、定义端口配置
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

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

#####在Dad.html中写入页面信息
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dad</title>
</head>
<body>
    <h1>我是爸爸</h1>
</body>
</html>
'''

#####在Son.html中写入要继承Dad.html逻辑
'''
<!DOCTYPE html>
# 注意：要继承模板写入继承模板的位置
{% extends "Dad.html" %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Son</title>
</head>
<body>

</body>
</html>
'''

#####启动Tornado服务，访问http://127.0.0.1:8001/son
# 这样Son.html就成功地继承到了Dad.html中的内容