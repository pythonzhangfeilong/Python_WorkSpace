#####Tornado静态文件
'''
Tornado中的静态文件加载，直接在创建应用中添加static_path，然后App文件夹下就可以创建一个static的文件夹
class MyApplication(tornado.web.Application):
    def __init__(self, urls):
        super(MyApplication, self).__init__(
            debug=True,
            handlers=urls,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
'''

# 1、导入使用的模块
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# 2、定义端口配置
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# 3、创建视图views
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class MungedPageHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped: mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines,
                choice=random.choice)

# 4、创建路由
urls=[
    (r'/index',IndexHandler),
    (r'/munged',MungedPageHandler)
]

# 5、#创建配置-开启调试模式
configs=dict(debug=True)

# 6、#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls):
        super(MyApplication, self).__init__(
            debug=True,
            handlers=urls,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

# 7、创建服务器
def make_app():
    tornado.options.parse_command_line()
    httpserver=tornado.httpserver.HTTPServer(MyApplication(urls))
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

# 8、运行服务器
if __name__ == '__main__':
    make_app()
