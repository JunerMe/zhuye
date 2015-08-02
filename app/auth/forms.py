# -*- coding: utf-8 -*-
__author__ = 'Juner'

#注册用户表单
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from ..models import UserModel



class RegisterForm(Form):
    email = StringField('邮箱',validators=[InputRequired(), Email()])
    username = StringField('用户名',validators=[InputRequired(), Length(6, 64)])
    password = PasswordField('密码', validators=[InputRequired(), Length(6,64), EqualTo('password2', message='两次输入密码不一致，请重新输入')])
    password2 = PasswordField('确认密码', validators=[InputRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if UserModel.query.filter_by(email=field.data).first():
            raise ValueError('呃呃，这个邮箱已经注册过啦')


    def validate_username(self, filed):
        if UserModel.query.filter_by(username=filed.data).first():
            raise ValueError('呃呃，这个用户名已经被注册啦，换一个吧')


