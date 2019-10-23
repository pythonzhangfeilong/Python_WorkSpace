from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def func_student():
    return render_template('student.html')

@app.route('/result',methods=['POST',"GET"])
def func_result():
    if request.method=='POST':
        result=request.form
        return render_template('result.html',result=result)
if __name__ == '__main__':
    app.run()

