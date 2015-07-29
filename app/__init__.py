__author__ = 'Juner'

from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    app.config.from_object(Config)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app