#-*-coding:utf-8-*-
import os

base_dir = os.path.abspath(os.path.dirname(__name__))
class config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "shaowb"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    BASE_DIR = "/home/shaowb/PycharmProjects/blog"

    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'blog'
    USERNAME = 'root'
    PASSWORD = 'shaowb'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    @staticmethod
    def init_app(app):
        pass


class Cloud(config):
    pass
class Test(config):
    pass
class Local(config):
    pass



config = {
    "cloud": Cloud,
    "local": Local,
    "test": Test,
    "default": Local
}