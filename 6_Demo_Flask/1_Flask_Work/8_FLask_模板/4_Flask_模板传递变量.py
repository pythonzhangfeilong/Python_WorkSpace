#####Flask中后端变量传递到前端
'''
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
    # 如果想要按照Django中以字典的形式传递变量，那么在传递的时候就是**字典变量，因为**是会解包字典对象,变成key=value的形式
    return render_template('index.html',**data)
if __name__ == '__main__':
    app.run()
'''

'''
2、在templates文件夹中创建index.html，写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    {#传递变量#}
    <p>name={{ name }}</p>
    <p>age={{ age }}</p>
    {#字典传变量取值的俩种方式#}
    <p>my_dict:city={{ my_dict['city'] }}把key当成索引取value</p>
    <p>my_dict:city={{ my_dict.city}}直接点上key取value</p>
    {#列表传变量取值的三种方式#}
    <p>my_list:list={{ my_list }}直接将列表全部传过来</p>
    <p>my_list:list={{ my_list[2] }}给定索引值</p>
    <p>my_list:list={{ my_list[my_int] }}把my_int作为了一个索引值</p>
    {#列表索引取值直接运算#}
    <p>my_list[2]+my_list[3]:list={{ my_list[2]+my_list[3] }}</p>
    <p>my_list[2]-my_list[3]:list={{ my_list[2]-my_list[3] }}</p>
    <p>my_list[2]*my_list[3]:list={{ my_list[2]*my_list[3] }}</p>
    <p>my_list[2]/my_list[3]:list={{ my_list[2]/my_list[3] }}</p>
    {#直接俩个字符串变量的相加#}
    <p>{{ 'hello'+' python' }}</p>
    {#如果是变量相加，前提是他们的类型得保持一致#}
    <p>{{ age+my_int }}</p>

    {#过滤器 | ,过滤器是可以多级存在的，可以一直加过滤器条件#}
    *{{ '     python work      ' |upper|trim }}*
</body>
</html>
'''

'''
3、启动Flask服务，在浏览器中访问：http://127.0.0.1:5000/index，就会看到传递的变量
'''

















