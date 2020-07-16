'''
Main entry point homeportal application
'''
from flask import Flask
from config import config


def create_app(config_name):
    '''
    application factory
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    with app.app_context():

        from home import home

        # Register Blueprints
        app.register_blueprint(home.home_bp, url_prefix='/')

        return app
