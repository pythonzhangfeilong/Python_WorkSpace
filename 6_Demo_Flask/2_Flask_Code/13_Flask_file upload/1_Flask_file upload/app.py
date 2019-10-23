from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import os
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
