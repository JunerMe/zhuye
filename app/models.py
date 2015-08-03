__author__ = 'Juner'

from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class SiteModel(db.Model):
    __tablename__ = 'sitemodels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    site = db.Column(db.String(64), unique=True)
    #user_id = db.Column(db.Integer(64), db.ForeignKey('usersmodel.id'))

    def __repr__(self):
        return '<Site %r>' %self.name

class UserModel(UserMixin, db.Model):
    __tablename__ = 'usersmodel'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    #websites = db.relationship('SiteModel', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('密码不可读取！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def log_user(user_id):
        return UserModel.query.get(int(user_id))

