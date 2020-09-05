'''
configuration file for homeportal project
'''
from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY') or 'my_hard_to_guess_secret_key'
    WTF_CSRF_ENABLED = True

    # Database specific configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = environ.get(
        'PORTAL_DATABASE_URI') or 'sqlite:////tmp/db_dev.sqlite3'
    SQLALCHEMY_BINDS = {
        'kookboek_db': SQLALCHEMY_DATABASE_URI,
        'runner_db': environ.get(
            'RUNNER_DATABASE_URI') or 'sqlite:////tmp/runner_db_dev.sqlite3'
    }
    EXPORT_FOLDER = environ.get('PORTAL_EXPORT_FOLDER') or'/tmp/'


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = environ.get(
        'PORTAL_DATABASE_URI') or 'sqlite:////tmp/db_test.sqlite3'
    SQLALCHEMY_BINDS = {
        'kookboek_db': SQLALCHEMY_DATABASE_URI,
        'runner_db': environ.get(
            'RUNNER_DATABASE_URI') or 'sqlite:////tmp/runner_db_test.sqlite3'
    }
    EXPORT_FOLDER = environ.get('PORTAL_EXPORT_FOLDER') or'/tmp/'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = environ.get(
        'PORTAL_DATABASE_URI') or 'sqlite:////usr/tmp/db.sqlite3'
    SQLALCHEMY_BINDS = {
        'kookboek_db': SQLALCHEMY_DATABASE_URI,
        'runner_db': environ.get(
            'RUNNER_DATABASE_URI') or 'sqlite:////tmp/runner_db.sqlite3'
    }
    EXPORT_FOLDER = environ.get('PORTAL_EXPORT_FOLDER') or'/tmp/'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
