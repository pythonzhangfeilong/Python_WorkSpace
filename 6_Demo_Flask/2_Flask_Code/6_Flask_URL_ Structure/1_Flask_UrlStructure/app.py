from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest'%guest

@app.route('/user/<name>')
def hello_user(name):
    # 如果名字是admin就会执行hello_admin函数
    if name=='admin':
        return redirect(url_for('hello_admin'))
    # 如果名字不是admin就会执行hello_guest函数，名且把该名字也传递进去
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == '__main__':
    app.run()

