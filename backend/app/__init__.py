from flask import jsonify
from flask_openapi3 import Info
from flask_openapi3 import OpenAPI

from .exceptions import APIError
from .extensions import socketio, db, cors
from .views import api
from .socketio_handlers import *


def create_app(config_override=None):
    info = Info(title="TIC-TAC-TOE API", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    app.config.from_pyfile('config.py')

    if config_override:
        app.config.update(config_override)

    socketio.init_app(app)
    db.init_app(app)
    cors.init_app(app)

    app.register_api(api)

    @app.errorhandler(APIError)
    def handle_exception(err):
        return jsonify({"message": err.description}), err.code

    return app


_all_ = ['create_app', 'socketio', 'db']
