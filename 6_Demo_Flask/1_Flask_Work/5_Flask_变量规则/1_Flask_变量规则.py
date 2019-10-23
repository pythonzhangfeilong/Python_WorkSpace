#####Flask_变量规则
'''
    通过向规则参数添加变量部分，可以动态构建url，此变量部分标记为<variable-name>它作为关键字参数传递给与规则相关联的函数。
'''
# 1、把字符串作为变量参数包含在url中，并且在页面响应
from flask import Flask
app = Flask(__name__)

@app.route('/str/<name>')
def func_str(name):
    return 'str is %s!'%name

if __name__ == '__main__':
    app.run()
'''
启动flask服务，在浏览器中访问http://127.0.0.1:5000/func/zhang那么页面就会响应Hello zhang!

当在浏览器地址的最后输入了zhang，那么zhang就作为了一个参数传递给了name，执行下去就会return返回这个Hello zhang！
'''

# 2、除了默认字符串变量部分之外，还可以使用以下转换器构建规则：
'''
① int       接受整数
② float     对于浮点值
③ path      接受用作目录分隔符的斜杠
'''
from flask import Flask
app = Flask(__name__)

# url地址接受的字符串
@app.route('/str/<name>')
def func_str(name):
    return 'str is %s!'%name

# url地址接受的整数
@app.route('/int/<int:postID>')
def func_int(postID):
    return 'int Number %d'%postID

# url地址接受的小数
@app.route('/float/<float:xiaoshu>')
def func_float(xiaoshu):
    return 'float Number %d'%xiaoshu

if __name__ == '__main__':
    app.run()



