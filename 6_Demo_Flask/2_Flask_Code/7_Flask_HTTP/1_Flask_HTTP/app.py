from flask import Flask
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
app = Flask(__name__)

@app.route('/success/<name>')
def func_success(name):
    return 'Hello %s!'%name

@app.route('/login',methods=['POST','GET'])
def func_login():
    if request.method=='POST':
        user=request.form['username']
        return redirect(url_for('success',name=user))
    else:
        user=request.form['username']
        return redirect(url_for('success',name=user))

if __name__ == '__main__':
    app.run()
