from flask import Flask
from config.appconfig import init_app as init_config
from blast import init_app as init_container
from routes import init_app as init_routes


def create_app():
    app = Flask(__name__)
    init_config(app)
    init_container(app)
    init_routes(app)
    return app
