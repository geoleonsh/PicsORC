# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, RadioField


class PictureForms(FlaskForm):
    pic_file = FileField('image', validators=[FileRequired(message="必须上传图片")], render_kw={"accept": "image/*"})
    pic_type = RadioField('pic-type',
                          choices=[('general', '通用识别'), ('dish', '菜肴识别'), ('car', '车型识别'), ('plant', '植物识别')],
                          render_kw={"placeholder": "单选择类型"}, default='general')
    pic_submit = SubmitField('上传图片')
