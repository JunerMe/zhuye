# -*- coding: utf-8 -*-
__author__ = 'Juner'



from flask_wtf import Form
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired, length
from ..models import SiteModel

#首页表单
class SiteForm(Form):
    name = StringField('名称',validators=[InputRequired(), length(1,64)])
    site = StringField('网址',validators=[InputRequired()])
    submit = SubmitField('添加网址')


    def validate_name(self,field):
        if SiteModel.query.filter_by(name=field.data).first():
            raise ValidationError('该网址已经被添加了哦')


    def validate_site(self,field):
        if field.data[:4] != 'www.':
            raise ValidationError('网址应该以“www.”开头！请重新输入')
        if SiteModel.query.filter_by(site=field.data).first():
            raise ValidationError('该网站名已经被添加了哦')


#网页编辑页面表单
class EditForm(Form):
    name = StringField('名称',validators=[length(0,64)])
    site = StringField('网址')
    submit = SubmitField('确认更改')


    def validate_site(self,field):
        if field.data[:4] != 'www.':
            raise ValidationError('网址应该以“www.”开头！请重新输入')