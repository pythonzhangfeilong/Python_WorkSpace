#####块
'''
其实就是在父亲的页面中写标签，标签里写入{%block header%}{%end%}站住位子，就像下面的这个例子：
    <header>
        {%block header%}
        {%end%}
    </header>
然后在在儿子的页面中，继承父亲的内容，{%extends 'Dad.html'%}，然后再需要的位置写入父亲刚才占位置写的内容，注意儿子不用写标签
    {%block header%}
            儿子
    {%end%}
'''

#####在Tornado_block.py中写入：
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

#####在父亲的Dad.html中写入
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dad</title>
</head>
<body>
    <h1>我是你爸爸</h1>
    <header>
        {%block header%}
        {%end%}
    </header>
</body>
</html>
'''

#####在儿子的Son.html中写入
'''
<!DOCTYPE html>
{%extends 'Dad.html'%}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Son</title>
</head>
<body>
    {%block header%}
            儿子
    {%end%}
</body>
</html>
'''

# 启动Torando服务访问http://127.0.0.1:8000/son
# 这样就不仅继承了父亲的页面，好把父亲给占位的地方添加上了儿子自己的内容