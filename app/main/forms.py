# -*- coding: utf-8 -*-
__author__ = 'Juner'

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SiteForm(Form):
    sitename = StringField('名称',validators=[DataRequired()])
    website = StringField('网址',validators=[DataRequired()])
    submit = SubmitField('添加网址')