#-*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
bootstrap = Bootstrap()
