__author__ = 'Juner'

from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap.init_app(app)
    db.init_app(app)



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app