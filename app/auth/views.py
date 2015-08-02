# -*- coding: utf-8 -*-
__author__ = 'Juner'

from . import auth
from .forms import RegisterForm
from flask import render_template, redirect, url_for
from ..models import UserModel
from .. import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserModel(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)






