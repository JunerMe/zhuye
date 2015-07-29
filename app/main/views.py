__author__ = 'Juner'

from . import main
from flask import render_template
from .forms import SiteForm


@main.route('/', methods=['GET','POST'])
def index():
    form = SiteForm()
    return render_template('index.html',form=form)