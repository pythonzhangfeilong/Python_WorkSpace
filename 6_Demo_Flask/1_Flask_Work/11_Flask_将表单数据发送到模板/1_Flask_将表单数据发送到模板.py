#####Flask将表单数据发送到模板
'''
    在URL规则中指定http方法。触发函数接收的Form数据可以以字典对象的形式收集它并将其转发到模板以在相应的网页上呈现它。
'''

# 实例：
'''
在以下示例中，'/' URL会呈现具有表单的网页（student.html）。填入的数据会发布到触发 result()函数的'/result' URL。
results()函数收集字典对象中的request.form中存在的表单数据，并将其发送给result.html。
'''
# 1、在templates文件夹中创建一个student.html写入:
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>student</title>
</head>
<body>
     <form action = "/result" method = "POST">
     <p>Name <input type = "text" name = "Name" /></p>
     <p>Physics <input type = "text" name = "Physics" /></p>
     <p>Chemistry <input type = "text" name = "chemistry" /></p>
     <p>Maths <input type ="text" name = "Mathematics" /></p>
     <p><input type = "submit" value = "submit" /></p>
  </form>
</body>
</html>
'''

# 2、在templates文件夹中创建result.html文件写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <table style="border: solid 1px red">
        {% for key,value in result.items() %}
            <tr>
                <td>key</td>
                <td>value</td>
            </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

# 3、在app.py中写入：
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

# 4、启动Flask服务：在浏览器中访问http://127.0.0.1:5000/