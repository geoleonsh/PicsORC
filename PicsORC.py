#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, redirect, url_for, flash
import shibie
from Forms import PictureForms
from config import MainConfig

app = Flask(__name__, template_folder='templates')
app.config.from_object(MainConfig)
baidu = ''


@app.route('/', methods=['POST', 'GET'])
def index():
    form = PictureForms()
    if form.validate_on_submit():
        image_file = form.pic_file.data
        dir = os.path.join(os.path.dirname(__file__), 'images/', image_file.filename)
        file_type = image_file.filename.split('.')[-1]
        # 判断文件类型
        if file_type not in ['jpg', 'jpeg', 'bmp', 'png']:
            flash("文件类型错误", category='check')
            return redirect(url_for('index'))
        else:
            # 临时存储文件
            image_file.save(dir)
            type = form.pic_type.data
            SB = shibie.ShiBie()
            global baidu
            baidu = SB.get_response(type, dir)
            # 删除临时文件
            os.remove(dir)
            return redirect(url_for('index'))

    return render_template('index.html', orc=baidu, form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
