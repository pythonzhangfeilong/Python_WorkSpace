from flask import Flask
from flask import render_template
app = Flask(__name__)

# Flask平铺传递变量
@app.route('/flask_index')
def func_flask():
    return render_template('index.html',name='zhang',age=20)

# 像Django中自定的形式传递变量
@app.route('/django_index')
def func_django():
    data={
        'name': 'zhang',
        'age': 18,
        'my_dict': {'city':'huhehaote'},
        'my_list': [1,2,3,4,5,6],
        'my_int': 0,
    }
    return render_template('index.html',**data)
if __name__ == '__main__':
    app.run()
