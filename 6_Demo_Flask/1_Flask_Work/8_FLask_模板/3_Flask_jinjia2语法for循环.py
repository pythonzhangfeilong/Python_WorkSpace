# 1、在template文件夹中创建result.html写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <table border = 1>
         {#python3中是items()#}
         {% for key, value in result.items() %}
        <tr>
            <td>key</td>
            <td>value</td>
        </tr>
     {% endfor %}
    </table>
</body>
</html>
'''

# 2、在app.py文件中写入：
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run()

'''
在浏览器中访问：http://127.0.0.1:5000/result
'''