__author__ = 'Juner'

from . import db


class SiteModel(db.Model):
    __tablename__ = 'sitemodels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    site = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Site %r>' %self.name

class UserModel(db.Model):
    __tablename__ = 'usersmodel'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

