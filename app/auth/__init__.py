# -*- coding: utf-8 -*-
__author__ = 'Juner'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
