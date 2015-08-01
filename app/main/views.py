__author__ = 'Juner'

from . import main
from flask import render_template, redirect, url_for
from .forms import SiteForm, EditForm
from ..models import SiteModel
from .. import db


#主页路由
@main.route('/', methods=['GET','POST'])
def index():
    form = SiteForm()
    if form.validate_on_submit():
        newsite = SiteModel(name=form.name.data, site=form.site.data)
        db.session.add(newsite)
        return redirect(url_for('.index'))
    sites = SiteModel.query.all()
    return render_template('index.html',form=form, sites=sites)


#编辑网址路由
@main.route('/edit_site',methods=['GET','POST'])
def editsite():
    sites = SiteModel.query.all()
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
