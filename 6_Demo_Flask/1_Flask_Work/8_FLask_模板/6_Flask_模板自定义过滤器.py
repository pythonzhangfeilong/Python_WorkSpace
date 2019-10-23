'''
1、在app.py中写入：
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')
def func_index():
    data={
        'my_list':[0,1,2,3,4,5,6]
    }
    return render_template('index.html',**data)

# 自定义过滤器
def func_buchang(data):
    return data[::2]
# 注册过滤器(第一个参数是过滤器的函数，第二个参数是过滤器的名字)
app.add_template_filter(func_buchang,'buchang')

if __name__ == '__main__':
    app.run()
'''

'''
2、templates文件夹中创建index.html文件，写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    my_list:{{ my_list | buchang }}
</body>
</html>
'''

'''
3、启动Flask服务，在浏览器中访问http://127.0.0.1:5000/index
'''