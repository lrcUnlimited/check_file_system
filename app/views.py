__author__ = 'li'
# -*- coding: gb2312 -*-


from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os, file_sim_hash, codecs
from app import app

# 上传文件保存目录
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# 允许文件上传的格式
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])
# 允许文件上传的最大大小
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# 判断一个文件是否允许上传
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            fname = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
            minfilepath, sourcefile, min_distance, sim_percent = file_sim_hash.get_simlar_file(
                os.path.join(app.config['UPLOAD_FOLDER'], fname))
            print(sim_percent)
            if (min_distance > 6):
                return render_template('results.html', sim_percent=sim_percent, result=u'无重复文件',
                                       sourcefilecontent=sourcefile)
            simfile = codecs.open(minfilepath, 'r', 'gb2312', errors='ignore')
            filecontent = simfile.read()
            print filecontent
            print sourcefile
            simfile.close()
            return render_template('results.html', sim_percent=sim_percent, result=filecontent,
                                   sourcefilecontent=sourcefile)


@app.route('/')
def index():
    return redirect(url_for('upload'), 302)
