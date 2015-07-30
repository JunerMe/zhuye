__author__ = 'Juner'

from . import main
from flask import render_template, redirect, url_for
from .forms import SiteForm
from ..models import SiteModel
from .. import db


@main.route('/', methods=['GET','POST'])
def index():
    form = SiteForm()
    if form.validate_on_submit():
        newsite = SiteModel(name=form.name.data, site=form.site.data)
        db.session.add(newsite)
        return redirect(url_for('.index'))
    sites = SiteModel.query.all()
    return render_template('index.html',form=form, sites=sites)