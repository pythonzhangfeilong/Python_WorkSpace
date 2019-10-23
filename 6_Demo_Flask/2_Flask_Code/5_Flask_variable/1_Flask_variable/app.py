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
