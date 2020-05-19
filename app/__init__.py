#-*-coding:utf-8-*-
from flask import Flask
from app.config import config
from app.extensions import db, migrate, moment, bootstrap
from flaskext.markdown import Markdown

from .home import home as home_bp

def create_app(config_name):

    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(home_bp)
    from app.models import models
    db.init_app(app)
    migrate.init_app(app,db)
    moment.init_app(app)
    bootstrap.init_app(app)
    Markdown(app)
    return app