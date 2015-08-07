__author__ = 'Juner'

from . import main
from flask import render_template, redirect, url_for, abort, flash
from .forms import SiteForm, EditForm
from ..auth.forms import RegisterForm
from ..models import SiteModel, UserModel
from .. import db
from flask_login import current_user


#主页路由
@main.route('/', methods=['GET','POST'])
def index():
    form = RegisterForm()


    if form.validate_on_submit():
        user = UserModel(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('你已经注册成功，赶快登录吧')
        return redirect(url_for('auth.login'))
    '''
    form = SiteForm()
    if form.validate_on_submit():
        newsite = SiteModel(name=form.name.data, site=form.site.data)
        db.session.add(newsite)
        return redirect(url_for('.index'))
        '''
    sites = SiteModel.query.all()

    #sites_dict = {}
    sites_list = []
    for site in sites:
        site_users = site.user.all()
        site_users_num = len(site_users)
        #sites_dict[site.name] = site_users_num
        asite = [site.name, site_users_num, site.site]
        sites_list.append(asite)
    sorted_sites = sorted(sites_list, key=lambda e:e[1], reverse= True)
    return render_template('index.html', form=form, sites=sites, sorted_sites=sorted_sites, site_users=site_users)


#编辑网址路由
@main.route('/edit_site',methods=['GET','POST'])
def editsite():
    user = current_user._get_current_object()
    sites = user.sites.all()
    #sites = SiteModel.query.all()
    return render_template('edit-site.html', sites=sites)

#编辑单个路由
@main.route('/edit/<int:id>', methods=['GET','POST'])
def edit_id(id):
    form = EditForm()
    site =  SiteModel.query.get(id)
    if form.validate_on_submit():
        site.name = form.name.data
        site.site = form.site.data
        db.session.add(site)
        return redirect(url_for('.editsite'))
    form.name.data = site.name
    form.site.data = site.site
    return render_template('edit-id.html', form = form, site=site)

#删除网站
@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete_id(id):
    site =  SiteModel.query.get(id)
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for('.editsite'))

@main.route('/<username>', methods=['GET','POST'])
def user(username):
    form = SiteForm()
    user = UserModel.query.filter_by(username=username).first()

    if user is None:
        abort(404)
    if form.validate_on_submit():
        site = SiteModel.query.filter_by(site=form.site.data).first()
        newsite = SiteModel(name=form.name.data, site=form.site.data)#, user=current_user._get_current_object())
        if site is  None:
            db.session.add(newsite)
            user.sites.append(newsite)
        else:
            user.sites.append(site)
        db.session.add(user)

    sites = user.sites.all()
    return render_template('user.html', form=form, user=user, sites=sites)



