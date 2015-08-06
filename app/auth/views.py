# -*- coding: utf-8 -*-
__author__ = 'Juner'

from . import auth
from .forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash
from ..models import UserModel
from .. import db
from flask_login import login_user, logout_user, login_required



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserModel(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('你已经注册成功，赶快登录吧')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('你已经登录la')
            return redirect(url_for('main.user', username=user.username))
        flash('用户名或密码错误！')
    return render_template('auth/login.html', form =form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('你已经退出了')
    return redirect(url_for('main.index'))






