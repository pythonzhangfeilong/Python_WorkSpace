from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/index',methods=['POST','GET'])
def func_index():
    text=''
    if request.method=='POST':
        text=request.form.get('text')
    return render_template('index.html',text=text)

if __name__ == '__main__':
    app.run()
