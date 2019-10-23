##### Flask文件上传：
'''
    Flask文件上传相对简单，它需要一个HTML表单，其enctype属性设置为“multipart / form-data”，将文件发布到url，url处理程序从
        request.files[]对象中提取文件，并将其保存到所需要的位置

    每个上传的文件首先会保存在服务器上的临时位置，然后将其实际保存到它的最终位置。目标文件的名称可以是硬编码的，也可以从
        request.files[file]对象的filename属性中获取。但是，建议使用secure_filename()函数获取它的安全版本。
    可以在Flask对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。
'''
#1、创建upload.html，写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>upload</title>
</head>
<body>
     <form action = "/uploader" method = "POST"
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
</body>
</html>
'''

# 2、在app.py中写入：
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def func_upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()
















