#-*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import os
from app import create_app
from app.extensions import db
from logging.handlers import TimedRotatingFileHandler
import logging
app = create_app(os.environ.get("FLASK_CONFIG") or "default")





manager = Manager(app)
manager.add_command('db', MigrateCommand)


# @app.route("/add")
# def add():
#     user = User(username="shaowb", email="98", passwd_hash="weq", confirmed=True)
#     db.session.add(user)
#     db.session.commit()
#
#     return "ok221122"
formatter = logging.Formatter(
    "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
handler = TimedRotatingFileHandler(
    "flask.log", when="D", interval=1, backupCount=15,
    encoding="UTF-8", delay=False, utc=True)
app.logger.addHandler(handler)
handler.setFormatter(formatter)
if __name__ == '__main__':
    manager.run()