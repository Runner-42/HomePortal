'''
Main entry point homeportal application
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config
from .extensions import db_kookboek

csrf = CSRFProtect()


def create_app(config_name):
    '''
    application factory
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    csrf.init_app(app)
    db_kookboek.init_app(app)

    with app.app_context():

        from .home import home
        from .kookboek.routes import kookboek_bp
        # from .runner import runner
        # from .domotica import domotica

        # Database
        db_kookboek.create_all()     # Create all tables

        # Register Blueprints
        app.register_blueprint(home.home_bp, url_prefix='/')
        app.register_blueprint(kookboek_bp, url_prefix='/kookboek')
        # app.register_blueprint(runner.runner_bp, url_prefix='/runner')
        # app.register_blueprint(domotica.domotica_bp, url_prefix='/domotica')

        return app
